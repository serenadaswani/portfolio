# Builds local test copies of every preview (compiled tokens + bundle.css inlined) into tools/previews/.local/
import os, glob
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.abspath(os.path.join(B, '..', '..', 'published'))
LOCAL = os.path.join(B, '.local'); os.makedirs(LOCAL, exist_ok=True)
css = open(os.path.join(LOCAL, 'tokens.compiled.css')).read() + '\n' + open(os.path.join(PUB, 'components', 'bundle.css')).read()
for p in glob.glob(os.path.join(PUB, 'components', '*', 'preview.html')):
    n = p.split(os.sep)[-2]
    h = open(p).read().replace('</head>', '<style>' + css + '</style></head>', 1)
    h = h.replace('<html lang="en">', '<html lang="en" data-theme="light">', 1)
    open(os.path.join(LOCAL, n + '.html'), 'w').write(h)
print('local previews in', LOCAL)
