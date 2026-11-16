import sys; sys.path.insert(0,'.')
from rects import R
from PIL import Image, ImageDraw, ImageFilter
OR=(230,95,46)
def ring(im,b,pad=6,w=3,r=10):
    s=2; W,H=im.size
    ov=Image.new('RGBA',(W*s,H*s),(0,0,0,0)); d=ImageDraw.Draw(ov)
    x0,y0,x1,y1=[v*s for v in b]; p=pad*s
    d.rounded_rectangle((x0-p,y0-p,x1+p,y1+p),radius=r*s,outline=OR+(255,),width=w*s)
    d.rounded_rectangle((x0-p-6,y0-p-6,x1+p+6,y1+p+6),radius=(r+6)*s,outline=OR+(60,),width=6*s)
    ov=ov.resize((W,H),Image.LANCZOS)
    return Image.alpha_composite(im.convert('RGBA'),ov)
def screen(n): return Image.open('figma/'+n+'.png').convert('RGBA')
def hero_frame(im):
    W,H=1920,1080
    bg=Image.new('RGB',(W,H)); d=ImageDraw.Draw(bg)
    a,b=(0x2b,0x3a,0x67),(0x7a,0xae,0xe9)
    for x in range(W):
        pass
    # diagonal gradient
    import numpy as np
    yy,xx=np.mgrid[0:H,0:W]; t=((xx/W)+(yy/H))/2
    arr=np.zeros((H,W,3),dtype=np.uint8)
    for i in range(3): arr[...,i]=(a[i]+(b[i]-a[i])*t).astype(np.uint8)
    bg=Image.fromarray(arr).convert('RGBA')
    h=920; w=round(1440*h/1024)
    sc=im.resize((w,h),Image.LANCZOS)
    m=Image.new('L',(w*2,h*2),0); ImageDraw.Draw(m).rounded_rectangle((0,0,w*2-1,h*2-1),radius=28,fill=255); m=m.resize((w,h),Image.LANCZOS)
    x=(W-w)//2; y=(H-h)//2+0
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle((x,y+18,x+w,y+h+18),radius=14,fill=(10,20,50,90))
    sh=sh.filter(ImageFilter.GaussianBlur(28)); bg=Image.alpha_composite(bg,sh)
    bg.paste(sc,(x,y),m); return bg.convert('RGB')
