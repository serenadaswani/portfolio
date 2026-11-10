# Derives the portable design-system/css/components.css from the authored published/components/bundle.css.
# Removes: section 0 (responsive re-point + touch sizes, which tokens.css handles), the HIG preference overrides
# (also in tokens.css), and section 22 (specimen scaffolding used only by the published previews).
# Usage (from the repo root):  python3 design-system/tools/build_components_css.py
import os, re
DS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(DS, 'published', 'components', 'bundle.css')).read()
c = src[:src.index('/* ---------- 22. Specimen scaffolding')]
a = c.index('/* ---------- 0.'); b = c.index('/* ---------- 1. Base')
c = c[:a] + '/* Responsive type, touch sizes, Increase Contrast and Reduce Transparency come from tokens.css. Display styles: font-stretch: var(--font-width-display). */\n\n' + c[b:]
i = c.index('/* HIG Increase Contrast'); j = c.index('}\n}', c.index('prefers-reduced-transparency')) + 3
c = c[:i] + c[j:]
c = re.sub(r'^/\* Paper × Midnight — component stylesheet (v[\d.]+) \([^)]*\)', r'/* Paper × Midnight — component stylesheet \1 (load after tokens.css)', c, count=1)
open(os.path.join(DS, 'css', 'components.css'), 'w').write(c)
print('css/components.css written')
