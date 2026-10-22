# Instructions for AI agents working in this repo

Read `PUBLISHING.md` before changing anything. The essentials:

- Posts are source files in `content/posts/`. Publish by adding or editing one and pushing to `main`.
- Never edit generated files (`index.html`, `posts/`, `ratings/`, `ignore/`, the static page folders,
  `404.html`, `rss.xml`, `feed.xml`, `sitemap.xml`, `llms.txt`). The build overwrites them.
- Design changes go in `templates/` and `assets/`; site-wide settings and the current reading in `site.yml`.
- Run `python3 tools/build.py --check` before pushing. No em dashes, never the word "signal",
  and rated posts need the five required sections in order.
