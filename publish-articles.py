#!/usr/bin/env python3
"""Build concubro's essays and discovery files from Markdown plus articles.json."""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
BASE_URL = "https://concubro.com"
ASSET_VERSION = "20260816b"


def load_articles() -> list[dict]:
    articles = json.loads((ROOT / "articles.json").read_text(encoding="utf-8"))
    required = {
        "source", "slug", "title", "description", "published", "modified",
        "reading_minutes", "og_image",
    }
    for article in articles:
        missing = required - article.keys()
        if missing:
            raise ValueError(f"{article.get('slug', 'article')} is missing {sorted(missing)}")
        date.fromisoformat(article["published"])
        date.fromisoformat(article["modified"])
        if not (ROOT / article["source"]).is_file():
            raise FileNotFoundError(article["source"])
    return sorted(articles, key=lambda item: item["published"])


def markdown_blocks(markdown: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph:
            blocks.append(("p", " ".join(line.strip() for line in paragraph)))
            paragraph.clear()

    for line in markdown.replace("\r\n", "\n").split("\n"):
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            flush()
            blocks.append((f"h{len(heading.group(1))}", heading.group(2)))
        elif not line.strip():
            flush()
        else:
            paragraph.append(line)
    flush()
    return blocks


def inline_html(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"\[([^]]+)]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', escaped)
    return escaped


def article_body(markdown: str) -> str:
    blocks = markdown_blocks(markdown)
    if blocks and blocks[0][0] == "h1":
        blocks = blocks[1:]
    return "\n".join(f"      <{tag}>{inline_html(text)}</{tag}>" for tag, text in blocks)


def plain_text(markdown: str) -> str:
    lines = []
    for tag, text in markdown_blocks(markdown):
        lines.append(text)
    return "\n\n".join(lines).strip() + "\n"


def article_html(article: dict, markdown: str) -> str:
    title = html.escape(article["title"])
    description = html.escape(article["description"], quote=True)
    slug = article["slug"]
    page_url = f"{BASE_URL}/{slug}.html"
    txt_url = f"{BASE_URL}/{slug}.txt"
    image_url = f"{BASE_URL}/{article['og_image']}"
    published_date = date.fromisoformat(article["published"])
    day_format = "%#d" if sys.platform == "win32" else "%-d"
    display_date = published_date.strftime(f"%B {day_format}, %Y")
    tldr_prompt = quote(
        "I was too lazy to read this article, briefly summarize it for me.\n\n" + txt_url,
        safe="",
    )
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article["title"],
        "description": article["description"],
        "datePublished": article["published"],
        "dateModified": article["modified"],
        "image": image_url,
        "mainEntityOfPage": page_url,
        "author": {"@type": "Person", "name": "@concubro", "url": f"{BASE_URL}/"},
    }
    schema_json = json.dumps(schema, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <script src="./font-arrival.js?v={ASSET_VERSION}"></script>
  <title>{title} | concubro</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{page_url}" />
  <link rel="alternate" type="text/plain" href="{txt_url}" />
  <link rel="alternate" type="application/atom+xml" title="concubro essays" href="{BASE_URL}/feed.xml" />
  <link rel="icon" href="./favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;1,400&family=Raleway:wght@200;400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./global.css?v={ASSET_VERSION}" />
  <meta property="og:title" content="{title} | concubro" />
  <meta property="og:description" content="{description}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{page_url}" />
  <meta property="og:image" content="{image_url}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:type" content="image/png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title} | concubro" />
  <meta name="twitter:description" content="{description}" />
  <meta name="twitter:image" content="{image_url}" />
  <script type="application/ld+json">
    {schema_json}
  </script>
</head>
<body class="article-page">
  <main class="site-shell">
    <header>
      <nav><a href="./">concubro</a></nav>
      <h1>{title}</h1>
      <p class="meta">@concubro · {display_date} · <a class="tldr-link" href="https://chatgpt.com/?q={tldr_prompt}" target="_blank" rel="noopener noreferrer">TLDR</a></p>
    </header>
    <article id="content">
{article_body(markdown)}
    </article>
  </main>
  <footer>made with notepad in 2026 · <a href="mailto:hello@concubro.com">reach out</a></footer>
  <script src="./false-edge.js?v=20260814e" defer></script>
</body>
</html>
'''


def homepage_row(article: dict) -> str:
    title = html.escape(article["title"])
    description = html.escape(article["description"], quote=True)
    minutes = article["reading_minutes"]
    return (
        f'        <li class="index-item" data-published="{article["published"]}">'
        f'<a class="index-link" href="./{article["slug"]}.html" title="{description}">'
        f'<span class="index-title">{title}</span></a>'
        '<span class="index-fresh" hidden aria-label="Published within the last 30 days"></span>'
        f'<span class="index-meta"> ({minutes}&#8209;min&nbsp;read)</span></li>'
    )


def update_homepage(articles: list[dict]) -> None:
    path = ROOT / "index.html"
    page = path.read_text(encoding="utf-8")
    if 'type="application/atom+xml"' not in page:
        page = page.replace(
            '  <link rel="canonical" href="https://concubro.com/" />',
            '  <link rel="canonical" href="https://concubro.com/" />\n'
            '  <link rel="alternate" type="application/atom+xml" title="concubro essays" href="https://concubro.com/feed.xml" />',
        )
    for article in articles:
        row = homepage_row(article)
        pattern = re.compile(
            rf'^\s*<li class="index-item"[^\n]*href="\./{re.escape(article["slug"])}\.html"[^\n]*</li>\s*$',
            re.MULTILINE,
        )
        if pattern.search(page):
            page = pattern.sub(row, page)
        else:
            page = page.replace("      </ul>", row + "\n      </ul>")
    path.write_text(page, encoding="utf-8", newline="\n")


def update_sitemap(articles: list[dict]) -> None:
    path = ROOT / "sitemap.xml"
    ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", ns)
    tree = ET.parse(path)
    root = tree.getroot()
    existing = {
        node.findtext(f"{{{ns}}}loc"): node for node in root.findall(f"{{{ns}}}url")
    }
    newest = max(article["modified"] for article in articles)
    article_dates = {f"{BASE_URL}/{a['slug']}.html": a["modified"] for a in articles}
    article_dates[f"{BASE_URL}/"] = newest
    for loc, lastmod in article_dates.items():
        node = existing.get(loc)
        if node is None:
            node = ET.SubElement(root, f"{{{ns}}}url")
            ET.SubElement(node, f"{{{ns}}}loc").text = loc
        lastmod_node = node.find(f"{{{ns}}}lastmod")
        if lastmod_node is None:
            lastmod_node = ET.SubElement(node, f"{{{ns}}}lastmod")
        lastmod_node.text = lastmod
    ET.indent(tree, space="  ")
    tree.write(path, encoding="utf-8", xml_declaration=True)


def update_llms(articles: list[dict]) -> None:
    path = ROOT / "llms.txt"
    current = path.read_text(encoding="utf-8")
    optional = current.partition("## Optional")[2].strip()
    lines = [
        "# concubro",
        "",
        "> concubro is a small static site for essays and odd things. Human-facing pages are HTML, and machine-friendly plain-text versions of the essays are linked directly below.",
        "",
        "The canonical HTML contains each complete essay. Plain-text editions are also available for readers that prefer them.",
        "",
        "## Essays",
        "",
    ]
    for article in articles:
        lines.append(
            f'- [{article["title"]}]({BASE_URL}/{article["slug"]}.txt): {article["description"]}'
        )
    if optional:
        lines.extend(["", "## Optional", "", optional])
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def write_feed(articles: list[dict]) -> None:
    latest = max(article["modified"] for article in articles)
    entries = []
    for article in reversed(articles):
        slug = article["slug"]
        page_url = f"{BASE_URL}/{slug}.html"
        entries.append(f'''  <entry>
    <title>{html.escape(article["title"])}</title>
    <link href="{page_url}" />
    <link rel="alternate" type="text/plain" href="{BASE_URL}/{slug}.txt" />
    <id>{page_url}</id>
    <published>{article["published"]}T12:00:00Z</published>
    <updated>{article["modified"]}T12:00:00Z</updated>
    <summary>{html.escape(article["description"])}</summary>
  </entry>''')
    feed = f'''<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>concubro essays</title>
  <link href="{BASE_URL}/feed.xml" rel="self" />
  <link href="{BASE_URL}/" />
  <id>{BASE_URL}/</id>
  <updated>{latest}T12:00:00Z</updated>
  <author><name>@concubro</name><uri>{BASE_URL}/</uri></author>
{chr(10).join(entries)}
</feed>
'''
    (ROOT / "feed.xml").write_text(feed, encoding="utf-8", newline="\n")


def generate_og(article: dict) -> None:
    subprocess.run(
        [
            sys.executable, str(ROOT / "generate-og.py"),
            "--title", article["title"],
            "--description", article["description"],
            "--output", article["og_image"],
        ],
        check=True,
        cwd=ROOT,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build all concubro essays.")
    parser.add_argument(
        "--force-og",
        action="store_true",
        help="Regenerate existing Open Graph cards as well as missing ones",
    )
    args = parser.parse_args()
    articles = load_articles()
    for article in articles:
        markdown = (ROOT / article["source"]).read_text(encoding="utf-8")
        (ROOT / f'{article["slug"]}.html').write_text(
            article_html(article, markdown), encoding="utf-8", newline="\n"
        )
        (ROOT / f'{article["slug"]}.txt').write_text(
            plain_text(markdown), encoding="utf-8", newline="\n"
        )
        if args.force_og or not (ROOT / article["og_image"]).exists():
            generate_og(article)
    update_homepage(articles)
    update_sitemap(articles)
    update_llms(articles)
    write_feed(articles)
    print(f"Built {len(articles)} essays, homepage metadata, sitemap, llms.txt, and feed.xml")


if __name__ == "__main__":
    main()
