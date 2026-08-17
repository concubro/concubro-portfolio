# concubro-portfolio

The static website for concubro.

## Publishing an essay

1. Add the top-level Markdown file.
2. Add its public metadata to `articles.json`.
3. Run `python publish-articles.py`.

The publisher writes complete canonical HTML, a plain-text edition, homepage
metadata, Open Graph art, `sitemap.xml`, `llms.txt`, and `feed.xml`. Existing OG
cards are left alone unless you pass `--force-og`.
