#!/usr/bin/env python3
"""
markdown_to_html.py — Convert daiq-docs markdown articles into self-contained
HTML files with base64-embedded images.

Behavior
--------
- Reads docs/<slug>/index.md
- Preserves the Jekyll front matter unchanged so the Just-the-Docs theme,
  navigation, and search index continue to work.
- Hashes every referenced image. If any single image hash appears LOGO_THRESHOLD
  or more times within one article, the script treats it as a repeated logo /
  banner: the first occurrence is kept, all subsequent occurrences are stripped.
- All non-logo image references (including images that legitimately appear 2-4
  times) are preserved.
- Remaining image references are inlined as base64 data URIs.
- Markdown body is converted to HTML using Python-Markdown with the tables,
  attr_list, fenced_code, and toc extensions. The toc extension auto-generates
  `id` attributes on headings so deep links continue to work.
- Output is written to docs/<slug>/index.html.

Usage
-----
    python scripts/markdown_to_html.py --all
    python scripts/markdown_to_html.py docs/how-to-shrink-sql-database-log-files
    python scripts/markdown_to_html.py docs/some-slug --dry-run
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import re
import sys
from pathlib import Path

import markdown

LOGO_THRESHOLD = 5  # image repeated this many times in one article -> drop dupes

IMAGE_REF_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
}


def split_front_matter(text: str) -> tuple[str, str]:
    """Return (front_matter_block, body). Front matter is delimited by --- on
    its own line at the very top of the file. If absent, returns ('', text)."""
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    front = text[: end + 5]  # includes the trailing ---\n
    body = text[end + 5 :]
    return front, body


def hash_image(image_path: Path) -> str:
    return hashlib.md5(image_path.read_bytes()).hexdigest()


def image_data_uri(image_path: Path) -> str:
    suffix = image_path.suffix.lower()
    mime = MIME_TYPES.get(suffix, "application/octet-stream")
    data = image_path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{b64}"


def resolve_image_path(article_dir: Path, ref: str) -> Path:
    """Resolve a markdown image-ref string to a filesystem path."""
    clean = ref.strip()
    if clean.startswith("./"):
        clean = clean[2:]
    return article_dir / clean


def process_article(article_dir: Path, dry_run: bool = False) -> dict:
    """Convert <article_dir>/index.md to <article_dir>/index.html with embedded
    images. Returns a stats dict."""
    slug = article_dir.name
    md_path = article_dir / "index.md"
    html_path = article_dir / "index.html"

    if not md_path.exists():
        return {"slug": slug, "skipped": True, "reason": "no index.md"}

    text = md_path.read_text(encoding="utf-8")
    front, body = split_front_matter(text)

    # Pass 1: hash every referenced image, count occurrences per hash
    refs = list(IMAGE_REF_RE.finditer(body))
    path_to_hash: dict[str, str | None] = {}
    hash_count: dict[str, int] = {}
    missing: list[str] = []

    for m in refs:
        path_str = m.group(2).strip()
        if path_str in path_to_hash:
            # Path already seen; just bump the count for its hash
            h = path_to_hash[path_str]
            if h is not None:
                hash_count[h] = hash_count.get(h, 0) + 1
            continue
        img_path = resolve_image_path(article_dir, path_str)
        if not img_path.exists():
            missing.append(path_str)
            path_to_hash[path_str] = None
            continue
        h = hash_image(img_path)
        path_to_hash[path_str] = h
        hash_count[h] = hash_count.get(h, 0) + 1

    # Identify logo hashes (appearing LOGO_THRESHOLD+ times)
    logo_hashes = {h for h, c in hash_count.items() if c >= LOGO_THRESHOLD}

    # Pass 2: rewrite body — for logo hashes keep first only, strip rest;
    # for everything else embed as data URI.
    seen_logo: set[str] = set()
    dropped = 0
    embedded = 0

    def replace(m: re.Match) -> str:
        nonlocal dropped, embedded
        alt = m.group(1)
        path_str = m.group(2).strip()
        h = path_to_hash.get(path_str)

        if h is None:
            # File not found — leave reference unchanged so the build doesn't
            # silently lose content. This will surface as a broken image on
            # the live site, which is the correct signal.
            return m.group(0)

        if h in logo_hashes:
            if h in seen_logo:
                dropped += 1
                return ""  # strip duplicate logo entirely
            seen_logo.add(h)

        img_path = resolve_image_path(article_dir, path_str)
        data_uri = image_data_uri(img_path)
        embedded += 1
        return f"![{alt}]({data_uri})"

    new_body = IMAGE_REF_RE.sub(replace, body)

    # Convert markdown body to HTML
    md = markdown.Markdown(
        extensions=["tables", "attr_list", "fenced_code", "toc"],
        extension_configs={"toc": {"toc_depth": "2-6"}},
    )
    html_body = md.convert(new_body)

    # Reassemble: front matter + a {% raw %} guard + HTML body
    # The raw guard prevents Jekyll's Liquid processor from interpreting any
    # stray {{ or {% sequences in the rendered body. Front matter is OUTSIDE
    # the guard so Jekyll/Just-the-Docs still see title, layout, nav_order, etc.
    output_parts = [front, "{% raw %}\n", html_body, "\n{% endraw %}\n"]
    output = "".join(output_parts)

    if not dry_run:
        html_path.write_text(output, encoding="utf-8")

    return {
        "slug": slug,
        "refs": len(refs),
        "unique_hashes": len({h for h in path_to_hash.values() if h}),
        "logos_dropped": dropped,
        "embedded": embedded,
        "missing": len(missing),
        "output_bytes": len(output.encode("utf-8")),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument(
        "target",
        nargs="?",
        help="Path to a single article folder (e.g. docs/how-to-shrink-sql-database-log-files). "
        "Omit when using --all.",
    )
    parser.add_argument(
        "--all", action="store_true", help="Process every docs/<slug>/ folder."
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="daiq-docs repository root (default: current dir).",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    docs_dir = repo_root / "docs"

    if args.all:
        article_dirs = sorted(d for d in docs_dir.iterdir() if d.is_dir())
    elif args.target:
        target = Path(args.target)
        if not target.is_absolute():
            target = (repo_root / target).resolve()
        article_dirs = [target]
    else:
        parser.error("Pass an article path OR --all.")

    header = f'{"slug":<72} {"refs":>5} {"uniq":>5} {"drop":>5} {"kb":>9}'
    print(header)
    print("-" * len(header))

    total_embedded = 0
    total_dropped = 0
    total_bytes = 0
    processed = 0
    for d in article_dirs:
        try:
            stats = process_article(d, dry_run=args.dry_run)
        except Exception as e:
            print(f"ERROR processing {d.name}: {e}", file=sys.stderr)
            continue
        if stats.get("skipped"):
            print(f'{stats["slug"]:<72} skipped ({stats["reason"]})')
            continue
        processed += 1
        total_embedded += stats["embedded"]
        total_dropped += stats["logos_dropped"]
        total_bytes += stats["output_bytes"]
        if stats["missing"]:
            note = f' [!] {stats["missing"]} missing img'
        else:
            note = ""
        size_kb = stats["output_bytes"] / 1024
        print(
            f'{stats["slug"]:<72} {stats["refs"]:>5} '
            f'{stats["unique_hashes"]:>5} {stats["logos_dropped"]:>5} '
            f'{size_kb:>9.0f}{note}'
        )

    print("-" * len(header))
    print(
        f"TOTAL: {processed} articles, {total_embedded} images embedded, "
        f"{total_dropped} logo copies stripped, {total_bytes / 1024 / 1024:.1f} MB output"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
