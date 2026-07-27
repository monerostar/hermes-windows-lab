#!/usr/bin/env python3
"""Inject pure CSS/SVG animations into hermes-stack-map.html"""
from pathlib import Path
import re

path = Path(r"C:/Users/Admin/src/hermes-windows-lab/docs/hermes-stack-map.html")
html = path.read_text(encoding="utf-8")

new_css = r"""
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'JetBrains Mono', monospace;
      background: #020617;
      min-height: 100vh;
      padding: 1.5rem 2rem 2.5rem;
      color: white;
    }
    .container { max-width: 1280px; margin: 0 auto; }
    .header { margin-bottom: 1.25rem; animation: fadeDown 0.7s ease both; }
    .header-row { display: flex; align-items: center; gap: 0.85rem; margin-bottom: 0.4rem; }
    .pulse-dot {
      width: 12px; height: 12px; background: #22d3ee; border-radius: 50%;
      animation: pulse 2s infinite; box-shadow: 0 0 12px rgba(34,211,238,0.5);
    }
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.45} }
    @keyframes fadeDown {
      from { opacity: 0; transform: translateY(-10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(14px); }
      to { opacity: 1; transform: translateY(0); }
    }
    @keyframes softIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
    h1 { font-size: 1.45rem; font-weight: 700; letter-spacing: -0.02em; }
    .subtitle { color: #94a3b8; font-size: 0.82rem; margin-left: 1.75rem; line-height: 1.45; max-width: 56rem; }
    .toolbar {
      display: flex; flex-wrap: wrap; gap: 0.6rem; align-items: center;
      margin: 0.85rem 0 0 1.75rem;
    }
    .toolbar label {
      display: inline-flex; align-items: center; gap: 0.4rem;
      font-size: 0.72rem; color: #94a3b8; cursor: pointer;
      user-select: none; border: 1px solid #1e293b; border-radius: 999px;
      padding: 0.28rem 0.7rem; background: rgba(15,23,42,0.6);
    }
    .toolbar input { accent-color: #22d3ee; }
    .diagram-container {
      background: rgba(15, 23, 42, 0.55);
      border-radius: 1rem;
      border: 1px solid #1e293b;
      padding: 1.1rem 1rem 0.75rem;
      overflow-x: auto;
      animation: fadeUp 0.85s ease 0.15s both;
      position: relative;
    }
    .diagram-container::after {
      content: "";
      pointer-events: none;
      position: absolute; inset: 0; border-radius: 1rem;
      background: radial-gradient(800px 200px at 20% 0%, rgba(34,211,238,0.06), transparent 60%),
                  radial-gradient(600px 220px at 80% 10%, rgba(167,139,250,0.05), transparent 55%);
      animation: ambient 8s ease-in-out infinite alternate;
    }
    @keyframes ambient {
      from { opacity: 0.55; }
      to { opacity: 1; }
    }
    svg { width: 100%; min-width: 1080px; display: block; position: relative; z-index: 1; }

    .flow {
      stroke-dasharray: 5 9;
      animation: flowDash 1.35s linear infinite;
    }
    .flow-slow {
      stroke-dasharray: 6 10;
      animation: flowDash 2.4s linear infinite;
    }
    .flow-reverse {
      stroke-dasharray: 5 9;
      animation: flowDashRev 1.8s linear infinite;
    }
    @keyframes flowDash {
      to { stroke-dashoffset: -42; }
    }
    @keyframes flowDashRev {
      to { stroke-dashoffset: 42; }
    }

    .node {
      transform-box: fill-box;
      transform-origin: center;
      transition: filter 0.35s ease, opacity 0.35s ease;
    }
    .node-glow-cyan { animation: glowCyan 3.2s ease-in-out infinite; }
    .node-glow-emerald { animation: glowEmerald 3.6s ease-in-out infinite; }
    .node-glow-violet { animation: glowViolet 3.4s ease-in-out infinite; }
    .node-glow-amber { animation: glowAmber 3.8s ease-in-out infinite; }
    .node-glow-orange { animation: glowOrange 3.1s ease-in-out infinite; }
    .node-glow-rose { animation: glowRose 3.5s ease-in-out infinite; }
    .node-glow-tech {
      animation: glowCyan 2.8s ease-in-out infinite, breathe 4.5s ease-in-out infinite;
    }
    .node-glow-main {
      animation: glowEmerald 2.8s ease-in-out infinite, breathe 5s ease-in-out infinite;
    }
    .node-glow-balanced {
      animation: glowViolet 2.4s ease-in-out infinite, breathe 3.8s ease-in-out infinite;
    }
    @keyframes breathe {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.015); }
    }
    @keyframes glowCyan {
      0%,100% { filter: drop-shadow(0 0 0 rgba(34,211,238,0)); }
      50% { filter: drop-shadow(0 0 6px rgba(34,211,238,0.55)); }
    }
    @keyframes glowEmerald {
      0%,100% { filter: drop-shadow(0 0 0 rgba(52,211,153,0)); }
      50% { filter: drop-shadow(0 0 6px rgba(52,211,153,0.5)); }
    }
    @keyframes glowViolet {
      0%,100% { filter: drop-shadow(0 0 0 rgba(167,139,250,0)); }
      50% { filter: drop-shadow(0 0 7px rgba(167,139,250,0.55)); }
    }
    @keyframes glowAmber {
      0%,100% { filter: drop-shadow(0 0 0 rgba(251,191,36,0)); }
      50% { filter: drop-shadow(0 0 6px rgba(251,191,36,0.45)); }
    }
    @keyframes glowOrange {
      0%,100% { filter: drop-shadow(0 0 0 rgba(251,146,60,0)); }
      50% { filter: drop-shadow(0 0 6px rgba(251,146,60,0.5)); }
    }
    @keyframes glowRose {
      0%,100% { filter: drop-shadow(0 0 0 rgba(251,113,133,0)); }
      50% { filter: drop-shadow(0 0 6px rgba(251,113,133,0.45)); }
    }

    .host-boundary {
      animation: boundaryPulse 6s ease-in-out infinite;
    }
    @keyframes boundaryPulse {
      0%,100% { stroke-opacity: 0.55; }
      50% { stroke-opacity: 1; }
    }

    .scanline {
      pointer-events: none;
      animation: scan 7s linear infinite;
    }
    @keyframes scan {
      0% { transform: translateY(-40px); opacity: 0; }
      8% { opacity: 0.35; }
      92% { opacity: 0.2; }
      100% { transform: translateY(920px); opacity: 0; }
    }

    .live-ping {
      animation: livePing 2.2s ease-out infinite;
      transform-origin: center;
      transform-box: fill-box;
    }
    @keyframes livePing {
      0% { opacity: 0.7; transform: scale(0.85); }
      70% { opacity: 0; transform: scale(1.8); }
      100% { opacity: 0; transform: scale(1.8); }
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 0.85rem;
      margin-top: 1.35rem;
    }
    .card {
      background: rgba(15, 23, 42, 0.55);
      border-radius: 0.75rem;
      border: 1px solid #1e293b;
      padding: 1.05rem 1.1rem;
      animation: fadeUp 0.7s ease both;
      transition: border-color 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
    }
    .card:nth-child(1) { animation-delay: 0.35s; }
    .card:nth-child(2) { animation-delay: 0.42s; }
    .card:nth-child(3) { animation-delay: 0.49s; }
    .card:nth-child(4) { animation-delay: 0.56s; }
    .card:nth-child(5) { animation-delay: 0.63s; }
    .card:nth-child(6) { animation-delay: 0.7s; }
    .card:hover {
      border-color: #334155;
      transform: translateY(-2px);
      box-shadow: 0 10px 28px rgba(0,0,0,0.28);
    }
    .card-header { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.65rem; }
    .card-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; animation: pulse 2.4s infinite; }
    .card-dot.cyan { background: #22d3ee; }
    .card-dot.emerald { background: #34d399; }
    .card-dot.violet { background: #a78bfa; }
    .card-dot.amber { background: #fbbf24; }
    .card-dot.rose { background: #fb7185; }
    .card-dot.orange { background: #fb923c; }
    .card-dot.slate { background: #94a3b8; }
    .card h3 { font-size: 0.82rem; font-weight: 600; }
    .card ul { list-style: none; color: #94a3b8; font-size: 0.72rem; line-height: 1.45; }
    .card li { margin-bottom: 0.28rem; }
    .footer { text-align: center; margin-top: 1.25rem; color: #475569; font-size: 0.72rem; animation: softIn 1s ease 0.8s both; }
    .note {
      margin-top: 1rem; color: #64748b; font-size: 0.72rem; line-height: 1.5;
      border-left: 2px solid #1e293b; padding-left: 0.85rem;
      animation: softIn 1s ease 0.75s both;
    }

    body:has(#pause-motion:checked) .flow,
    body:has(#pause-motion:checked) .flow-slow,
    body:has(#pause-motion:checked) .flow-reverse,
    body:has(#pause-motion:checked) .node-glow-cyan,
    body:has(#pause-motion:checked) .node-glow-emerald,
    body:has(#pause-motion:checked) .node-glow-violet,
    body:has(#pause-motion:checked) .node-glow-amber,
    body:has(#pause-motion:checked) .node-glow-orange,
    body:has(#pause-motion:checked) .node-glow-rose,
    body:has(#pause-motion:checked) .node-glow-tech,
    body:has(#pause-motion:checked) .node-glow-main,
    body:has(#pause-motion:checked) .node-glow-balanced,
    body:has(#pause-motion:checked) .host-boundary,
    body:has(#pause-motion:checked) .scanline,
    body:has(#pause-motion:checked) .live-ping,
    body:has(#pause-motion:checked) .pulse-dot,
    body:has(#pause-motion:checked) .card-dot,
    body:has(#pause-motion:checked) .diagram-container::after {
      animation-play-state: paused !important;
    }
    body:has(#pause-motion:checked) .scanline { opacity: 0; }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
      .scanline { display: none; }
      .flow, .flow-slow, .flow-reverse { stroke-dasharray: none; }
    }
"""

html2 = re.sub(r"<style>.*?</style>", "<style>\n" + new_css + "\n  </style>", html, count=1, flags=re.S)

toolbar = """
      <div class="toolbar">
        <label><input type="checkbox" id="pause-motion"> Pause motion</label>
        <span style="font-size:0.7rem;color:#475569">Pure CSS/SVG · respects prefers-reduced-motion</span>
      </div>
"""
if "pause-motion" not in html2:
    html2 = html2.replace(
        "Snapshot inventory: 2026-07-25. Default agent: Grok 4.5 (xai-oauth).\n      </p>",
        "Snapshot inventory: 2026-07-25. Default agent: Grok 4.5 (xai-oauth).\n        Animated edition.\n      </p>"
        + toolbar,
        1,
    )


def classify_edge(tag: str) -> str:
    if "class=" in tag:
        return tag
    stroke_m = re.search(r'stroke="([^"]+)"', tag)
    color = stroke_m.group(1) if stroke_m else ""
    is_dashed = "stroke-dasharray" in tag
    cls = "flow"
    if color == "#94a3b8":
        cls = "flow-slow"
    if color == "#fb7185" and is_dashed:
        cls = "flow-reverse"
    if color == "#fbbf24" and is_dashed:
        cls = "flow-slow"
    return re.sub(r"<(line|path)\b", rf'<\1 class="{cls}"', tag, count=1)


parts = html2.split("<!-- ========== HOST BOUNDARY ========== -->", 1)
if len(parts) == 2:
    edges, rest = parts

    def edge_sub(m):
        t = m.group(0)
        if "marker-end" in t or (t.startswith("<path") and 'stroke=' in t and 'fill="none"' in t):
            return classify_edge(t)
        return t

    edges2 = re.sub(r"<(line|path)\b[^>]*/?>", edge_sub, edges)
    html2 = edges2 + "<!-- ========== HOST BOUNDARY ========== -->" + rest

html2 = html2.replace(
    '<rect x="24" y="24" width="1132" height="872" rx="14" fill="rgba(251,191,36,0.03)" stroke="#fbbf24" stroke-width="1" stroke-dasharray="10,5"/>',
    '<rect class="host-boundary" x="24" y="24" width="1132" height="872" rx="14" fill="rgba(251,191,36,0.03)" stroke="#fbbf24" stroke-width="1" stroke-dasharray="10,5"/>',
    1,
)

if "id=\"scanGrad\"" not in html2:
    html2 = html2.replace(
        "</defs>",
        """  <linearGradient id="scanGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/>
            <stop offset="50%" stop-color="#22d3ee" stop-opacity="0.35"/>
            <stop offset="100%" stop-color="#a78bfa" stop-opacity="0"/>
          </linearGradient>
        </defs>""",
        1,
    )

if "class=\"scanline\"" not in html2:
    html2 = html2.replace(
        '<rect width="100%" height="100%" fill="url(#grid)"/>',
        '''<rect width="100%" height="100%" fill="url(#grid)"/>
        <rect class="scanline" x="24" y="0" width="1132" height="28" fill="url(#scanGrad)" opacity="0.25"/>''',
        1,
    )

replacements = [
    (
        '<rect x="40" y="78" width="78" height="44" rx="6" fill="rgba(30,41,59,0.55)" stroke="#94a3b8" stroke-width="1.5"/>',
        '<rect class="node node-glow-cyan" x="40" y="78" width="78" height="44" rx="6" fill="rgba(30,41,59,0.55)" stroke="#94a3b8" stroke-width="1.5"/>',
    ),
    (
        '<rect x="214" y="68" width="92" height="48" rx="6" fill="rgba(8,51,68,0.45)" stroke="#22d3ee" stroke-width="1.5"/>',
        '<rect class="node node-glow-tech" x="214" y="68" width="92" height="48" rx="6" fill="rgba(8,51,68,0.45)" stroke="#22d3ee" stroke-width="1.5"/>',
    ),
    (
        '<rect x="214" y="126" width="192" height="32" rx="6" fill="rgba(6,78,59,0.4)" stroke="#34d399" stroke-width="1.5"/>',
        '<rect class="node node-glow-main" x="214" y="126" width="192" height="32" rx="6" fill="rgba(6,78,59,0.4)" stroke="#34d399" stroke-width="1.5"/>',
    ),
    (
        '<rect x="836" y="70" width="90" height="42" rx="6" fill="rgba(136,19,55,0.35)" stroke="#fb7185" stroke-width="1.5"/>',
        '<rect class="node node-glow-rose" x="836" y="70" width="90" height="42" rx="6" fill="rgba(136,19,55,0.35)" stroke="#fb7185" stroke-width="1.5"/>',
    ),
    (
        '<rect x="936" y="70" width="90" height="42" rx="6" fill="rgba(120,53,15,0.35)" stroke="#fbbf24" stroke-width="1.5"/>',
        '<rect class="node node-glow-amber" x="936" y="70" width="90" height="42" rx="6" fill="rgba(120,53,15,0.35)" stroke="#fbbf24" stroke-width="1.5"/>',
    ),
    (
        '<rect x="54" y="242" width="138" height="98" rx="6" fill="rgba(6,78,59,0.45)" stroke="#34d399" stroke-width="1.8"/>',
        '<rect class="node node-glow-main" x="54" y="242" width="138" height="98" rx="6" fill="rgba(6,78,59,0.45)" stroke="#34d399" stroke-width="1.8"/>',
    ),
    (
        '<rect x="206" y="242" width="138" height="98" rx="6" fill="rgba(8,51,68,0.5)" stroke="#22d3ee" stroke-width="1.8"/>',
        '<rect class="node node-glow-tech" x="206" y="242" width="138" height="98" rx="6" fill="rgba(8,51,68,0.5)" stroke="#22d3ee" stroke-width="1.8"/>',
    ),
    (
        '<rect x="358" y="242" width="128" height="98" rx="6" fill="rgba(6,78,59,0.32)" stroke="#34d399" stroke-width="1.5"/>',
        '<rect class="node node-glow-emerald" x="358" y="242" width="128" height="98" rx="6" fill="rgba(6,78,59,0.32)" stroke="#34d399" stroke-width="1.5"/>',
    ),
    (
        '<rect x="500" y="242" width="128" height="98" rx="6" fill="rgba(76,29,149,0.32)" stroke="#a78bfa" stroke-width="1.5"/>',
        '<rect class="node node-glow-violet" x="500" y="242" width="128" height="98" rx="6" fill="rgba(76,29,149,0.32)" stroke="#a78bfa" stroke-width="1.5"/>',
    ),
    (
        '<rect x="642" y="242" width="140" height="98" rx="6" fill="rgba(30,41,59,0.5)" stroke="#94a3b8" stroke-width="1.5"/>',
        '<rect class="node node-glow-cyan" x="642" y="242" width="140" height="98" rx="6" fill="rgba(30,41,59,0.5)" stroke="#94a3b8" stroke-width="1.5"/>',
    ),
    (
        '<rect x="918" y="244" width="78" height="36" rx="5" fill="rgba(76,29,149,0.4)" stroke="#c4b5fd" stroke-width="1.6"/>',
        '<rect class="node node-glow-balanced" x="918" y="244" width="78" height="36" rx="5" fill="rgba(76,29,149,0.4)" stroke="#c4b5fd" stroke-width="1.6"/>',
    ),
    (
        '<rect x="834" y="410" width="140" height="52" rx="6" fill="rgba(251,146,60,0.28)" stroke="#fb923c" stroke-width="1.5"/>',
        '<rect class="node node-glow-orange" x="834" y="410" width="140" height="52" rx="6" fill="rgba(251,146,60,0.28)" stroke="#fb923c" stroke-width="1.5"/>',
    ),
    (
        '<rect x="986" y="410" width="138" height="52" rx="6" fill="rgba(251,146,60,0.22)" stroke="#fb923c" stroke-width="1.4"/>',
        '<rect class="node node-glow-orange" x="986" y="410" width="138" height="52" rx="6" fill="rgba(251,146,60,0.22)" stroke="#fb923c" stroke-width="1.4"/>',
    ),
    (
        '<rect x="986" y="580" width="138" height="52" rx="6" fill="rgba(136,19,55,0.28)" stroke="#fb7185" stroke-width="1.4"/>',
        '<rect class="node node-glow-rose" x="986" y="580" width="138" height="52" rx="6" fill="rgba(136,19,55,0.28)" stroke="#fb7185" stroke-width="1.4"/>',
    ),
    (
        '<rect x="834" y="580" width="140" height="52" rx="6" fill="rgba(136,19,55,0.32)" stroke="#fb7185" stroke-width="1.5"/>',
        '<rect class="node node-glow-rose" x="834" y="580" width="140" height="52" rx="6" fill="rgba(136,19,55,0.32)" stroke="#fb7185" stroke-width="1.5"/>',
    ),
    (
        '<rect x="54" y="408" width="292" height="104" rx="6" fill="rgba(251,146,60,0.18)" stroke="#fb923c" stroke-width="1.4"/>',
        '<rect class="node node-glow-orange" x="54" y="408" width="292" height="104" rx="6" fill="rgba(251,146,60,0.18)" stroke="#fb923c" stroke-width="1.4"/>',
    ),
]

miss = 0
for a, b in replacements:
    if a not in html2:
        print("MISS:", a[:90])
        miss += 1
    else:
        html2 = html2.replace(a, b, 1)

ping = """
        <!-- live pings -->
        <circle class="live-ping" cx="275" cy="255" r="5" fill="#22d3ee" opacity="0.5"/>
        <circle class="live-ping" cx="123" cy="255" r="5" fill="#34d399" opacity="0.5" style="animation-delay:0.7s"/>
        <circle class="live-ping" cx="904" cy="422" r="5" fill="#fb923c" opacity="0.5" style="animation-delay:1.1s"/>
        <circle class="live-ping" cx="957" cy="255" r="4" fill="#a78bfa" opacity="0.5" style="animation-delay:0.4s"/>
"""
if html2.count("live-ping") < 3:
    html2 = html2.replace(
        "<!-- ========== LEGEND ========== -->",
        ping + "\n        <!-- ========== LEGEND ========== -->",
        1,
    )

html2 = html2.replace(
    "<title>Hermes Stack Map — monerostar</title>",
    "<title>Hermes Stack Map (animated) — monerostar</title>",
    1,
)
html2 = html2.replace(
    "Hermes Stack Map · Option C · 2026-07-25 · monerostar · self-contained HTML (JetBrains Mono)",
    "Hermes Stack Map · Option C · animated · 2026-07-25 · monerostar · pure CSS/SVG",
    1,
)

path.write_text(html2, encoding="utf-8", newline="\n")
print("OK", path.stat().st_size)
print("miss", miss)
print("flow", len(re.findall(r'class="flow"', html2)))
print("flow-slow", html2.count("flow-slow"))
print("node-glow", html2.count("node-glow"))
print("live-ping", html2.count("live-ping"))
print("pause", "pause-motion" in html2)
print("scanline", "scanline" in html2)
