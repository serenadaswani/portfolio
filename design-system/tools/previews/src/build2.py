import os, sys, importlib, glob
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(B, 'src'))
sys.path.insert(0, os.path.join(B, 'src', 'comps'))
CHECK = open(os.path.join(B, 'src', 'check.js')).read()
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">')
THEMES = [('light', 'l', 'Light · Paper'), ('dark', 'd', 'Dark · Midnight')]

def pairs_html(pairs, theme=None):
    out = []
    for label, fg, bg, mn in pairs:
        deco = ' data-deco' if mn == 0 else ''
        out.append(f'<span class="pm-spec__cap">{label} <span data-fg="{fg}" data-bg="{bg}" data-min="{mn or 3}"{deco}></span></span>')
    return '<div class="pm-spec__a11y"' + (f' data-theme="{theme}" style="background:var(--ink);padding:var(--space-3);border-radius:var(--radius-md)"' if theme else '') + ' aria-label="Contrast checks">' + ''.join(out) + '</div>'

def render(m):
    w = f' width={m.WIDTH}' if getattr(m, 'WIDTH', None) else ''
    head = f'<!-- @dsCard group="{m.GROUP}" height={m.HEIGHT}{w} subtitle="{m.SUB}" -->\n'
    secs = []
    for th, t, name in THEMES:
        body = m.BODY.replace('{T}', t).replace('{V}', 'x')
        secs.append(f'<section class="pm-spec" data-theme="{th}" aria-label="{name}"><p class="pm-spec__theme">{name}</p>{body}{pairs_html(getattr(m, "PAIRS", []), getattr(m, "PAIRS_THEME", None))}</section>')
    style = getattr(m, 'STYLE', '')
    script = getattr(m, 'SCRIPT', '')
    return (head + '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{m.NAME}</title>\n{FONTS}\n<style>{style}</style>\n</head>\n<body>\n<main>\n' + '\n'.join(secs) +
            '\n</main>\n<script>\n' + CHECK + '\n' + script + '\n</script>\n</body>\n</html>\n')

names = []
for f in sorted(glob.glob(os.path.join(B, 'src', 'comps', '*.py'))):
    m = importlib.import_module(os.path.basename(f)[:-3])
    d = os.path.join(B, '..', '..', 'published', 'components', m.NAME)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'preview.html'), 'w').write(render(m))
    open(os.path.join(d, 'README.md'), 'w').write(m.README.strip() + '\n')
    names.append(m.NAME)
print(' '.join(names))
