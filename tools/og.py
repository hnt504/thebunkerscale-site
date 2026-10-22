"""Share images: one 1200x630 card per post, showing its Bunker Scale rating.

This is the picture people see when a post is shared on social media, in
iMessage, Slack and so on. Cards are only redrawn when what's on them changes
(title, rating, band), so builds stay fast.
"""

from __future__ import annotations

import hashlib
import io
import json
import math
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "og"
VERSION = "1"  # bump to force every card to be redrawn after a design change

BG = (244, 240, 230)
INK = (30, 31, 27)
MUTED = (93, 90, 80)
LINE = (207, 199, 180)
W, H = 1200, 630


def _font(name: str, size: int) -> ImageFont.FreeTypeFont:
    """The site's own fonts are WOFF2; Pillow needs plain TrueType, so convert in memory."""
    t = TTFont(ROOT / "assets" / "fonts" / f"{name}.woff2")
    t.flavor = None
    buf = io.BytesIO()
    t.save(buf)
    buf.seek(0)
    return ImageFont.truetype(buf, size)


def _axes(name: str, size: int, **values) -> ImageFont.FreeTypeFont:
    font = _font(name, size)
    try:
        names = [a["name"] for a in font.get_variation_axes()]
        names = [n.decode() if isinstance(n, bytes) else n for n in names]
        wanted = {"Weight": values.get("wght"), "Optical size": values.get("opsz"), "Width": values.get("wdth")}
        current = [a["default"] for a in font.get_variation_axes()]
        font.set_variation_by_axes([wanted.get(n) or current[i] for i, n in enumerate(names)])
    except Exception:
        pass
    return font


def _rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _gauge(draw: ImageDraw.ImageDraw, cx: int, cy: int, r: int, bands: list[dict], rating: int | None) -> None:
    """The site's 0-10 gauge: six colored arcs and a needle."""
    for b in bands:
        start = 180 + (b["low"] / 11) * 180 + 1.5
        end = 180 + ((b["high"] + 1) / 11) * 180 - 1.5
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=start, end=end, fill=_rgb(b["color"]), width=46)
    if rating is not None:
        a = math.radians(180 + ((rating + 0.5) / 11) * 180)
        tip = (cx + (r - 12) * math.cos(a), cy + (r - 12) * math.sin(a))
        draw.line([(cx, cy), tip], fill=INK, width=9)
    draw.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=INK)
    draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(209, 138, 18))


def _wrap(draw, text: str, font, width: int) -> list[str]:
    words, lines, line = text.split(), [], ""
    for w in words:
        trial = f"{line} {w}".strip()
        if draw.textlength(trial, font=font) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def card(post: dict, site: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    band = post.get("band")
    accent = _rgb(band["color"]) if band else (107, 114, 83)
    d.rectangle([0, 0, W, 14], fill=accent)

    label = _axes("plex-sans", 24, wght=700)
    d.text((72, 64), "THE BUNKER SCALE", font=label, fill=INK)

    # title: largest size that fits in 4 lines
    for size in (64, 58, 52, 46, 40):
        title_font = _axes("newsreader", size, wght=600, opsz=48)
        lines = _wrap(d, post["title"], title_font, 690)
        if len(lines) <= 4:
            break
    lines = lines[:4]
    y = 140
    for line in lines:
        d.text((72, y), line, font=title_font, fill=INK)
        y += int(size * 1.18)

    # rating badge
    if post.get("rating") is not None:
        big = _axes("plex-sans", 40, wght=700)
        text = f"{post['rating']}/10 · {band['name'].upper()}"
        tw = d.textlength(text, font=big)
        lum = (0.299 * accent[0] + 0.587 * accent[1] + 0.114 * accent[2]) / 255
        d.rounded_rectangle([72, 488, 72 + tw + 44, 552], radius=8, fill=accent)
        d.text((94, 495), text, font=big, fill=INK if lum > 0.6 else (255, 255, 255))
    else:
        small = _axes("plex-sans", 30, wght=600)
        d.text((72, 500), (post.get("kicker") or "").upper(), font=small, fill=MUTED)

    foot = _axes("plex-sans", 22, wght=500)
    d.text((72, 578), site["url"].split("://", 1)[1], font=foot, fill=MUTED)

    _gauge(d, 985, 370, 165, site["bands"], post.get("rating"))
    nums = _axes("plex-sans", 22, wght=500)
    d.text((985, 410), "0 = background noise", font=nums, fill=MUTED, anchor="mm")
    d.text((985, 440), "10 = get in the bunker", font=nums, fill=MUTED, anchor="mm")
    return img


def fingerprint(post: dict) -> str:
    data = {"v": VERSION, "title": post["title"], "rating": post.get("rating"),
            "band": (post.get("band") or {}).get("name"), "kicker": post.get("kicker")}
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]


def ensure_cards(posts: list[dict], site: dict, dry: bool) -> list[str]:
    """Draw any missing or stale cards. Returns the files that changed."""
    changed = []
    manifest_path = OUT / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    for post in posts:
        fp = fingerprint(post)
        path = OUT / f"{post['slug']}.png"
        if manifest.get(post["slug"]) == fp and path.exists():
            continue
        changed.append(str(path.relative_to(ROOT)))
        if not dry:
            OUT.mkdir(parents=True, exist_ok=True)
            card(post, site).save(path, optimize=True)
            manifest[post["slug"]] = fp
    if changed and not dry:
        manifest_path.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n")
        changed.append(str(manifest_path.relative_to(ROOT)))
    return changed
