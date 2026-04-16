"""
Convert a customer-support PDF into a Markdown file with sequentially-named
images stored in a sibling images/ folder.

Usage:
    python pdf_to_markdown.py <input.pdf> <output_dir> [--image-url-prefix URL]

For a folder of PDFs:
    for f in /path/to/pdfs/*.pdf; do
        python pdf_to_markdown.py "$f" /path/to/output
    done
"""

import argparse
import os
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF


# DAQ docs use blue for section headings in the PDF (Introduction, Step 1, ...)
HEADING_COLOR_HEX = "1F6FB5"  # approximate blue used in these docs


def color_int_to_hex(color_int: int) -> str:
    """Convert PyMuPDF's integer color to an uppercase 6-char hex string."""
    return f"{color_int & 0xFFFFFF:06X}"


def is_heading_span(span: dict) -> bool:
    """A heading is a larger, blue span that matches 'Step N', 'Introduction', etc."""
    text = span.get("text", "").strip()
    if not text:
        return False
    size = span.get("size", 0)
    color = color_int_to_hex(span.get("color", 0))
    # Heuristic: blue-ish and larger than body text (~11pt)
    is_blueish = color.startswith("1F") or color.startswith("2E") or color.startswith("2F")
    return size >= 13 and is_blueish


def title_from_filename(stem: str) -> str:
    """Convert a PascalCase/CamelCase filename stem into a human title.

    Examples:
        HowToShrinkSQLDatabaseLogFiles -> "How To Shrink SQL Database Log Files"
        Install_ACS_Client             -> "Install ACS Client"
    """
    # Replace separators with spaces first
    s = stem.replace("_", " ").replace("-", " ")
    # Insert space before each capital that follows a lowercase letter: aB -> a B
    s = re.sub(r"([a-z])([A-Z])", r"\1 \2", s)
    # Split runs of capitals from following capital+lowercase: SQLDatabase -> SQL Database
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", s)
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s


def slugify(s: str) -> str:
    """Turn a filename stem or title into a URL-friendly slug."""
    s = re.sub(r"([a-z])([A-Z])", r"\1-\2", s)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1-\2", s)
    s = s.lower().replace("_", "-").replace(" ", "-")
    s = re.sub(r"[^a-z0-9-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def convert_pdf(pdf_path: Path, output_dir: Path, image_url_prefix: str = "",
                jekyll: bool = False, nav_order: int = 0):
    stem = pdf_path.stem  # e.g. HowToShrinkSQLDatabaseLogFiles
    doc = fitz.open(pdf_path)
    title = title_from_filename(stem)

    if jekyll:
        # Jekyll / Just-the-Docs layout: one folder per doc, markdown as index.md
        doc_dir = output_dir / slugify(stem)
        md_filename = "index.md"
    else:
        doc_dir = output_dir / stem
        md_filename = f"{stem}.md"

    img_dir = doc_dir / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    md_lines = []
    if jekyll:
        md_lines += [
            "---",
            "layout: default",
            f"title: {title}",
            f"nav_order: {nav_order}",
            "---",
            "",
        ]
    md_lines += [f"# {title}", ""]
    image_counter = 0
    skipped_banner = False  # skip the first image on page 1 (DAQ logo/banner)

    for page_index, page in enumerate(doc):
        # Build a list of items (text blocks + images) sorted by vertical position.
        items = []

        # Text blocks
        text_dict = page.get_text("dict")
        for block in text_dict["blocks"]:
            if block.get("type") != 0:
                continue
            y_top = block["bbox"][1]
            items.append(("text", y_top, block))

        # Images (use get_image_info for bbox + xref)
        for info in page.get_image_info(xrefs=True):
            xref = info.get("xref", 0)
            if xref == 0:
                continue
            bbox = info.get("bbox", (0, 0, 0, 0))
            items.append(("image", bbox[1], {"xref": xref, "bbox": bbox}))

        items.sort(key=lambda x: x[1])

        seen_xrefs = set()
        for kind, _, payload in items:
            if kind == "text":
                md_lines.extend(render_text_block(payload, page_index, title))
            else:
                xref = payload["xref"]
                if xref in seen_xrefs:
                    continue
                seen_xrefs.add(xref)
                # Skip the very first image on page 1: it's the DAQ logo/title banner.
                if page_index == 0 and not skipped_banner:
                    skipped_banner = True
                    continue
                image_counter += 1
                img_name = f"{stem}_{image_counter:02d}.png"
                img_path = img_dir / img_name
                save_image(doc, xref, img_path)
                link = f"{image_url_prefix}images/{img_name}" if image_url_prefix else f"./images/{img_name}"
                md_lines.append("")
                md_lines.append(f"![{stem} image {image_counter:02d}]({link})")
                md_lines.append("")

    md_path = doc_dir / md_filename
    # Collapse runs of blank lines
    cleaned = []
    prev_blank = False
    for line in md_lines:
        blank = (line.strip() == "")
        if blank and prev_blank:
            continue
        cleaned.append(line)
        prev_blank = blank
    md_path.write_text("\n".join(cleaned).strip() + "\n", encoding="utf-8")

    doc.close()
    return md_path, image_counter


def render_text_block(block: dict, page_index: int, doc_title: str) -> list:
    """Convert a PyMuPDF text block into Markdown lines."""
    title_norm = re.sub(r"\s+", " ", doc_title.strip().lower())
    lines_out = []
    for line in block["lines"]:
        line_text_parts = []
        line_is_heading = False
        for span in line["spans"]:
            text = span.get("text", "")
            if not text.strip():
                line_text_parts.append(text)
                continue
            if is_heading_span(span):
                line_is_heading = True
            line_text_parts.append(text)
        full = "".join(line_text_parts).strip()
        if not full:
            continue
        # Skip the date and the big title banner text on page 1 (we already have H1).
        if page_index == 0 and re.match(
            r"^(January|February|March|April|May|June|July|August|"
            r"September|October|November|December)\s+\d", full
        ):
            continue
        if page_index == 0 and re.sub(r"\s+", " ", full.lower()) == title_norm:
            continue
        if page_index == 0 and full.startswith("Copyright"):
            lines_out.append(f"*{full}*")
            lines_out.append("")
            continue
        if line_is_heading:
            lines_out.append("")
            lines_out.append(f"## {full}")
            lines_out.append("")
            continue
        lines_out.append(full)
    if lines_out and lines_out[-1] != "":
        lines_out.append("")
    return lines_out


def save_image(doc, xref: int, out_path: Path):
    """Extract an embedded image by xref and save it as PNG."""
    pix = fitz.Pixmap(doc, xref)
    if pix.n - pix.alpha >= 4:  # CMYK -> RGB
        pix = fitz.Pixmap(fitz.csRGB, pix)
    pix.save(str(out_path))
    pix = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument(
        "--image-url-prefix",
        default="",
        help="Prefix for image URLs in the markdown (e.g. https://cdn.example.com/docs/mydoc/). "
             "If omitted, relative paths like ./images/<name>.png are used."
    )
    parser.add_argument(
        "--jekyll",
        action="store_true",
        help="Emit Jekyll front matter and use Just-the-Docs folder layout "
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
