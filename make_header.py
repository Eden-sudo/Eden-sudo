"""Genera assets/header.svg: encabezado animado (solo CSS, sin JavaScript ni servicios externos).
Uso: python3 make_header.py"""
import random

W, H = 980, 210
rng = random.Random(1)
COLS, ROWS, CELL, GAP = 16, 8, 14, 4
GX, GY = W - 40 - COLS * (CELL + GAP) + GAP, (H - ROWS * (CELL + GAP) + GAP) // 2

cells = []
for r in range(ROWS):
    for c in range(COLS):
        on = rng.random() < 0.5
        dur = rng.choice([2.4, 3.2, 4.0, 5.6])
        delay = rng.uniform(0, 4)
        cls = "b1" if on else "b0"
        cells.append(f'<rect class="bit {cls}" x="{GX + c * (CELL + GAP)}" y="{GY + r * (CELL + GAP)}" '
                     f'width="{CELL}" height="{CELL}" rx="3" style="animation-duration:{dur}s;animation-delay:-{delay:.2f}s"/>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Carlos Duarte, embedded ML engineer">
<style>
  .bg {{ fill: #f8fafc; stroke: #d0d7de; }}
  .name {{ fill: #0f172a; font: 700 40px 'Segoe UI', Helvetica, Arial, sans-serif; }}
  .role {{ fill: #0f766e; font: 600 18px 'Segoe UI', Helvetica, Arial, sans-serif; }}
  .code {{ fill: #475569; font: 15px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
  .b0 {{ fill: #cbd5e1; }} .b1 {{ fill: #14b8a6; }}
  .bit {{ animation-name: flip; animation-iteration-count: infinite; animation-timing-function: steps(1); }}
  @keyframes flip {{ 0% {{ opacity: 1; }} 50% {{ opacity: .18; }} }}
  .cursor {{ fill: #14b8a6; animation: blink 1.1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  @media (prefers-color-scheme: dark) {{
    .bg {{ fill: #0d1117; stroke: #30363d; }}
    .name {{ fill: #e6edf3; }} .role {{ fill: #2dd4bf; }} .code {{ fill: #8b949e; }}
    .b0 {{ fill: #21262d; }}
  }}
  @media (prefers-reduced-motion: reduce) {{ .bit, .cursor {{ animation: none; }} }}
</style>
<rect class="bg" x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14"/>
<text class="name" x="40" y="86">Carlos Duarte</text>
<text class="role" x="42" y="120">Embedded systems · Aspiring research engineer</text>
<text class="code" x="42" y="160">bit = popcount(~(w ^ x)) &gt;= T; <tspan class="cursor">▌</tspan></text>
{chr(10).join(cells)}
</svg>
'''
open("assets/header.svg", "w").write(svg)
print("assets/header.svg", len(svg), "bytes")
