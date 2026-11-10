import os,re
B=os.path.dirname(os.path.abspath(__file__))
PUB=os.path.abspath(os.path.join(B,'..','..','published'))
chk=open(f'{B}/src/check.js').read()
def out(name,html):
    d=f'{PUB}/components/{name}'; os.makedirs(d,exist_ok=True); open(f'{d}/preview.html','w').write(html)
cs=open(f'{B}/src/ColorSurfaces.html').read().replace('{{CHECK_FN}}',chk); out('ColorSurfaces',cs)
L=open(f'{B}/src/Layout.html').read().replace('{{CHECK_FN}}',chk)
for name,w,h,sub in [('Mobile375',375,7620,'Mobile, 375px: 4-column grid, base type scale, stacked header. Light then dark.'),
                     ('Tablet768',768,6320,'Tablet, 768px: 8-column grid, two cards per row, tablet type steps. Light then dark.'),
                     ('Desktop1280',1280,5240,'Desktop, 1280px: 12-column grid, sticky metadata aside, desktop type steps. Light then dark.')]:
    out(name,L.replace('{{W}}',str(w)).replace('{{H}}',str(h)).replace('{{SUB}}',sub))
print('built')
