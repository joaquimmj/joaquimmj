"""Builds dark_mode.svg and light_mode.svg: ASCII portrait on the left, neofetch-style card on the right.

Usage: python generate.py photo.jpg
"""
import sys
from html import escape

from PIL import Image, ImageOps

USER = "joaquim@manjijung"
WIDTH = 51  # width of the info column, in characters

# (key, value); an empty key = blank line, a key starting with "—" = section title
INFO = [
    ("OS", "macOS"),
    ("Location", "Paris, France"),
    ("Role", "Founder"),
    ("Host", "Aptence, QuantAcademy"),
    ("", ""),
    ("Languages.Programming", "TypeScript, Python, C++"),
    ("Languages.Web", "JavaScript, HTML, CSS"),
    ("Languages.Data", "SQL, PL/pgSQL, Shell"),
    ("Languages.Real", "French, English, German"),
    ("", ""),
    ("— Projects", ""),
    ("Aptence", "aptence.app"),
    ("QuantAcademy", "quantacademy.app"),
    ("", ""),
    ("— Contact", ""),
    ("LinkedIn", "joaquim-manji-jung"),
    ("TikTok", "@quant_academy"),
    ("Website", "aptence.app"),
]

ASCII_COLS, ASCII_ROWS = 38, 20  # a cell is ~10.5 × 20 px, so 38 × 20 keeps the image square
RAMP = " .'`^\",:;Il!i><~+_-?][}{1)(|tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

THEMES = {
    "dark": dict(bg="#161b22", fg="#c9d1d9", key="#ffa657", value="#a5d6ff", dots="#616e7f"),
    "light": dict(bg="#f6f8fa", fg="#24292f", key="#953800", value="#0a3069", dots="#c2cfde"),
}


def to_ascii(path):
    img = ImageOps.exif_transpose(Image.open(path)).convert("L")
    box = img.point(lambda v: 255 if v > 40 else 0).getbbox()
    if box:
        m = 12
        img = img.crop((max(box[0] - m, 0), max(box[1] - m, 0), min(box[2] + m, img.width), min(box[3] + m, img.height)))  # crop to the subject on a dark background
    img = ImageOps.autocontrast(img.resize((ASCII_COLS, ASCII_ROWS)))
    px = img.load()
    char = lambda v: " " if v < 40 else RAMP[v * (len(RAMP) - 1) // 255]  # dark background = blank
    return ["".join(char(px[x, y]) for x in range(ASCII_COLS)) for y in range(ASCII_ROWS)]



def info_lines(t, info):
    head = f"{USER} " + "—" * (WIDTH - len(USER) - 1)
    out = [f'<tspan fill="{t["fg"]}">{escape(head)}</tspan>']
    for key, value in info:
        if not key:
            out.append(f'<tspan fill="{t["fg"]}">.</tspan>')
        elif key.startswith("—"):
            title = key + " " + "—" * (WIDTH - len(key) - 1)
            out.append(f'<tspan fill="{t["fg"]}">{escape(title)}</tspan>')
        else:
            dots = " " + "." * max(2, WIDTH - len(key) - len(value) - 6) + " "
            out.append(
                f'<tspan fill="{t["fg"]}">. </tspan><tspan fill="{t["key"]}">{escape(key)}</tspan>'
                f'<tspan fill="{t["fg"]}">:</tspan><tspan fill="{t["dots"]}">{dots}</tspan>'
                f'<tspan fill="{t["value"]}">{escape(value)}</tspan>'
            )
    return out


def svg(art, info, t):
    lh, x0, x1, y0 = 20, 15, 435, 30
    lines = info_lines(t, info)
    top = y0 + max(0, len(lines) - len(art)) * lh // 2  # centre the portrait next to the card
    rows = [f'<tspan x="{x0}" y="{top + i * lh}">{escape(r)}</tspan>' for i, r in enumerate(art)]
    infos = [f'<tspan x="{x1}" y="{y0 + i * lh}">{l}</tspan>' for i, l in enumerate(lines)]
    h = y0 + max(len(art), len(lines)) * lh
    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="985px" height="{h}px" font-size="16px">
<style>
@font-face {{ src: local('Consolas'), local('Consolas Bold'); font-family: 'ConsolasFallback'; font-display: swap; -webkit-size-adjust: 109%; size-adjust: 109%; }}
text, tspan {{ white-space: pre; }}
</style>
<rect width="985px" height="{h}px" fill="{t["bg"]}" rx="15"/>
<text fill="{t["fg"]}">{"".join(rows)}</text>
<text>{"".join(infos)}</text>
</svg>
"""


if __name__ == "__main__":
    art = to_ascii(sys.argv[1])
    info = INFO
    for name, theme in THEMES.items():
        with open(f"{name}_mode.svg", "w") as f:
            f.write(svg(art, info, theme))
