# Paper × Midnight token emitter.
# Source of truth: design-system/tokens/design-tokens.json (DTCG-style).
# Emits: design-system/css/tokens.css and design-system/published/tokens.json (the Claude design-system artifact's list-shaped tokens).
# Usage (from the repo root):  python3 design-system/tools/build_tokens.py
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
DS = os.path.dirname(HERE)
SRC = os.path.join(DS, 'tokens', 'design-tokens.json')
OUT_CSS = os.path.join(DS, 'css', 'tokens.css')
OUT_ART = os.path.join(DS, 'published', 'tokens.json')
USAGE = os.path.join(HERE, 'usage.json')
src = json.load(open(SRC))
prim = src['color']['primitive']
sem = src['color']['semantic']
ty = src['typography']
def kebab(s): return re.sub(r'(?<=[a-z])(?=[A-Z0-9])','-',s).lower()
SH = {k: (v['$value']['light'], v['$value']['dark']) for k, v in src['shadow'].items() if k != 'none' and isinstance(v.get('$value'), dict)}
def dv(*path):
    node = src
    for p in path: node = node[p]
    return node['$value']
# ---------- resolve helpers
def resolve(v,th=None):
  while isinstance(v,str) and v.startswith('{'):
    path=v[1:-1].split('.'); node=src
    for p in path: node=node[p]
    v=node['$value']
  return v
def cssname_sem(grp,key):
  m={'background':'bg'}; g=m.get(grp,grp); k=kebab(key)
  special={('bg','selectedBackground'):'', }
  name={('action','selectedBackground'):'action-selected-bg',('action','selectedText'):'action-selected-text',('action','selectedIndicator'):'selected-indicator',
        ('focus','ring'):'focus-ring',('state','successBackground'):'state-success-bg',('state','warningBackground'):'state-warning-bg',
        ('state','errorBackground'):'state-error-bg',('state','infoBackground'):'state-info-bg',('disabled','background'):'disabled-bg',
        ('text','onAccent'):'text-on-accent',('text','onImage'):'text-on-image'}.get((grp,key))
  return 'color-'+(name or f'{g}-{k}')
primcss={k:kebab(k) for k in prim}
for k in list(primcss):
  if k.startswith('cobalt'): primcss[k]='cobalt-'+k[6:]
def ref_to_css(v):
  if isinstance(v,str) and v.startswith('{color.primitive.'): return 'var(--'+primcss[v[17:-1]]+')'
  if isinstance(v,str) and v.startswith('{color.semantic.'):
    p=v[1:-1].split('.'); return 'var(--'+cssname_sem(p[3],p[4])+')'
  return v
# ---------- tokens.css
L=['/* Paper × Midnight — semantic CSS tokens v1.6 (generated from design-tokens.json) */',
   '/* Audit fixes applied. Provisional: test the rendered build for WCAG 2.2 AA. */',':root {','  color-scheme: light;']
L.append('  /* primitives */')
for k,v in prim.items(): L.append(f'  --{primcss[k]}: {v["$value"]};')
def sem_block(th,ind='  '):
  out=[]
  for grp,d in sem[th].items():
    for key,t in d.items(): out.append(f'{ind}--{cssname_sem(grp,key)}: {ref_to_css(t["$value"])};')
  return out
L.append('  /* semantic: light (default) */'); L+=sem_block('light')
L.append('  /* type */')
fam=lambda k: ', '.join(f'"{x}"' if ' ' in x else x for x in ty['fontFamily'][k]['$value'])
L.append(f'  --font-sans: {fam("sans")}; --font-meta: {fam("meta")};')
L.append(f"  --font-width-display: {ty['fontWidth']['display']['$value']}; --font-width-text: {ty['fontWidth']['text']['$value']};")
for k,v in ty['fontWeight'].items():
  if k!='wordmark' and not str(v['$value']).startswith('{'): L.append(f'  --weight-{k}: {v["$value"]};')
L.append('  --weight-wordmark: var(--weight-semibold);')
names={'displayXl':'display-xl','displayLg':'display-lg','h1':'h1','h2':'h2','h3':'h3','h4':'h4','bodyLg':'body-lg','bodyMd':'body-md','bodySm':'body-sm','labelMd':'label','caption':'caption','micro':'micro'}
for k,v in ty['scale'].items():
  n=names[k]; s=v['$value']
  L.append(f'  --type-{n}: {s["fontSize"]}; --line-{n}: {s["lineHeight"]}; --weight-{n}: {s["fontWeight"]}; --tracking-{n}: {s["letterSpacing"]};')
for k,v in ty['tracking'].items(): L.append(f'  --tracking-{k}: {v["$value"]};')
L.append('  /* space, shape, layout */')
for k,v in src['spacing'].items(): L.append(f'  --space-{k[5:]}: {v["$value"]};')
for k,v in src['layout']['radius'].items(): L.append(f'  --radius-{k}: {v["$value"]};')
L.append(f'  --content-max-width: {src["layout"]["contentMaxWidth"]["$value"]}; --reading-max-width: {src["layout"]["readingMaxWidth"]["$value"]};')
for k,v in src['layout']['grid'].items(): L.append(f'  --grid-columns-{k.replace("Columns","")}: {v["$value"]};')
L.append('  /* interaction */')
L.append(f"  --focus-ring-width: {dv('focus','ringWidth')}; --focus-ring-offset: {dv('focus','ringOffset')};")
L.append(f"  --link-underline-thickness: {dv('link','underlineThickness')}; --link-underline-thickness-hover: {dv('link','underlineThicknessHover')}; --link-underline-offset: {dv('link','underlineOffset')};")
ez=dv('motion','ease'); ez=ez if isinstance(ez,str) else 'cubic-bezier('+', '.join(str(x) for x in ez)+')'
L.append(f"  --motion-duration-fast: {dv('motion','durationFast')}; --motion-duration-base: {dv('motion','durationBase')}; --motion-ease: {ez};")
L.append(f"  --control-height-xs: {dv('control','heightXs')}; --control-height-sm: {dv('control','heightSm')}; --control-height-md: {dv('control','heightMd')}; --control-height-lg: {dv('control','heightLg')}; --control-min-target: {dv('control','minTarget')};")
L.append('  --shadow-none: none;')
for k,(l,d) in SH.items(): L.append(f'  --shadow-{k}: {l};')
L.append('}')
dark=sem_block('dark','    ')
dark=dark+[f'    --shadow-{k}: {d};' for k,(l,d) in SH.items()]
L+=['[data-theme="dark"] {','  color-scheme: dark;']+[d[2:] for d in dark]+['}']
L+=['@media (prefers-color-scheme: dark) {','  :root:not([data-theme="light"]) {','    color-scheme: dark;']+dark+['  }','}']
def bpblock(bp):
  out=[]
  for k,(fs,lh) in ty['responsiveScale'][bp].items():
    n=names[k]; out.append(f'    --type-{n}: {fs}; --line-{n}: {lh};')
  return out
L+=['/* Apple HIG accessibility settings */',
 '@media (prefers-contrast: more) {',
 '  :root { --color-border-subtle: var(--silver); --color-border-default: var(--light-border-strong); --color-border-button: var(--light-border-strong); --color-text-tertiary: var(--blue-slate); }',
 '  [data-theme="dark"] { --color-border-subtle: var(--dark-border-default); --color-border-default: var(--dark-border-strong); --color-border-button: var(--steel); --color-text-tertiary: var(--dark-text-secondary); }',
 '}',
 '@media (prefers-contrast: more) and (prefers-color-scheme: dark) {',
 '  :root:not([data-theme="light"]) { --color-border-subtle: var(--dark-border-default); --color-border-default: var(--dark-border-strong); --color-border-button: var(--steel); --color-text-tertiary: var(--dark-text-secondary); }',
 '}',
 '@media (prefers-reduced-transparency: reduce) {',
 '  :root, [data-theme] { --color-overlay-scrim: var(--ink); --color-overlay-backdrop: var(--ink); }',
 '}']
L+=['@media (pointer: coarse) {',f"  :root {{ --control-height-md: {dv('control','coarse','heightMd')}; --control-height-lg: {dv('control','coarse','heightLg')}; --control-min-target: {dv('control','coarse','minTarget')}; }}",'}']
L+=['@media (min-width: 768px) {','  :root {']+bpblock('tablet')+['  }','}']
L+=['@media (min-width: 1024px) {','  :root {']+bpblock('desktop')+['  }','}']
L+=[':focus-visible { outline: var(--focus-ring-width) solid var(--color-focus-ring); outline-offset: var(--focus-ring-offset); }',
    '@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; } }','']
open(OUT_CSS,'w').write('\n'.join(L))

# ---------- artifact tokens.json (list shape)
usage=json.load(open(USAGE))
ctoks=[]
for k,v in prim.items():
  ctoks.append({'name':primcss[k],'value':v['$value'],'usage':usage['prim'].get(primcss[k],'Primitive. Feeds semantic roles only; never used directly in components.')})
for grp,d in sem['light'].items():
  for key,t in d.items():
    n=cssname_sem(grp,key); lv=ref_to_css(t['$value']); dv=ref_to_css(sem['dark'][grp][key]['$value'])
    a=lambda x: '{'+x[6:-1]+'}' if x.startswith('var(') else x
    ctoks.append({'name':n,'value':{'light':a(lv),'dark':a(dv)},'usage':usage['sem'].get(n,'')})
groups=[]
G=[('Display',['displayXl','displayLg'],'Instrument Sans at 90% width (font-width-display). Responsive: steps up at 768px and 1024px via responsiveType.'),('Headings',['h1','h2','h3','h4'],None),('Body',['bodyLg','bodyMd','bodySm'],None),('Utility',['labelMd','caption','micro'],'Label tracking resolved to 0.02em.')]
for gname,keys,note in G:
  g={'name':gname,'family':'sans','styles':[]}
  if note: g['note']=note
  for k in keys:
    s=ty['scale'][k]['$value']; n=names[k]; u=usage['type'][n]
    g['styles'].append({'name':n,'fontSize':s['fontSize'],'lineHeight':s['lineHeight'],'fontWeight':s['fontWeight'],'letterSpacing':s['letterSpacing'],'sample':u[0],'usage':u[1]})
  groups.append(g)
def fam(items,note=None):
  d={'tokens':[{'name':a,'value':b,'usage':c} for a,b,c in items]}
  if note: d['note']=note
  return d
scale=[]
for k,v in ty['scale'].items():
  n=names[k]; s=v['$value']
  scale+= [(f'type-{n}',s['fontSize'],f'{n} size (mobile base); components read this var.'),(f'line-{n}',str(s['lineHeight']),f'{n} line height, unitless.')]
resp=[]
for bp,mn in [('tablet','768'),('desktop','1024')]:
  for k,(fs,lh) in ty['responsiveScale'][bp].items():
    n=names[k]
    if bp=='desktop' and n in('h3','body-lg'): continue
    resp+=[(f'type-{n}-{bp}',fs,f'{n} size at ≥{mn}px.'),(f'line-{n}-{bp}',str(lh),f'{n} line height at ≥{mn}px.')]
art={'name':'Paper × Midnight','version':4,
 'color':{'themes':[{'id':'light','name':'Light · Paper'},{'id':'dark','name':'Dark · Midnight'}],'note':'v1.1 with audit fixes applied. Components use only color-* roles; primitives feed them.','tokens':ctoks},
 'type':{'fonts':[],'families':{'sans':'"Instrument Sans", sans-serif','meta':'"Instrument Sans", sans-serif'},'groups':groups},
 'fontWidth':fam([('font-width-display','90%','font-stretch for display-xl and display-lg: condensed editorial headlines.'),('font-width-text','100%','Every other style.')],'Instrument Sans width axis (75–100%).'),
 'spacing':fam([(f'space-{k[5:]}',v['$value'],usage['space'][k]) for k,v in src['spacing'].items()],'4px base.'),
 'radius':fam([(f'radius-{k}',v['$value'],usage['radius'][k]) for k,v in src['layout']['radius'].items()]),
 'shadow':{'note':'Flat but dimensional: a light 1px ring plus soft, Midnight-tinted, negative-spread shadows (layered like Stripe). Never as the only edge.','tokens':[{'name':'shadow-none','value':'none','usage':'Flat elements: nav, links, badges, inputs, frameless cards.'},{'name':'shadow-xs','value':{'light':SH['xs'][0],'dark':SH['xs'][1]},'usage':'Resting containers with a border-subtle ring: panels, outlined cards, bento tiles, secondary buttons, the selected segment.'},{'name':'shadow-sm','value':{'light':SH['sm'][0],'dark':SH['sm'][1]},'usage':'Hover on interactive surfaces (outlined cards, link tiles, thumbnails); tooltip.'},{'name':'shadow-md','value':{'light':SH['md'][0],'dark':SH['md'][1]},'usage':'Popover; the featured bento tile.'},{'name':'shadow-lg','value':{'light':SH['lg'][0],'dark':SH['lg'][1]},'usage':'Dialog and sheet.'}]},
 'typeScale':fam(scale,'Same values as the type styles, exposed as the vars tokens.css defines, so component CSS is portable.'),
 'responsiveType':fam(resp,'bundle.css re-points --type-*/--line-* to these at 768px and 1024px.'),
 'tracking':fam([(f'tracking-{k}',v['$value'],usage['tracking'][k]) for k,v in ty['tracking'].items()]),
 'fontWeight':fam([('weight-regular','400','Body, caption.'),('weight-medium','500','Headings, labels, buttons.'),('weight-semibold','600','Wordmark only.')]),
 'interaction':fam([('focus-ring-width','3px','Every focus-visible outline.'),('focus-ring-offset','3px','Keeps the ring on the ground, not the fill (ring vs cobalt fill is 1.36:1).'),
    ('link-underline-thickness','1px','Links at rest.'),('link-underline-thickness-hover','2px','Links on hover.'),('link-underline-offset','0.2em','All underlined links.'),
    ('motion-duration-fast','120ms','Color and border transitions.'),('motion-duration-base','200ms','Overlays (tooltip, lightbox) fading in.'),('motion-ease','cubic-bezier(0.2, 0, 0, 1)','All transitions; disabled under prefers-reduced-motion.')]),
 'control':fam([('control-height-xs','24px','Inline and table actions, tag-adjacent controls. Keep 8px or more between targets.'),('control-height-sm','32px','Toolbars, panel headers, secondary nav actions.'),('control-height-md','40px','Default buttons, nav items, icon buttons (44px on touch).'),('control-height-lg','48px','Hero call to action (52px on touch).'),('control-min-target','24px','WCAG 2.5.8 floor (44px on touch).'),('control-height-md-coarse','44px','control-height-md under pointer: coarse.'),('control-height-lg-coarse','52px','control-height-lg under pointer: coarse.'),('control-min-target-coarse','44px','control-min-target under pointer: coarse.')],'Compact for pointers (Linear, Geist); touch sizes follow Apple HIG via pointer: coarse.'),
 'layout':fam([('content-max-width','1200px','Page container.'),('reading-max-width','680px','Prose measure.'),('grid-columns-mobile','4','≤767px.'),('grid-columns-tablet','8','768–1023px.'),('grid-columns-desktop','12','≥1024px.')]),
 'breakpoint':fam([('breakpoint-tablet-min','768px','Tablet type, 8-column grid, container queries.'),('breakpoint-desktop-min','1024px','Desktop type, 12-column grid, container queries.')],'Container queries use these literal values (CSS cannot read vars in conditions).'),
}
json.dump(art,open(OUT_ART,'w'),indent=1,ensure_ascii=False)
print('colors',len(ctoks))

print('tokens.css and published/tokens.json written')
