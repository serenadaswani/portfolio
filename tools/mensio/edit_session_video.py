import subprocess, sys, os
S = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(S, 'session-src.mp4')
FONT = sys.argv[1]
OUT = os.path.join(S, 'out', 'session.mp4')
W, H = 1600, 900
PW, PH = 1914, 1076          # source padded to 16:9
PADY = (PH - 938) // 2
FPS = 30
# (start, end, speed, caption, (cx0, cy0, z0) -> (cx1, cy1, z1)) in source pixels (unpadded y)
SEG = [
 (0.3, 3.3, 1.0, '1  Picks metrics from 40+ options', (957, 469, 1.0), (520, 380, 1.9)),
 (6.0, 12.0, 2.0, '2  Sets a date range', (957, 469, 1.0), (960, 430, 1.6)),
 (21.5, 26.0, 1.0, '3  Hits an invalid combination', (957, 469, 1.0), (1700, 200, 3.0)),
 (27.0, 31.0, 1.6, '4  Reworks the grouping', (957, 469, 1.0), (600, 400, 1.7)),
 (34.0, 43.0, 3.0, '5  Waits for the data to load', (957, 469, 1.0), (957, 469, 1.15)),
 (46.5, 50.2, 1.0, '6  Leaves without saving. Progress lost.', (957, 469, 1.0), (860, 380, 1.8)),
]
def ease(p): return f"if(lt({p},0.5),2*{p}*{p},1-pow(-2*{p}+2,2)/2)"
parts, inputs = [], []
for i, (a, b, sp, cap, (x0, y0, z0), (x1, y1, z1)) in enumerate(SEG):
    dur = (b - a) / sp
    N = max(1, int(dur * FPS * 0.7))
    p = f"min(on/{N},1)"
    e = ease(p)
    z = f"({z0}+({z1}-{z0})*{e})"
    cx = f"({x0}+({x1}-{x0})*{e})"
    cy = f"({y0 + PADY}+({y1 + PADY}-{y0 + PADY})*{e})"
    xs = f"max(0,min(iw-iw/zoom,{cx}-iw/zoom/2))"
    ys = f"max(0,min(ih-ih/zoom,{cy}-ih/zoom/2))"
    txt = cap.replace(':', '\\:').replace("'", "’")
    chain = (f"[0:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)/{sp},fps={FPS},"
             f"drawbox=x=1730:y=8:w=160:h=42:color=0x1a112b:t=fill,"
             f"pad={PW}:{PH}:0:{PADY}:color=white,"
             f"zoompan=z='{z}':x='{xs}':y='{ys}':d=1:s={W}x{H}:fps={FPS},"
             f"drawtext=fontfile='{FONT}':text='{txt}':fontsize=42:fontcolor=white:box=1:boxcolor=0x206cfd:boxborderw=20:x=56:y=h-th-72,"
             f"fade=t=in:st=0:d=0.2:color=white,fade=t=out:st={dur - 0.2:.2f}:d=0.2:color=white,setsar=1[v{i}]")
    parts.append(chain)
fc = ';'.join(parts) + ';' + ''.join(f'[v{i}]' for i in range(len(SEG))) + f'concat=n={len(SEG)}:v=1:a=0,format=yuv420p[out]'
cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', SRC, '-filter_complex', fc, '-map', '[out]', '-an',
       '-c:v', 'libx264', '-preset', 'slow', '-crf', '24', '-movflags', '+faststart', OUT]
subprocess.run(cmd, check=True)
print(OUT)
