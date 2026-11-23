"""Build ASO-Squares-Cubes-Tables.html: squares 10-30, cubes 1-30, tables 11-25.
Numbers only, no text. House fonts and colours; three soft tints tell the blocks apart.
On a desktop (>=1200 x 600) everything fits one screen, built for the user's 1920x1080:
  row 1: squares 7 x 3 (10-16, 17-23, 24-30) | cubes 10 x 3 (1-10, 11-20, 21-30)
  row 2: the 15 tables side by side, x1 to x10 down each card."""
import pathlib
here = pathlib.Path(__file__).resolve().parent.parent

css = """
:root{
  --bg:#fbfbfb; --paper:#fff; --fg:#111; --muted:#6e6e73;
  --f-serif:"EB Garamond","Iowan Old Style",Georgia,serif;
  --f-mono:"IBM Plex Mono",ui-monospace,"SF Mono",Menlo,monospace;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.4 var(--f-serif);
  font-variant-numeric:lining-nums tabular-nums;-webkit-font-smoothing:antialiased;overflow-x:hidden}

/* one tint per block: squares blue, cubes magenta, tables green */
.sq{--acc:#2b4cff}
.cu{--acc:#c2185b}
.tabs{--acc:#0b8a4f}
.sq,.cu,.tabs{--tint:color-mix(in srgb,var(--acc) 6%,#fff);--line:color-mix(in srgb,var(--acc) 16%,#fff);
  --hov:color-mix(in srgb,var(--acc) 14%,#fff);--hline:color-mix(in srgb,var(--acc) 45%,#fff)}

main{padding:16px}
.sq,.cu{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:6px;margin:0 0 20px}
.tabs{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:6px}

.cell{display:flex;justify-content:space-between;align-items:baseline;gap:8px;padding:8px 10px;
  background:var(--tint);border:1px solid var(--line);border-radius:2px;
  transition:background-color .15s,border-color .15s}
.k{font-family:var(--f-mono);font-size:12px;color:var(--muted);transition:color .15s}
.v{font-size:20px;font-weight:600}

.tb{background:var(--tint);border:1px solid var(--line);border-radius:2px;padding:3px 0;transition:border-color .15s}
.r{display:flex;justify-content:space-between;align-items:baseline;gap:6px;padding:3px 10px;
  border-bottom:1px dotted var(--line);transition:background-color .15s}
.r:last-child{border-bottom:0}
.r b{font-size:18px;font-weight:600}

/* hover: the box under the pointer deepens its own tint */
.cell:hover{background:var(--hov);border-color:var(--hline)}
.tb:hover{border-color:var(--hline)}
.r:hover{background:var(--hov)}
.cell:hover .k,.r:hover .k{color:var(--acc)}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}

/* one screen, no scroll, on a desktop monitor */
@media (min-width:1200px) and (min-height:600px){
  html,body{height:100%;overflow:hidden}
  main{height:100vh;padding:2vh 1.2vw;display:grid;
    grid-template-columns:minmax(0,7fr) minmax(0,10fr);grid-template-rows:minmax(0,3fr) minmax(0,10fr);gap:2vh 1.2vw}
  .sq,.cu{margin:0;grid-template-rows:repeat(3,minmax(0,1fr));gap:.7vh .4vw}
  .sq{grid-template-columns:repeat(7,minmax(0,1fr))}
  .cu{grid-template-columns:repeat(10,minmax(0,1fr))}
  .tabs{grid-column:1/3;grid-template-columns:repeat(15,minmax(0,1fr));gap:.4vw}
  .cell{flex-direction:column;align-items:stretch;justify-content:space-between;padding:.8vh .55vw;min-height:0}
  .cell .k{align-self:flex-start;font-size:1.4vh;line-height:1}
  .cell .v{align-self:flex-end;font-size:2.5vh;line-height:1}
  .tb{display:flex;flex-direction:column;padding:.4vh 0;min-height:0}
  .r{flex:1;align-items:center;padding:0 .5vw;min-height:0}
  .r .k{font-size:1.4vh;line-height:1}
  .r b{font-size:2.5vh;line-height:1}
}
"""

def cells(cls, rng, power, mark):
    return f'<div class="{cls}">' + "".join(
        f'<div class="cell"><span class="k">{n}{mark}</span><span class="v">{n**power:,}</span></div>'
        for n in rng) + "</div>"

squares = cells("sq", range(10, 31), 2, "²")
cubes = cells("cu", range(1, 31), 3, "³")
tabs = '<div class="tabs">' + "".join(
    '<div class="tb">' + "".join(
        f'<div class="r"><span class="k">{t} × {i}</span><b>{t*i}</b></div>' for i in range(1, 11)) + "</div>"
    for t in range(11, 26)) + "</div>"

html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Squares, Cubes and Tables</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@600&family=IBM+Plex+Mono:wght@400&display=swap">
<style>{css}</style></head>
<body>
<main>
{squares}
{cubes}
{tabs}
</main>
</body></html>
"""
(here / "ASO-Squares-Cubes-Tables.html").write_text(html)
print("written")
