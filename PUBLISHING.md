# Publishing The Bunker Scale

**Short version: write a Markdown file in `content/posts/`, push it to `main`, and you're done.**
GitHub rebuilds the whole site, checks the house rules, deploys it, and tells search
engines. Nothing else needs to run anywhere.

This replaces the old workflow (`build/publish.sh`, `build.py`, `validate.py`,
`lead-magnet-patch.py` and `indexnow.py` on the publishing box). Retire those. In
particular, **do not write or copy HTML into `posts/`, `index.html` or any other
generated file.** If that happens anyway, the build imports the HTML back into
`content/` so nothing is lost, but it's a safety net, not the process.

## What lives where

| Path | What it is | Edit it? |
|---|---|---|
| `content/posts/*.md` | Posts (Markdown with front matter). Older posts are `.html` with the same front matter. | Yes |
| `content/pages/*.html` | About, How the Ratings Work, Privacy | Yes |
| `site.yml` | Site name, tagline, email, beehiiv and GoatCounter settings, the six scale bands, **the current reading** | Yes |
| `templates/*.html` | Page layouts (Jinja2): header, footer, signup box, post page, homepage... | Yes, for design changes |
| `assets/` | CSS, fonts, icons, OG image | Yes |
| `free/` | The fridge checklist PDFs | Yes |
| `tools/` | The build, validator, importer and IndexNow scripts | Rarely |
| `index.html`, `posts/`, `ratings/`, `ignore/`, `about/`, `how-the-ratings-work/`, `privacy/`, `404.html`, `rss.xml`, `feed.xml`, `sitemap.xml`, `llms.txt` | **Generated.** Rebuilt on every push. | **No** |

## Publishing a post

1. Create `content/posts/<slug>.md`:

   ```markdown
   ---
   title: AI Agents Are Knocking on the Bank Door. Banks Are Starting to Lock It.
   date: 2026-10-22
   order: 1
   rating: 7
   slug: ai-agents-knocking-on-the-bank-door
   type: Safety Watch
   description: One or two plain sentences. Used on cards, in search results and in the feed.
   ---

   *Rating as of October 22, 2026: 7/10 · Pay Attention*

   *Optional italic dek.*

   ## What changed
   ...
   ```

   - `rating` is a whole number 0 to 10. Leave it out for unrated pieces (like the launch post).
   - `type` is the small label above the headline (Safety Watch, Briefing, Launch post).
   - `order` only matters on a day with more than one post: higher shows first. Default 0.
   - `draft: true` keeps a post off the site.
   - `band:` is optional and ignored. The band always comes from `rating`.
   - Don't hand-write the "BUNKER SCALE: X/10" header or the fridge-checklist box. The template adds both.

2. Push to `main`. Within a couple of minutes the post is live, the homepage, archive,
   ratings page, ignore page, feeds, sitemap and `llms.txt` are updated, and IndexNow is pinged.

To check a post before pushing, run `pip install -r requirements.txt` once, then
`python3 tools/build.py --check`. It runs every check and lists what would change without
writing anything.

## Article anatomy (required for every rated post)

The prose can be anything; the structure can't. The build refuses to publish a rated post
unless it has:

1. The `*Rating as of <Month D, YYYY>: X/10 · Band*` line near the top.
2. These H2 sections, in this order (other sections, a Bunker Check quote, a closer or
   `## Sources` can go around or after them):
   - `## What changed`
   - `## Why it matters`
   - `## What you can probably ignore`
   - `## Why it earned this rating`
   - `## What I'm watching next`
3. A `## Sources` list, with the primary source marked "(primary source)". (A missing marker is a warning, not a failure.)

Two formats get picked up automatically, so keep using them:

- **What you can probably ignore:** start each item with the scary claim in bold quotes,
  then the reason, e.g. `**"AI is draining people's bank accounts."** Nobody in these reports...`.
  These feed the homepage "What you can probably ignore" section and the `/ignore/` page.
- **Bunker Check:** a blockquote starting `> **Bunker Check**` with a `**Direction:**` line.
  It's styled as a box on the post, and the direction shows on the Ratings page.

## House rules (the build fails on these)

- No em dashes (—) anywhere in a post's title, description or body.
- Never use the word "signal".
- Rated posts follow the anatomy above.
- A post's `rating` must match its latest `rating_history` entry (see below).
- Internal links must point at pages that exist.

Voice rules from the brief still apply even though no script can check them: warm and
serious, humble, absurd humor only, no stacked short-sentence drama, nothing that sounds
like claiming superior judgment.

## Changing a rating

Ratings change in public. Edit the post's source file:

1. Set `rating:` to the new number.
2. Add `rating_history` with the original rating and the change, each with a short reason:

   ```yaml
   rating: 8
   rating_history:
     - date: 2026-10-22
       rating: 7
       note: Original rating.
     - date: 2026-10-28
       rating: 8
       note: The Fed confirmed specific cases of agents moving money customers didn't authorize.
   ```

3. Update the `*Rating as of ...*` line and the Bunker Check box in the body.

The post shows a "Rating history" box and an "Updated" date, and the change is listed on
`/ratings/#changes`.

## The current reading

The homepage gauge points at one overall reading for the whole AI-risk picture, set in
`site.yml` under `current_reading` (value, date, direction and a short plain-English summary).
It's a judgment, not an average of the posts. A weekly look is plenty. When it changes, move the
old one into `reading_history` with a note, so the Ratings page keeps the record.

## If a publish fails

The build runs as the "Build and publish" GitHub Action. If a post breaks a rule, the
action fails, nothing new goes live, and GitHub emails the repo owner. The log (repo →
Actions tab) says exactly which file and which rule. Fix the source file and push again.

## Settings that used to be in build.py

- beehiiv form ID, subscribe link, Family AI Safety Guide link: `site.yml` → `beehiiv`
- GoatCounter: `site.yml` → `goatcounter`
- Signup box copy (regular and fridge-checklist versions): `templates/_macros.html` → `subscribe`
- Fridge-checklist box inside posts: `LM_BOX` in `tools/build.py` (inserted before the 2nd H2)
- Feed styling: `rss.css` at the root
- IndexNow: the key file at the root; the workflow pings automatically
