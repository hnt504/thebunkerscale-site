"""Turn published HTML pages back into source files.

Used two ways:
  * once, to move the original hand-built site into content/
  * by the build workflow as a safety net: if a bot publishes a post the old
    way (writing posts/<slug>/index.html directly), the post is imported into
    content/posts/ before the site is rebuilt, so nothing gets lost.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

import yaml

LM_BOX = re.compile(r'<aside class="lm-top"[\s\S]*?</aside>\n?')


def _meta(doc: str, attr: str, name: str) -> str | None:
    m = re.search(rf'<meta {attr}="{re.escape(name)}" content="([^"]*)"', doc)
    return html.unescape(m.group(1)) if m else None


def front_matter(meta: dict, body: str) -> str:
    fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=10_000)
    return f"---\n{fm}---\n{body.strip()}\n"


def parse_post(path: Path) -> tuple[dict, str]:
    doc = path.read_text(encoding="utf-8")
    slug = path.parent.name
    meta: dict = {"title": _meta(doc, "property", "og:title")}
    meta["description"] = _meta(doc, "name", "description")
    date = (_meta(doc, "property", "article:published_time") or "")[:10]
    meta["date"] = date
    mod = re.search(r'"dateModified":"([^"]+)"', doc)
    if mod and mod.group(1)[:10] != date:
        meta["updated"] = mod.group(1)[:10]
    rating = re.search(r'<p class="rating-h">BUNKER SCALE: (\d+)/10', doc)
    if rating:
        meta["rating"] = int(rating.group(1))
    meta["slug"] = slug
    kicker = re.search(r'<p class="kicker">([^<]*)</p>', doc)
    if kicker:
        meta["type"] = html.unescape(kicker.group(1))

    start = doc.index("</header>", doc.index('class="post-head"')) + len("</header>")
    end = doc.index('<aside class="post-foot">', start)
    body = LM_BOX.sub("", doc[start:end]).strip()
    meta = {k: v for k, v in meta.items() if v not in (None, "")}
    if not meta.get("title"):
        raise ValueError(f"{slug}: no title found")
    return meta, body


PAGE_INFO = {
    # path: (nav key, breadcrumb name, json-ld type, show subscribe box, show scale strip)
    "about": ("about", "About", "AboutPage", True, False),
    "how-the-ratings-work": ("scale", "How the Ratings Work", "WebPage", True, True),
    "privacy": ("", "", "", False, False),
}


def parse_page(path: Path) -> tuple[dict, str]:
    doc = path.read_text(encoding="utf-8")
    name = path.parent.name
    nav, crumb, ld, subscribe, strip = PAGE_INFO.get(name, ("", "", "", True, False))
    meta = {
        "title": _meta(doc, "property", "og:title"),
        "description": _meta(doc, "name", "description"),
        "nav": nav,
        "breadcrumb": crumb,
        "schema_type": ld,
        "subscribe": subscribe,
        "scale_strip": strip,
    }
    start = doc.index("</header>", doc.index('class="post-head"')) + len("</header>")
    end = doc.index("</article>", start)
    body = doc[start:end]
    body = re.sub(r'^<div class="strip"[\s\S]*?</div>', "", body.lstrip())
    meta = {k: v for k, v in meta.items() if v not in (None, "")}
    return meta, body.strip()


def _norm(fragment: str) -> str:
    return re.sub(r"\s+", " ", fragment).strip()


def import_post(root: Path, slug: str, overwrite: bool = False, render=None) -> Path | None:
    """Import posts/<slug>/index.html into content/posts/.

    With overwrite=True an existing source file is updated rather than replaced:
    front-matter fields the HTML can't express (order, rating_history, ...) are
    kept, and a Markdown source keeps its Markdown body when the published body
    is unchanged. `render` turns a source body into HTML so the two can be compared.
    """
    src = root / "posts" / slug / "index.html"
    dest_dir = root / "content" / "posts"
    existing = sorted(dest_dir.glob(f"{slug}.*"))
    if existing and not overwrite:
        return None
    meta, body = parse_post(src)
    dest_dir.mkdir(parents=True, exist_ok=True)
    if not existing:
        dest = dest_dir / f"{slug}.html"
        dest.write_text(front_matter(meta, body), encoding="utf-8")
        return dest

    old_path = existing[0]
    old_meta, old_body = split_front_matter(old_path.read_text(encoding="utf-8"))
    merged = {**old_meta, **meta}
    old_html = render(old_body, old_path.suffix) if render else old_body
    if _norm(old_html) == _norm(body):
        if merged == old_meta:
            return None
        old_path.write_text(front_matter(merged, old_body), encoding="utf-8")
        return old_path
    for path in existing:
        path.unlink()
    dest = dest_dir / f"{slug}.html"
    dest.write_text(front_matter(merged, body), encoding="utf-8")
    return dest


def split_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    return (yaml.safe_load(fm) or {}), body.strip()


def import_page(root: Path, name: str) -> Path:
    meta, body = parse_page(root / name / "index.html")
    dest = root / "content" / "pages" / f"{name}.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(front_matter(meta, body), encoding="utf-8")
    return dest
