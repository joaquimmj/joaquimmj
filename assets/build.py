"""Builds the SVGs of the profile README (dark and light), so every card shares one design.

    python3 assets/build.py

No dependencies. Fonts fall back to what the viewer has: SVGs shown through <img> can't load web fonts.
"""

from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent
SANS = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
SERIF = "Newsreader, 'Iowan Old Style', Georgia, 'Times New Roman', serif"
MONO = "'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace"

THEMES = {
    "dark": dict(bg="#0d1117", panel="#11161d", line="#262c36", grid="#1b212a", ink="#e6edf3", muted="#8b949e",
                 faint="#6e7681", accent="#3fb27f", accent_soft="#173a2c", red="#f0816b"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", line="#d0d7de", grid="#eaeef2", ink="#1f2328", muted="#59636e",
                  faint="#8c959f", accent="#1a7f52", accent_soft="#dcf3e7", red="#cf4b33"),
}


def svg(w, h, body, style=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img"><style>{style}</style>{body}</svg>\n')


def header(t):
    w, h = 1200, 330
    cols = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="{t["grid"]}"/>' for x in range(60, w - 60, 120))
    rows = "".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{t["grid"]}"/>' for y in range(30, h, 30))
    letters = "".join(
        f'<text x="{x + 60}" y="21" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{t["faint"]}">{c}</text>'
        for x, c in zip(range(60, w, 120), "ABCDEFGHIJ"))
    style = f"""
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    .rise {{ animation: rise .9s ease-out both; }}
    .d1 {{ animation-delay: .15s; }} .d2 {{ animation-delay: .45s; }} .d3 {{ animation-delay: .75s; }}
    @keyframes rise {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: none; }} }}
    """
    body = f"""
  <rect width="{w}" height="{h}" rx="14" fill="{t["bg"]}"/>
  <g opacity=".9">{cols}{rows}</g>
  <rect x="0" y="0" width="{w}" height="30" fill="{t["panel"]}"/>{letters}
  <line x1="0" y1="30" x2="{w}" y2="30" stroke="{t["line"]}"/>
  <!-- formula bar -->
  <g class="rise d1">
    <rect x="60" y="58" width="560" height="34" rx="6" fill="{t["panel"]}" stroke="{t["line"]}"/>
    <text x="78" y="80" font-family="{MONO}" font-size="13" fill="{t["faint"]}">B2</text>
    <line x1="108" y1="64" x2="108" y2="86" stroke="{t["line"]}"/>
    <text x="122" y="80" font-family="{SERIF}" font-style="italic" font-size="14" fill="{t["faint"]}">fx</text>
    <text x="148" y="80" font-family="{MONO}" font-size="13.5" fill="{t["ink"]}">=BUILD(<tspan fill="{t["accent"]}">"AI tools"</tspan>, <tspan fill="{t["accent"]}">"finance"</tspan>)</text>
    <rect class="cursor" x="387" y="69" width="2" height="15" fill="{t["accent"]}"/>
  </g>
  <!-- selected cell -->
  <g class="rise d2">
    <rect x="60" y="118" width="720" height="92" fill="{t["bg"]}" stroke="{t["accent"]}" stroke-width="2"/>
    <rect x="775" y="205" width="9" height="9" fill="{t["accent"]}" stroke="{t["bg"]}" stroke-width="2"/>
    <text x="84" y="183" font-family="{SERIF}" font-size="58" fill="{t["ink"]}">Joaquim Manji-Jung</text>
  </g>
  <g class="rise d3">
    <text x="62" y="252" font-family="{SANS}" font-size="19" fill="{t["muted"]}">I build AI tools for finance, and study how LLM agents get numbers wrong.</text>
    <text x="62" y="288" font-family="{MONO}" font-size="13" fill="{t["faint"]}">Paris · Economics + CS @ Paris 1 Panthéon-Sorbonne · Founder @ Aptence</text>
  </g>
  <!-- right column: three key figures -->
  <g class="rise d3" font-family="{MONO}">
    {figure(t, 860, 128, "3.5% → 0", "figures wrong: web search vs sourced data")}
    {figure(t, 860, 188, "5K", "users on QuantAcademy, built solo")}
    {figure(t, 860, 248, "18M+", "organic views, $0 in ads")}
  </g>
"""
    return svg(w, h, body, style)


def figure(t, x, y, big, small):
    return (f'<text x="{x}" y="{y + 22}" font-size="22" font-weight="600" fill="{t["ink"]}">{escape(big)}</text>'
            f'<text x="{x}" y="{y + 42}" font-family="{SANS}" font-size="12.5" fill="{t["muted"]}">{escape(small)}</text>')


def section(t, label, ref):
    w, h = 1200, 44
    body = f"""
  <rect x="0" y="16" width="10" height="10" fill="{t["accent"]}"/>
  <text x="22" y="29" font-family="{SANS}" font-size="15" font-weight="600" letter-spacing="2.2" fill="{t["ink"]}">{escape(label.upper())}</text>
  <line x1="{22 + len(label) * 13 + 22}" y1="24" x2="{w}" y2="24" stroke="{t["line"]}"/>
"""
    return svg(w, h, body)


def wrap(text, n):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        if len(cur) + len(wd) + 1 > n:
            lines.append(cur)
            cur = wd
        else:
            cur = f"{cur} {wd}".strip()
    return lines + [cur]


def card(t, kicker, title, text, tags, stat=None, w=590, h=190):
    lines = wrap(text, 62)
    desc = "".join(f'<text x="28" y="{98 + i * 21}" font-family="{SANS}" font-size="14.5" fill="{t["muted"]}">{escape(l)}</text>'
                   for i, l in enumerate(lines[:3]))
    x, chips = 28, ""
    for tag in tags:
        tw = 7.6 * len(tag) + 20
        chips += (f'<rect x="{x}" y="{h - 44}" width="{tw}" height="22" rx="11" fill="{t["accent_soft"]}"/>'
                  f'<text x="{x + tw / 2}" y="{h - 29}" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{t["accent"]}">{escape(tag)}</text>')
        x += tw + 8
    stat_svg = ""
    if stat:
        stat_svg = (f'<text x="{w - 28}" y="40" text-anchor="end" font-family="{MONO}" font-size="12" fill="{t["muted"]}">{escape(stat)}</text>')
    body = f"""
  <rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="12" fill="{t["panel"]}" stroke="{t["line"]}"/>
  <text x="28" y="40" font-family="{MONO}" font-size="11.5" letter-spacing="1.2" fill="{t["accent"]}">{escape(kicker.upper())}</text>
  {stat_svg}
  <text x="28" y="72" font-family="{SANS}" font-size="22" font-weight="650" fill="{t["ink"]}">{escape(title)}</text>
  {desc}
  {chips}
"""
    return svg(w, h, body)


def research(t):
    w, h = 1200, 250
    bars = [("Web search only", 3.5), ("Sourced data", 0.0), ("Sourced data + review", 0.0)]
    chart = ""
    for i, (label, v) in enumerate(bars):
        y = 92 + i * 44
        bw = 0 if v == 0 else v / 3.5 * 300
        color = t["red"] if v else t["accent"]
        chart += (f'<text x="760" y="{y + 15}" text-anchor="end" font-family="{SANS}" font-size="13" fill="{t["muted"]}">{label}</text>'
                  f'<rect x="776" y="{y}" width="{max(bw, 3)}" height="22" rx="3" fill="{color}"/>'
                  f'<text x="{776 + max(bw, 3) + 10}" y="{y + 16}" font-family="{MONO}" font-size="13" fill="{t["ink"]}">{v:.1f}%</text>')
    body = f"""
  <rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="12" fill="{t["panel"]}" stroke="{t["line"]}"/>
  <text x="32" y="44" font-family="{MONO}" font-size="11.5" letter-spacing="1.2" fill="{t["accent"]}">PAPER · NOVEMBER 2026</text>
  <text x="32" y="82" font-family="{SERIF}" font-size="30" fill="{t["ink"]}">Filling the Gaps</text>
  <text x="32" y="110" font-family="{SANS}" font-size="15.5" fill="{t["muted"]}">How often do LLM agents misreport figures when they build financial models?</text>
  <text x="32" y="148" font-family="{SANS}" font-size="14" fill="{t["muted"]}">300 runs · 50 US and European companies · every flagged figure checked by hand</text>
  <text x="32" y="172" font-family="{SANS}" font-size="14" fill="{t["muted"]}">Pre-registered robustness check · statistics in Python</text>
  <text x="32" y="214" font-family="{MONO}" font-size="13" fill="{t["accent"]}">Read the paper  →</text>
  <text x="776" y="64" font-family="{MONO}" font-size="11.5" fill="{t["faint"]}">WRONG FILED FIGURES</text>
  {chart}
  <text x="776" y="226" font-family="{SANS}" font-size="12" fill="{t["faint"]}">36 of 1,018 with web search · 0 of 3,230 with sourced data</text>
"""
    return svg(w, h, body)


CARDS = {
    "deskstack": ("Open source", "deskstack", "Your AI deal team inside Claude. Models built, tied out to the filings, reviewed. Free data, US + Europe.", ["MCP", "SEC", "ESEF"], None),
    "freeterminal": ("Open source", "freeterminal", "Free, citable US and European financial data for Claude. Paste one URL, no API key.", ["MCP", "Cloudflare"], None),
    "cellrush": ("Open source", "cellrush", "Monkeytype for spreadsheets: Excel shortcuts against the clock, keyboard only, on a spreadsheet engine built from scratch.", ["React", "Game"], None),

    "traceroot": ("Contributor", "TraceRoot", "Open-source observability and self-healing layer for AI agents. I found and fixed LLM cost-tracking bugs.", ["YC S25", "LLM costs"], "★ 1.4k"),
    "aptence": ("Building", "Aptence", "Financial modeling assessments for banks and PE funds, in a browser spreadsheet, graded automatically.", ["aptence.app"], None),
    "quantacademy": ("Built solo", "QuantAcademy", "Finance interview prep in 9 languages: 5K users, first paying customers, 18M+ organic views.", ["quantacademy.app"], None),
}

if __name__ == "__main__":
    for name, t in THEMES.items():
        (OUT / f"header-{name}.svg").write_text(header(t))
        (OUT / f"research-{name}.svg").write_text(research(t))
        for key, label, ref in (("research", "Research", "B5"), ("open-source", "Open source", "B6"), ("building", "Building", "B7")):
            (OUT / f"section-{key}-{name}.svg").write_text(section(t, label, ref))
        for key, args in CARDS.items():
            (OUT / f"card-{key}-{name}.svg").write_text(card(t, *args))
    print("built", len(list(OUT.glob("*.svg"))), "svgs")
