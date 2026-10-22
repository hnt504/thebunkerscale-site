"""House rules every post must pass before it can go live.

Ported from the bots' original validate.py, so a post that passed there passes here:
  * no em dashes (Heather's rule) in a post's title, description or body
  * no use of the word "signal" (also Heather's rule)
  * a rated post has the "Rating as of" line and the five required sections, in order
  * a rating is a whole number from 0 to 10
  * the primary source should be marked "(primary source)"  (warning only)
  * internal links point at pages that exist                 (checked after the build)
"""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

EM_DASH = "—"
SIGNAL = re.compile(r"\bsignal(s|led|ing|ed)?\b", re.IGNORECASE)


def _text(fragment: str) -> str:
    return re.sub(r"<[^>]+>", " ", fragment)


def check(site: dict, posts: list[dict], required: list[str]) -> tuple[list[str], list[str]]:
    problems: list[str] = []
    warnings: list[str] = []
    seen: dict[str, str] = {}
    cr = site.get("current_reading") or {}
    if cr and not 0 <= int(cr.get("value", -1)) <= 10:
        problems.append("site.yml: current_reading value must be 0 to 10")
    if cr and EM_DASH in str(cr.get("summary", "")):
        problems.append("site.yml: the current reading summary contains an em dash")
    for p in posts:
        name = p["source"].name
        if p["slug"] in seen:
            problems.append(f"{name}: slug '{p['slug']}' is also used by {seen[p['slug']]}")
        seen[p["slug"]] = name
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", p["slug"]):
            problems.append(f"{name}: slug '{p['slug']}' should be lowercase words joined by hyphens")
        if not p["description"]:
            problems.append(f"{name}: needs a description (it's used on cards, in search results and in the feed)")
        if p["rating"] is not None and not 0 <= p["rating"] <= 10:
            problems.append(f"{name}: rating must be 0 to 10, got {p['rating']}")

        text = " ".join([p["title"], p["description"], _text(p["body_html"])])
        if EM_DASH in text:
            problems.append(f"{name}: contains an em dash. Use a comma, colon, period or parentheses instead.")
        if SIGNAL.search(text):
            problems.append(f"{name}: uses the word \"signal\". Pick another word.")

        if p["history"] and p["rating"] is not None and p["history"][-1]["rating"] != p["rating"]:
            problems.append(f"{name}: rating is {p['rating']} but the last rating_history entry says "
                            f"{p['history'][-1]['rating']}. Add a rating_history entry for the change.")
        for h in p["history"]:
            if not h["note"]:
                problems.append(f"{name}: every rating_history entry needs a note saying why ({h['date']})")
        if p["rating"] is None:
            continue
        body = p["body_html"]
        if not re.search(r"Rating as of [A-Z][a-z]+ \d{1,2}, \d{4}: \d{1,2}/10", _text(body)):
            problems.append(f"{name}: rated posts need a 'Rating as of <Month D, YYYY>: X/10 · Band' line near the top")
        heads = [re.sub(r"\s+", " ", _text(h)).strip() for h in re.findall(r"<h2[^>]*>([\s\S]*?)</h2>", body)]
        heads = [h.replace("’", "'") for h in heads]
        positions = []
        for section in required:
            if section not in heads:
                problems.append(f"{name}: missing the '## {section}' section")
            else:
                positions.append(heads.index(section))
        if len(positions) == len(required) and positions != sorted(positions):
            problems.append(f"{name}: the required sections are out of order (should be: {', '.join(required)})")
        if "(primary source" not in body:
            warnings.append(f"{name}: no source is marked '(primary source)'")
    return problems, warnings


class _Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src") and value and value.startswith("/") and not value.startswith("//"):
                self.links.append(value)


def check_links(root: Path) -> list[str]:
    problems = []
    pages = [p for p in root.rglob("*.html") if not any(part in {".git", "templates", "content", "node_modules", ".github"} for part in p.relative_to(root).parts)]
    for page in pages:
        parser = _Links()
        parser.feed(page.read_text(encoding="utf-8"))
        for link in parser.links:
            target = link.split("#")[0].split("?")[0]
            if not target:
                continue
            path = root / target.lstrip("/")
            if target.endswith("/"):
                path = path / "index.html"
            if not path.exists():
                problems.append(f"{page.relative_to(root)}: broken link to {link}")
    return problems
