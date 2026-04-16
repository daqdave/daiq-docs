# daiq-docs

DAQ Electronics customer-support documentation, published as a GitHub Pages
site using the [Just the Docs](https://just-the-docs.github.io/just-the-docs/)
theme.

Source PDFs are converted to Markdown (with images extracted to a sibling
`images/` folder) using the `scripts/pdf_to_markdown.py` converter.

## First time here?

**Open [`SETUP-GUIDE.md`](./SETUP-GUIDE.md)** — it walks you step-by-step
through installing GitHub Desktop, putting this folder on GitHub, enabling
GitHub Pages, and adding new articles. Written for someone who has never used
Git or GitHub before.

## Repo layout

```
daiq-docs/
├── _config.yml                       # Jekyll / Just-the-Docs site config
├── Gemfile                           # Optional — only needed to build locally
├── index.md                          # Landing page of the docs site
├── docs/
│   └── how-to-shrink-sql-database-log-files/
│       ├── index.md                  # The converted article
│       └── images/                   # Screenshots referenced by the article
│           ├── HowToShrinkSQLDatabaseLogFiles_01.png
│           └── ...
└── scripts/
    └── pdf_to_markdown.py            # PDF → Markdown + images converter
```

Each article lives in its own slug-named folder under `docs/`, containing
its own `index.md` and `images/` subfolder. This keeps each article
self-contained and gives it a clean URL (`/docs/<slug>/`).

## Adding a new article (quick reference)

```bash
python scripts/pdf_to_markdown.py source_pdfs/NewArticleName.pdf docs --jekyll --nav-order 20
```

Then commit and push via GitHub Desktop (or `git add`/`commit`/`push`).

For details, batch conversion of all PDFs at once, script dependencies, and
Windows-specific commands, see **[`SETUP-GUIDE.md`](./SETUP-GUIDE.md)**.
