import json,re,sys
t=json.load(open(sys.argv[1]))
def v(x): return re.sub(r'^\{(.+)\}$', r'var(--\1)', x)
L=['@import url("https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&family=Geist+Mono:wght@400;500&display=swap");',':root, [data-theme="light"] {']
for k in t['color']['tokens']:
  val=k['value']; L.append(f"  --{k['name']}: {v(val if isinstance(val,str) else val['light'])};")
L.append('}\n[data-theme="dark"] {')
for k in t['color']['tokens']:
  val=k['value']
  if not isinstance(val,str): L.append(f"  --{k['name']}: {v(val['dark'])};")
L.append('}\n:root {')
for fam,d in t.items():
  if isinstance(d,dict) and 'tokens' in d and fam!='color':
    for k in d['tokens']: L.append(f"  --{k['name']}: {k['value']};")
for k,val in t['type']['families'].items(): L.append(f"  --font-{k}: {val};")
L.append('}')
for g in t['type']['groups']:
  for s in g['styles']: L.append(f".{s['name']} {{ font-family: var(--font-sans); font-size:{s['fontSize']}; line-height:{s['lineHeight']}; font-weight:{s['fontWeight']}; letter-spacing:{s['letterSpacing']}; }}")
print('\n'.join(L))
