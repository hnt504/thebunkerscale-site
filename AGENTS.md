# Instructions for AI agents working in this repo

Read `PUBLISHING.md` before changing anything. For writing or rating posts, also read `EDITORIAL.md`;
for the daily AI Safety Watch (or an alert Heather pastes in), follow `WATCH.md`. The essentials:

- Posts are source files in `content/posts/`. A post goes live when its source file reaches `main`.
- Never edit generated files (`index.html`, `posts/`, `ratings/`, `ignore/`, the static page folders,
  `404.html`, `rss.xml`, `feed.xml`, `sitemap.xml`, `llms.txt`). The build overwrites them.
- Design changes go in `templates/` and `assets/`; site-wide settings and the current reading in `site.yml`.
- Run `python3 tools/build.py --check` before pushing. No em dashes, never the word "signal",
  and rated posts need the five required sections in order.
- Drafts go in through pull requests. Never push a new post or rating change straight to `main`; Heather publishes by merging.
