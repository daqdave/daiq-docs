"""
Convert a DAQ Electronics customer-support PDF into a Markdown file with
sequentially-named images stored in a sibling images/ folder.

Handles two template families in the daiq-docs source set:

- Template D (e.g. HowToShrinkSQLDatabaseLogFiles): simple legacy layout
  with large blue 13pt+ "Step N" headings and a single DAQ logo banner.

- Template A ("quick guide - *"): branded cover page (skipped), repeating
  blue/grey footer band (skipped), plain bold size-10 body headings (detected),
  italic blue inline emphasis ("Putty", "Management Console", etc.) preserved
  as markdown italics. Template A is detected by the presence of a running
  bold blue 10pt title in the footer band of page 0.

Usage:
    python pdf_to_markdown.py <input.pdf> <output_dir> [options]

Jekyll mode (for daiq-docs):
    python pdf_to_markdown.py file.pdf docs/ --jekyll --nav-order 10
"""

import argparse
import re
from pathlib import Path

import fitz  # PyMuPDF


# Layout-tuned thresholds (US Letter portrait, DAQ quick-guide template family).
FOOTER_Y_THRESHOLD = 725.0   # anything at or below this is footer chrome
COVER_Y_THRESHOLD = 250.0    # on page 0 (Template A), anything above this is cover art
HEADING_MIN_BLUE_SIZE = 13.0 # blue spans >= 13pt are Template D section headings
HEADING_MIN_BOLD_SIZE = 10.0 # fully-bold lines >= 10pt are Template A section headings
COPYRIGHT_MAX_SIZE = 8.5     # spans smaller than this on page 0 are copyright boilerplate


def color_to_rgb(color_int: int):
    r = (color_int >> 16) & 0xFF
    g = (color_int >> 8) & 0xFF
    b = color_int & 0xFF
    return r, g, b


def is_white(color_int: int) -> bool:
    return (color_int & 0xFFFFFF) == 0xFFFFFF


def is_blueish(color_int: int) -> bool:
    r, g, b = color_to_rgb(color_int)
    return b > 120 and r < 120


def is_bold_flag(flags: int) -> bool:
    # PyMuPDF exposes bold in flags bit 4 (value 16).
    return bool(flags & 16)


def is_italic_flag(flags: int) -> bool:
    # PyMuPDF exposes italic in flags bit 1 (value 2).
    return bool(flags & 2)


def line_y_top(line: dict) -> float:
    return line["bbox"][1]


def non_ws_spans(line: dict):
    return [s for s in line["spans"] if s.get("text", "").strip()]


def line_plain_text(line: dict) -> str:
    return "".join(s.get("text", "") for s in line["spans"]).strip()


def line_is_all_bold_heading(line: dict) -> bool:
    """All visible spans on this line are bold, >= 10pt, and not white."""
    spans = non_ws_spans(line)
    if not spans:
        return False
    for s in spans:
        if is_white(s.get("color", 0)):
            return False
        if s.get("size", 0) < HEADING_MIN_BOLD_SIZE:
            return False
        if not is_bold_flag(s.get("flags", 0)):
            return False
    return True


def line_is_all_blue_heading(line: dict) -> bool:
    """All visible spans are blueish and >= 13pt (legacy Template D heading)."""
    spans = non_ws_spans(line)
    if not spans:
        return False
    for s in spans:
        if s.get("size", 0) < HEADING_MIN_BLUE_SIZE:
            return False
        if not is_blueish(s.get("color", 0)):
            return False
    return True


# Explicit DAQ step-heading convention (e.g., "Step 1 – Login via Putty").
STEP_HEADING_RE = re.compile(r"^\s*Step\s+\d+\s*[–\-:]", re.I)

# Template B/C: enter skip mode on any of these (strips the 2-page legal wall + TOC).
LEGAL_WALL_ENTER_RE = re.compile(
    r"^\s*\**\s*("
    r"COPYRIGHT|TRADEMARKS|PROPRIETARY\s+INFORMATION|TABLE\s+OF\s+CONTENTS"
    r")\s*\**\s*$",
    re.I,
)

# Template B/C: exit skip mode on the first real numbered heading (e.g., "1.0 DOWNLOADING...").
# TOC entries also match this pattern but end with a page number, so we require the line
# to NOT end in a bare digit. Also cap length so dotted TOC lines are excluded.
NUMBERED_HEADING_RE = re.compile(r"^\d+(\.\d+){0,5}\s+[A-Z]")


def is_numbered_body_heading(text: str) -> bool:
    if not NUMBERED_HEADING_RE.match(text):
        return False
    if len(text) > 90:
        return False
    # TOC rows end in a page number: "... some text ........ 4"
    if re.search(r"\s\d+\s*$", text):
        return False
    # Too many consecutive dots → TOC leader dots
    if "..." in text:
        return False
    return True


def looks_like_single_line_heading(block: dict, line: dict, line_text: str) -> bool:
    """Heuristic: a one-line block with short, sentence-less text is a heading.

    Catches DAQ docs where section headings are rendered as plain 10pt text
    with extra whitespace rather than bold (e.g. the VLC quick guide).
    Excludes tiny diagram annotations (< 9pt) and table cells.
    """
    if len(block.get("lines", [])) != 1:
        return False
    # Font size guard: reject anything smaller than body text (diagram labels).
    if line_max_size(line) < 9.0:
        return False
    t = line_text.strip()
    if len(t) < 2 or len(t) > 45:
        return False
    if t.endswith((".", ",", ";", ":", "!", "?", ")")):
        return False
    # Reject bullets / numbered list items / URLs of any scheme / file paths.
    if re.match(r"^(\d+[\.\)]|[-*•]\s|\w+://|[A-Za-z]:\\|[/\\])", t):
        return False
    # Reject filenames: a single token ending in ".ext" (e.g. "StarWatch_SMS.lic").
    if " " not in t and re.search(r"\.[A-Za-z0-9]{2,5}$", t):
        return False
    # Require first non-space char to be uppercase or digit (not lowercase prose).
    first = t.lstrip()[:1]
    if not first or not (first.isupper() or first.isdigit()):
        return False
    # At least one letter somewhere.
    if not re.search(r"[A-Za-z]", t):
        return False
    return True


def line_all_white(line: dict) -> bool:
    spans = non_ws_spans(line)
    return bool(spans) and all(is_white(s.get("color", 0)) for s in spans)


def line_max_size(line: dict) -> float:
    spans = non_ws_spans(line)
    if not spans:
        return 0.0
    return max(s.get("size", 0) for s in spans)


def slugify(s: str) -> str:
    """URL-friendly slug: ascii-lowercase, hyphen-separated."""
    s = re.sub(r"([a-z])([A-Z])", r"\1-\2", s)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1-\2", s)
    s = s.lower().replace("_", "-").replace(" ", "-")
    s = re.sub(r"[^a-z0-9-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


# Acronyms / product names that should stay uppercase in titles.
TITLE_KEEP_UPPER = {
    "SMS", "SQL", "LDAP", "VLC", "RPI", "PICS", "SCIF", "DAQ", "USB", "RSM",
    "ERADC", "UDP", "TCP", "IP", "CSV", "PDF", "ACS", "IDS", "FAQ", "DVR",
    "ID", "TCP/IP", "API", "URL", "OS", "UDP", "BACnet",
}
TITLE_SMALL = {"a", "an", "and", "of", "the", "to", "for", "in", "on",
               "with", "via", "from", "your", "as", "at", "by", "or"}


def derive_title_from_stem(stem: str) -> str:
    """Fallback title derivation from the filename stem."""
    s = stem
    # Strip "quick guide - " prefix (Template A naming convention).
    s = re.sub(r"^\s*quick\s+guide\s*-\s*", "", s, flags=re.I)
    # Strip trailing "- rev N" or " rev N".
    s = re.sub(r"\s*-?\s*rev\s*#?\s*\d+\s*$", "", s, flags=re.I)
    # Strip trailing version digit (e.g. "...for video2").
    s = re.sub(r"(?<=\D)\d+\s*$", "", s)
    # Normalise separators.
    s = s.replace("_", " ").replace("-", " ")
    s = re.sub(r"([a-z])([A-Z])", r"\1 \2", s)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", s)
    s = re.sub(r"\s+", " ", s).strip()
    # Title-case while preserving known acronyms and lowercase small words.
    words = []
    for i, w in enumerate(s.split(" ")):
        if not w:
            continue
        up = w.upper()
        if up in TITLE_KEEP_UPPER:
            words.append(up)
        elif w.lower() in TITLE_SMALL and i != 0:
            words.append(w.lower())
        else:
            words.append(w[:1].upper() + w[1:].lower())
    return " ".join(words)


def extract_footer_title(doc) -> str | None:
    """Template A: running title appears at y >= 740 on page 0 in bold blue 10pt.
    Returns the first non-chrome string found in the footer band, or None."""
    if len(doc) == 0:
        return None
    page = doc[0]
    candidates = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block["lines"]:
            y = line_y_top(line)
            if y < FOOTER_Y_THRESHOLD:
                continue
            text = line_plain_text(line)
            if not text:
                continue
            if re.fullmatch(r"\d+", text):           # page number
                continue
            if re.fullmatch(r"quick\s*guide", text, flags=re.I):
                continue
            if re.fullmatch(r"rev\s*#?\s*\d+", text, flags=re.I):
                continue
            # Prefer the blue-bold 10pt span if present.
            for s in line["spans"]:
                txt = s.get("text", "").strip()
                if not txt:
                    continue
                if is_bold_flag(s.get("flags", 0)) and is_blueish(s.get("color", 0)):
                    candidates.append(txt)
                    break
            else:
                candidates.append(text)
    return candidates[0] if candidates else None


def render_line_body(line: dict) -> str:
    """Render a body line with inline bold/italic preserved, skipping white spans."""
    parts = []
    for span in line["spans"]:
        text = span.get("text", "")
        if not text:
            continue
        color = span.get("color", 0)
        if is_white(color):
            continue
        flags = span.get("flags", 0)
        bold = is_bold_flag(flags)
        italic = is_italic_flag(flags)
        if not text.strip():
            # pure whitespace — keep as-is
            parts.append(text)
            continue
        m = re.match(r"^(\s*)(.*?)(\s*)$", text, flags=re.DOTALL)
        leading, core, trailing = m.group(1), m.group(2), m.group(3)
        if not core:
            parts.append(text)
            continue
        if bold and italic:
            wrapped = f"***{core}***"
        elif bold:
            wrapped = f"**{core}**"
        elif italic:
            wrapped = f"*{core}*"
        else:
            wrapped = core
        parts.append(f"{leading}{wrapped}{trailing}")
    return "".join(parts).strip()


def escape_yaml(s: str) -> str:
    """Quote YAML scalar if it contains characters that could break front matter."""
    if any(ch in s for ch in [":", "'", '"', "#", "\\"]):
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s


def save_image(doc, xref: int, out_path: Path):
    """Extract an embedded image by xref and save it as PNG."""
    pix = fitz.Pixmap(doc, xref)
    if pix.n - pix.alpha >= 4:  # CMYK -> RGB
        pix = fitz.Pixmap(fitz.csRGB, pix)
    pix.save(str(out_path))
    pix = None  # noqa: F841  (ensures pixmap is released)


def convert_pdf(pdf_path: Path, output_dir: Path, image_url_prefix: str = "",
                jekyll: bool = False, nav_order: int = 0):
    doc = fitz.open(pdf_path)
    stem = pdf_path.stem

    footer_title = extract_footer_title(doc)
    template_a_mode = footer_title is not None
    title = footer_title or derive_title_from_stem(stem)

    slug = slugify(stem)
    doc_dir = output_dir / slug
    md_filename = "index.md" if jekyll else f"{slug}.md"
    img_dir = doc_dir / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    md_lines = []
    if jekyll:
        md_lines += [
            "---",
            "layout: default",
            f"title: {escape_yaml(title)}",
            f"nav_order: {nav_order}",
            "---",
            "",
        ]
    md_lines += [f"# {title}", ""]

    image_counter = 0
    skipped_first_banner = False  # legacy Template D behaviour
    legal_wall_mode = False       # Template B/C: swallow copyright + TOC pages

    # First pass: detect Template B/C "formal manual" structure by counting numbered
    # section headings like "1.0 INTRODUCTION", "2.1 ...", etc.  When this mode is on,
    # we suppress the single-line-block heading heuristic (which otherwise promotes
    # table cells such as "Mode" or "Expiration" into spurious ## headings).
    numbered_doc_mode = False
    _numbered_hits = 0
    for _p in doc:
        for _b in _p.get_text("dict")["blocks"]:
            if _b.get("type") != 0:
                continue
            for _line in _b["lines"]:
                _txt = "".join(s.get("text", "") for s in _line["spans"]).strip()
                if is_numbered_body_heading(_txt):
                    _numbered_hits += 1
                    if _numbered_hits >= 3:
                        break
            if _numbered_hits >= 3:
                break
        if _numbered_hits >= 3:
            break
    numbered_doc_mode = _numbered_hits >= 3

    for page_index, page in enumerate(doc):
        items = []

        text_dict = page.get_text("dict")
        for block in text_dict["blocks"]:
            if block.get("type") != 0:
                continue
            for line in block["lines"]:
                items.append(("text_line", line_y_top(line), (line, block)))

        seen_xrefs = set()
        for info in page.get_image_info(xrefs=True):
            xref = info.get("xref", 0)
            if xref == 0 or xref in seen_xrefs:
                continue
            seen_xrefs.add(xref)
            bbox = info.get("bbox", (0, 0, 0, 0))
            items.append(("image", bbox[1], {"xref": xref, "bbox": bbox}))

        items.sort(key=lambda x: x[1])

        title_norm = re.sub(r"\s+", " ", title.strip().lower())

        for kind, y, payload in items:
            if kind == "text_line":
                line, block = payload
                y_top = line_y_top(line)

                # All-pages: drop footer chrome.
                if y_top >= FOOTER_Y_THRESHOLD:
                    continue

                # All-pages: drop invisible banner (white-on-white) text.
                if line_all_white(line):
                    continue

                text = line_plain_text(line)
                if not text:
                    continue

                if template_a_mode and page_index == 0:
                    # Drop cover band.
                    if y_top < COVER_Y_THRESHOLD:
                        continue
                    # Drop copyright wall: everything small-font on page 0.
                    if line_max_size(line) < COPYRIGHT_MAX_SIZE:
                        continue
                    # Drop the known "... Security Suite" subtitle if it slipped through.
                    if re.fullmatch(r"[A-Za-z]+(\s+[A-Za-z]+)*\s+SMS\s+Security\s+Suite",
                                    text, flags=re.I):
                        continue
                elif not template_a_mode and page_index == 0:
                    # Template D legacy cover cleanup: strip date, duplicate title, copyright.
                    if re.match(
                        r"^(January|February|March|April|May|June|July|August|"
                        r"September|October|November|December)\s+\d",
                        text,
                    ):
                        continue
                    if re.sub(r"\s+", " ", text.lower()) == title_norm:
                        continue
                    if text.startswith(("Copyright", "©")):
                        continue

                # Template B/C legal-wall / TOC state machine.
                if legal_wall_mode:
                    if is_numbered_body_heading(text):
                        legal_wall_mode = False  # fall through to heading handling
                    else:
                        continue
                elif LEGAL_WALL_ENTER_RE.match(text):
                    legal_wall_mode = True
                    continue

                # Heading detection, in priority order.
                # Bold / blue heading rules only fire in short blocks (≤3 lines) to avoid
                # promoting bold cells inside multi-row tables.
                short_block = len(block.get("lines", [])) <= 3
                if short_block and line_is_all_blue_heading(line):
                    md_lines += ["", f"## {text}", ""]
                    continue
                if (short_block
                        and line_is_all_bold_heading(line)
                        and 4 <= len(text) <= 80
                        and not text.endswith((".", "?", "!"))):
                    md_lines += ["", f"## {text}", ""]
                    continue
                # DAQ "Step N – ..." sub-heading convention.
                if STEP_HEADING_RE.match(text) and len(text) <= 80:
                    md_lines += ["", f"### {render_line_body(line)}", ""]
                    continue
                # Single-line-block bare-heading heuristic (catches plain-text section titles).
                # Disabled when the doc uses numbered section headings (Template B/C),
                # because otherwise it promotes table cells into headings.
                if not numbered_doc_mode and looks_like_single_line_heading(block, line, text):
                    md_lines += ["", f"## {text}", ""]
                    continue

                body = render_line_body(line)
                if body:
                    md_lines.append(body)
            else:
                xref = payload["xref"]
                bbox = payload["bbox"]
                y_top = bbox[1]

                # Drop footer logos.
                if y_top >= FOOTER_Y_THRESHOLD:
                    continue

                # Drop images while we're swallowing the legal/TOC pages.
                if legal_wall_mode:
                    continue

                if template_a_mode:
                    # Template A: skip all cover-band images on page 0 (hex pattern,
                    # title bar, wordmark, blue divider, DAQ logo).
                    if page_index == 0 and y_top < COVER_Y_THRESHOLD:
                        continue
                else:
                    # Legacy Template D: skip only the very first image on page 0
                    # (the DAQ logo/banner).
                    if page_index == 0 and not skipped_first_banner:
                        skipped_first_banner = True
                        continue

                image_counter += 1
                img_name = f"{slug}_{image_counter:02d}.png"
                img_path = img_dir / img_name
                save_image(doc, xref, img_path)
                link = (f"{image_url_prefix}images/{img_name}"
                        if image_url_prefix else f"./images/{img_name}")
                md_lines += ["", f"![{title} image {image_counter:02d}]({link})", ""]

    # Condensed credit line in lieu of the copyright wall.
    md_lines += ["", "---", "", "*© DAQ Electronics, LLC*", ""]

    # Collapse runs of blank lines.
    cleaned = []
    prev_blank = False
    for line in md_lines:
        blank = (line.strip() == "")
        if blank and prev_blank:
            continue
        cleaned.append(line)
        prev_blank = blank

    md_path = doc_dir / md_filename
    md_path.write_text("\n".join(cleaned).strip() + "\n", encoding="utf-8")
    doc.close()
    return md_path, image_counter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument(
        "--image-url-prefix",
        default="",
        help="Prefix for image URLs in the markdown (e.g. https://cdn.example.com/docs/x/). "
             "If omitted, relative paths like ./images/<name>.png are used."
    )
    parser.add_argument(
        "--jekyll",
        action="store_true",
        help="Emit Jekyll front matter and use Just-the-Docs layout "
             "(one slug-named folder per doc, markdown saved as index.md)."
    )
    parser.add_argument(
        "--nav-order",
        type=int,
        default=0,
        help="When using --jekyll, the nav_order value for this doc."
    )
    args = parser.parse_args()
    md_path, n_imgs = convert_pdf(
        args.pdf, args.output_dir, args.image_url_prefix,
        jekyll=args.jekyll, nav_order=args.nav_order,
    )
    print(f"Wrote {md_path} with {n_imgs} images")


if __name__ == "__main__":
    main()
