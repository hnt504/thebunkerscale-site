# The daily watch

How Claude runs The Bunker Scale's AI Safety Watch: find what materially changed, write it up,
and hand Heather a ready-to-publish draft. **Nothing goes live until Heather merges it.**

Read `EDITORIAL.md` (judgment and voice) and `PUBLISHING.md` (format and mechanics) first.

## Ground rules

- **Never push to `main` and never merge.** Every draft is a pull request from a `watch/...` branch. Merging is how Heather publishes.
- **Most days, nothing qualifies.** That's the product working, not failing. Don't lower the bar to have something to show.
- **At most two new drafts per run.** If more cleared the bar, pick the most consequential and mention the rest in the run summary.
- **Never invent anything.** Every claim in a draft must match a source opened during this run.

## 1. Get set up

```bash
git clone https://github.com/hnt504/thebunkerscale-site && cd thebunkerscale-site
pip install -r requirements.txt
```

Then take stock so nothing gets covered twice:

- `content/posts/`: everything published, with dates and ratings (`llms.txt` has a one-line list).
- Open pull requests (`gh api repos/hnt504/thebunkerscale-site/pulls`): drafts Heather hasn't decided on yet. Don't duplicate them. If one is more than 7 days old, mention it in the summary.
- The "What I'm watching next" and Bunker Check sections of posts from the last 30 days: these are the follow-ups to look for.

## 2. Sweep (the last 36 hours, or since the newest post or open draft, whichever is longer)

Look in this order, and go to primary sources:

1. **Labs:** Anthropic, OpenAI, Google DeepMind, Meta, xAI, Mistral and other frontier labs: blogs, system and model cards, safety and misalignment reports, deployment or access changes.
2. **Safety and evaluation groups:** METR, Apollo Research, the UK AI Security Institute, the US Center for AI Standards and Innovation, the UN scientific panel on AI, academic preprints that are getting real attention.
3. **Government and regulators:** the White House, Congress, federal agencies (FTC, SEC, CISA and others), state attorneys general and governors, the EU AI Office, the UN, other national governments.
4. **Security incidents:** CISA, national CERTs, and major security firms' threat reports involving AI.
5. **Reporting:** Reuters, AP, Axios, the Financial Times, the Washington Post, the Wall Street Journal, The Verge, Ars Technica, Wired. Use them to find stories and for facts they report themselves, but cite the primary source whenever one exists.
6. **Heather's ChatGPT alerts, if available:** if this session has ChatAtlas, check the "AI Safety Watch" chat for new alerts. Treat them as tips: verify everything before using it.

## 3. Decide

For each candidate, answer "What materially changed?" using `EDITORIAL.md`. Sort into:

- **New post:** clears the bar and isn't already covered.
- **Rating change:** new evidence matches what an existing post said would move its rating ("could move higher/lower if"). Draft the change to that post instead of a new post.
- **Near miss:** real but not enough on its own. List it in the summary. Don't draft it.
- **Ignore:** hype, rhetoric, rumor.

## 4. Draft

**New post:** create `content/posts/<slug>.md` with the front matter from `PUBLISHING.md` and the full article shape from `EDITORIAL.md`. Use today's date. Set `type: Safety Watch` (or `Briefing` for a short one).

**Rating change:** edit that post's source file: new `rating`, a `rating_history` list with the original and the change (each with a one-line reason), an updated "Rating as of" line and Bunker Check, and an "Update, <Month D, YYYY>:" paragraph at the top of "What changed" saying what's new. Keep everything else.

**Pasted alerts:** when Heather pastes one of her ChatGPT alerts into a chat and asks to publish it, follow this same step: reshape it into the article format, keep her alert's rating unless verification gives a clear reason to change it (and say so in the PR), and check it against sources before drafting.

## 5. Verify, then check the build

- Open every cited source again and check each number, quote, date and name against it. Check every link loads. Remove or soften anything that doesn't hold up.
- Run `python3 tools/build.py --check`. Fix every ERROR (em dashes, the word "signal", missing sections, out-of-order sections, missing "Rating as of" line).

## 6. Open the pull request

```bash
git checkout -b watch/<YYYY-MM-DD>-<slug>
git add content/posts/<slug>.md          # source files only, never generated HTML
git commit -m "Draft: <title> (<rating>/10)"
git push -u origin HEAD
```

Open the PR with `gh api repos/hnt504/thebunkerscale-site/pulls` (base `main`). Title: `Draft: <title> (<rating>/10 · <Band>)`. The body is for Heather reading on her phone, in plain English:

- **What happened**, in two or three sentences.
- **Why it cleared the bar**, and the rating with the one-line reason.
- **How it compares** to the closest past ratings.
- **What I checked:** each key claim and the source it was verified against.
- **Not confirmed:** anything uncertain, and how the draft handles it.
- **To publish:** "Merge this pull request. To change anything, comment here or tell Claude in any chat."

## 7. Weekly current-reading review (Fridays)

Read the week's posts and drafts, then ask whether the overall picture moved. If it did, open a separate PR that updates `current_reading` in `site.yml` (move the old reading into `reading_history` with a note) and explain the case in the PR. If it didn't, say so in the summary. Never change the current reading without a PR.

## 8. Friday roundup email (beehiiv draft)

Every Friday, after the current-reading review, draft the week's email to subscribers in beehiiv.
Subscribers get nothing else from the site, so this is their weekly connection to it.

- **Where:** the beehiiv publication "The Bunker Scale" (`pub_358d8b68-a28d-4d38-9842-5326bdc54a01`). Create it with `save_post` as a **draft**. Never schedule or send it; Heather sends it from beehiiv.
- **Title and subject:** "This week on the Bunker Scale: <Month D> to <Month D>". Preview text: the current reading in a few words.
- **What goes in it,** in this order, all in the voice from `EDITORIAL.md` (no em dashes, never "signal"):
  1. One or two sentences on how the week felt.
  2. **The current reading:** the number, band, whether it moved or held, one line on why, linked to https://thebunkerscale.com/ratings/.
  3. **This week's posts** (only posts live on the site this week, newest first): linked title, "X/10 · Band", one sentence on what changed.
  4. **Rating changes** this week, if any, with the reason.
  5. **What you can probably ignore:** the best one from the week's posts, claim plus one-line reason.
  6. A "Bunker status:" closer and a link to the site.
- **Quiet week:** if there were no new posts and the reading held, draft a short note that says so and still gives the current reading. Flag it in the summary so Heather can decide whether to send it.
- If the beehiiv tools aren't available in the run, write the roundup in the summary instead, ready to paste.
- Include the beehiiv editor link in the run summary.

## 9. Report

End every run with a short summary for Heather: drafts opened (with links), the Friday roundup draft (if any), rating changes proposed, near misses in one line each, and anything that's blocking. If nothing cleared the bar, say "Nothing cleared the bar today" and list the top near misses.
