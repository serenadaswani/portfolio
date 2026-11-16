import sys,subprocess,os; sys.path.insert(0,'.')
from frames import *
kind=sys.argv[1]
if kind in ('hero','hero2'):
    seq=[('landing','create'),('landing2','newchart'),('details-filled','next'),('flowtype','guided'),('metrics-expanded','next'),('seasons','seasons'),('review','save'),('viewchart',None)]
else:
    seq=[('landing','create'),('landing2','newchart'),('details-filled','next'),('flowtype','guided'),('tooltip','tip'),('metrics-expanded','chips'),('metrics-expanded','next'),('seasons','league'),('seasons','seasons'),('review','stepper'),('review','save'),('viewchart',None),('landing','create'),('flowtype','presets'),('presetsetup','preset1'),('editchart','dup')]
d='vid/'+kind; os.makedirs(d,exist_ok=True)
files=[]
for i,(n,k) in enumerate(seq):
    im=screen(n)
    a=im; b=ring(im,R[n][k]) if k else im
    if kind=='hero': a,b=hero_frame(a),hero_frame(b)
    else: a,b=a.convert('RGB'),b.convert('RGB')
    fa=f'{d}/{i:02d}a.png'; fb=f'{d}/{i:02d}b.png'; a.save(fa); b.save(fb); files+= [(fa,0.7 if k else 2.2),(fb,0.9)] if k else [(fa,2.4)]
# build ffmpeg xfade chain
inputs=[];filt=[];T=0.35
for f,dur in files: inputs+=['-loop','1','-t',str(dur+T),'-i',f]
prev='[0:v]';off=0
for j in range(1,len(files)):
    off+=files[j-1][1]
    tr='fade' if files[j][0].endswith('b.png') else 'fade'
    dd=0.15 if files[j][0].endswith('b.png') else T
    out=f'[v{j}]'
    filt.append(f'{prev}[{j}:v]xfade=transition={tr}:duration={dd}:offset={off:.2f}{out}')
    prev=out; off+=0
    # account: xfade offset is in output timeline; subtract nothing since each input has +T tail
    off-=dd; off+=dd  # keep simple timeline
fc=';'.join(filt)+f';{prev}format=yuv420p[out]'
outp=f'out/{kind}.mp4'
cmd=['ffmpeg','-y','-loglevel','error',*inputs,'-filter_complex',fc,'-map','[out]','-r','30','-c:v','libx264','-preset','slow','-crf','20','-movflags','+faststart',outp]
subprocess.run(cmd,check=True); print(outp)
