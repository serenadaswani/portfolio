"""Badge review (v1.8 -> v1.9 proposal): Current | A Frosted | B Glass, on every surface a badge sits on.
A record for the decision, like review-v1.8.html. Run: python3 design-system/tools/previews/src/review_badges.py
"""
import os
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
tokens = open(os.path.join(REPO, 'design-system', 'css', 'tokens.css')).read()
comps = open(os.path.join(REPO, 'design-system', 'css', 'components.css')).read()

# Surfaces: the page, then each project wash at its strongest (bottom of the card), where a badge reads hardest.
SURFACES = [('Page', 'var(--color-bg-elevated)'),
            ('Mensio wash', 'color-mix(in srgb, #206CFD 16%, var(--color-bg-elevated))'),
            ('Procense wash', 'color-mix(in srgb, #1B2026 11%, var(--color-bg-elevated))'),
            ('Apple wash', 'color-mix(in srgb, #B6BAC6 45%, var(--color-bg-elevated))'),
            ('OmniSynkAI wash', 'color-mix(in srgb, #755CFB 16%, var(--color-bg-elevated))')]
VARIANTS = [('', 'Current', 'Outline: 1px silver ring, no fill.'),
            ('rv-frosted', 'A · Frosted', 'White at 55% + a light grey 1px ring (ink at 8%). No blur, so it stays within the system rules.'),
            ('rv-glass', 'B · Glass', 'White at 40% + a whiter 1px ring + 8px backdrop blur. Needs a rule change (the system bans blur and glass); falls back to solid with reduced transparency.')]

CSS = r"""
body { margin: 0; font-family: var(--font-sans); background: var(--color-bg-canvas); color: var(--color-text-primary); }
.rv { max-width: 1200px; margin: 0 auto; padding: var(--space-10) var(--space-4) var(--space-16); display: grid; gap: var(--space-8); }
.rv h1 { margin: 0; font-size: var(--type-h2); line-height: var(--line-h2); font-weight: var(--weight-medium); letter-spacing: var(--tracking-h2); }
.rv > p { margin: 0; max-width: 64ch; color: var(--color-text-secondary); }
.rv-bar { display: flex; gap: var(--space-2); align-items: center; }
.rv-grid { display: grid; gap: var(--space-4); grid-template-columns: minmax(0, 1fr); }
@media (min-width: 900px) { .rv-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
.rv-col { display: grid; gap: var(--space-2); align-content: start; }
.rv-col h2 { margin: 0; font-size: var(--type-body-md); line-height: var(--line-body-md); font-weight: var(--weight-medium); }
.rv-col > p { margin: 0 0 var(--space-2); min-height: 4.5em; font-size: var(--type-body-sm); line-height: var(--line-body-sm); color: var(--color-text-secondary); }
.rv-sw { display: grid; gap: var(--space-2); padding: var(--space-4); border-radius: var(--radius-md); }
.rv-sw span.pm-meta-text { display: block; }
.rv-sw ul { display: flex; flex-wrap: wrap; gap: var(--space-1); margin: 0; padding: 0; list-style: none; }
.rv-col .rv-sw:first-of-type { box-shadow: 0 0 0 1px var(--color-border-subtle); }

/* A · Frosted */
.rv-frosted .pm-badge { background: rgb(255 255 255 / 55%); box-shadow: inset 0 0 0 1px rgb(17 24 39 / 8%); }
/* B · Glass */
.rv-glass .pm-badge { background: rgb(255 255 255 / 40%); box-shadow: inset 0 0 0 1px rgb(255 255 255 / 70%), 0 1px 2px rgb(17 24 39 / 6%); -webkit-backdrop-filter: blur(8px) saturate(1.2); backdrop-filter: blur(8px) saturate(1.2); }
@media (prefers-reduced-transparency: reduce) { .rv-glass .pm-badge { -webkit-backdrop-filter: none; backdrop-filter: none; background: var(--color-bg-elevated); } }
/* Dark: the same idea with white at a few percent */
[data-theme="dark"] .rv-frosted .pm-badge { background: rgb(255 255 255 / 6%); box-shadow: inset 0 0 0 1px rgb(255 255 255 / 10%); }
[data-theme="dark"] .rv-glass .pm-badge { background: rgb(255 255 255 / 8%); box-shadow: inset 0 0 0 1px rgb(255 255 255 / 14%); }
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) .rv-frosted .pm-badge { background: rgb(255 255 255 / 6%); box-shadow: inset 0 0 0 1px rgb(255 255 255 / 10%); }
  :root:not([data-theme="light"]) .rv-glass .pm-badge { background: rgb(255 255 255 / 8%); box-shadow: inset 0 0 0 1px rgb(255 255 255 / 14%); }
}
"""

def col(cls, title, note):
    sw = ''.join(f'<div class="rv-sw" style="background:{bg}"><span class="pm-meta-text">{name}</span>'
                 '<ul aria-label="Disciplines"><li class="pm-badge">Product design</li><li class="pm-badge">Analytics</li><li class="pm-badge">AI</li></ul></div>'
                 for name, bg in SURFACES)
    return f'<section class="rv-col {cls}" aria-label="{title}"><h2>{title}</h2><p>{note}</p>{sw}</section>'

page = f'''<title>Badge Review</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&display=swap">
<style>{tokens}
{comps}
{CSS}</style>
<main class="rv">
  <div class="rv-bar"><h1>Badge: Current vs proposed</h1></div>
  <p>Discipline tags sit on the project washes. Each column shows the same three badges on the page and on each wash at its strongest. Use the button to compare dark mode.</p>
  <div class="rv-bar"><button type="button" class="pm-btn pm-btn--secondary pm-btn--sm" id="rv-theme" aria-pressed="false">Dark theme</button></div>
  <div class="rv-grid">{''.join(col(*v) for v in VARIANTS)}</div>
</main>
<script>
(function () {{
  var r = document.documentElement, b = document.getElementById('rv-theme');
  function dark() {{ var t = r.getAttribute('data-theme'); return t ? t === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; }}
  function sync() {{ b.setAttribute('aria-pressed', String(dark())); }}
  b.addEventListener('click', function () {{ r.setAttribute('data-theme', dark() ? 'light' : 'dark'); sync(); }}); sync();
}})();
</script>
'''
open(os.path.join(REPO, 'prototypes', 'review-badges.html'), 'w').write(page)
print(len(page))
