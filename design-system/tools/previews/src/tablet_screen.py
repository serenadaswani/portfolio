"""TabletScreen: one reusable, scrollable tablet screen, driven by procense/screens.json.

    render('landscape-qc-tests', frame=True, pins=[...])

Each screen is a base image (the fixed viewport: top bar, nav rail, action bar) with, when the screen scrolls, a
focusable scroll box laid exactly over the base image's content area holding the full-length middle section. Positions
are percentages of the base image, so the box stays aligned at any width; width is capped at the native 1x size.

pins: optional markers, each a dict {x, y, html} where x and y are percentages of the base image (as measured on the
static screen) and html is the marker's markup. A pin inside the scroll box is placed in the scrolling content so it
moves with it; anything else (top bar, action bar) stays on the base. Add 'content': True to give x and y as percentages
of the scroll-content image instead, for a pin further down than the first view.

Python 3.9 compatible (the Mac's system Python). Uses design-system tokens; the bezel colour is project art.
"""
import json, os, struct

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
CONFIG = os.path.join(ROOT, 'procense', 'screens.json')
SCALE = 1.5  # Figma exports are 1.5x


def _webp_size(path):
    """Pixel size of a WebP file (VP8, VP8L or VP8X), read from its header."""
    with open(path, 'rb') as f:
        b = f.read(30)
    if b[:4] != b'RIFF' or b[8:12] != b'WEBP':
        raise ValueError(f'{path} is not a WebP file')
    kind = b[12:16]
    if kind == b'VP8X':
        return 1 + int.from_bytes(b[24:27], 'little'), 1 + int.from_bytes(b[27:30], 'little')
    if kind == b'VP8L':
        bits = struct.unpack('<I', b[21:25])[0]
        return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    if kind == b'VP8 ':
        w, h = struct.unpack('<HH', b[26:30])
        return w & 0x3FFF, h & 0x3FFF
    raise ValueError(f'{path}: unknown WebP chunk {kind!r}')


def _pct(v):
    return f'{v:.4f}'.rstrip('0').rstrip('.') + '%'


_cfg = None
def config():
    global _cfg
    if _cfg is None:
        with open(CONFIG, encoding='utf-8') as f:
            _cfg = json.load(f)
    return _cfg


def screen(sid):
    """Resolve one screen's config: orientation, files, pixel sizes and the scroll box (1x px)."""
    cfg = config()
    s = dict(cfg['screens'][sid])
    orient = sid.split('-', 1)[0]
    if orient not in cfg['native']:
        raise ValueError(f'{sid}: ids start with landscape- or portrait-')
    nw, nh = cfg['native'][orient]
    d = os.path.join(ROOT, 'procense', cfg['dir'])
    s.update(id=sid, orientation=orient, native=(nw, nh), base=f'{cfg["dir"]}/{sid}.webp')
    s['base_px'] = _webp_size(os.path.join(d, f'{sid}.webp'))
    if s['base_px'] != (round(nw * SCALE), round(nh * SCALE)):
        raise ValueError(f'{sid}: base image is {s["base_px"]}, expected {nw}x{nh} at {SCALE}x')
    if s.get('scroll'):
        box = s.get('box', 'default')
        s['box'] = cfg['boxes'][orient][box] if isinstance(box, str) else box
        s['scroll'] = f'{cfg["dir"]}/{sid}-scroll.webp'
        s['scroll_px'] = _webp_size(os.path.join(d, f'{sid}-scroll.webp'))
        if s['scroll_px'][0] != round(s['box'][2] * SCALE):
            raise ValueError(f'{sid}: scroll image is {s["scroll_px"][0]}px wide, expected {s["box"][2]} at {SCALE}x')
    else:
        s['scroll'] = None
    return s


def render(sid, frame=False, pins=(), lazy=True, scroll=True):
    """The screen's markup. frame=True wraps it in a tablet bezel (off by default); scroll=False shows the base image only."""
    s = screen(sid)
    if not scroll:
        s['scroll'] = None
    nw, nh = s['native']
    load = ' loading="lazy"' if lazy else ''
    bw, bh = s['base_px']
    base = f'<img class="ts__base" src="{s["base"]}" width="{bw}" height="{bh}"{load} decoding="async" alt="{s["alt"]}">'
    chrome, inner, scroll = [], [], ''
    if s['scroll']:
        l, t, w, h = s['box']
        cw, ch = s['scroll_px']
        content_h = ch / SCALE  # 1x px
        for p in pins:
            if p.get('content'):
                inner.append((p['x'], p['y'], p['html']))
                continue
            x, y = p['x'] / 100 * nw, p['y'] / 100 * nh
            if l <= x <= l + w and t <= y <= t + h:  # inside the scroll area: place it in the content, at scroll 0
                inner.append(((x - l) / w * 100, (y - t) / content_h * 100, p['html']))
            else:
                chrome.append((p['x'], p['y'], p['html']))
        pin = lambda x, y, html: f'<span class="ts__pin" style="left:{_pct(x)};top:{_pct(y)}">{html}</span>'
        box = f'left:{_pct(l / nw * 100)};top:{_pct(t / nh * 100)};width:{_pct(w / nw * 100)};height:{_pct(h / nh * 100)}'
        fade = f'left:{_pct(l / nw * 100)};width:{_pct(w / nw * 100)};bottom:{_pct((nh - t - h) / nh * 100)}'
        scroll = (f'<div class="ts__scroll" style="{box}" tabindex="0" role="region" aria-label="{s["label"]} screen. Scroll for more.">'
                  f'<div class="ts__content"><img src="{s["scroll"]}" width="{cw}" height="{ch}" loading="lazy" decoding="async" alt="">'
                  + ''.join(pin(*q) for q in inner) + '</div></div>'
                  f'<span class="ts__fade" style="{fade}" aria-hidden="true"></span>')
        chrome_html = ''.join(pin(*q) for q in chrome)
    else:
        chrome_html = ''.join(f'<span class="ts__pin" style="left:{_pct(p["x"])};top:{_pct(p["y"])}">{p["html"]}</span>' for p in pins)
    screen_html = f'<div class="ts__screen">{base}{scroll}{chrome_html}</div>'
    if frame:
        screen_html = f'<div class="ts__bezel">{screen_html}</div>'
    mods = f' ts--{s["orientation"]}' + (' ts--framed' if frame else '') + ('' if s['scroll'] else ' ts--static')
    return f'<div class="ts{mods}" data-ts style="--ts-native:{nw}px">{screen_html}</div>'


CSS = """
/* TabletScreen (tablet_screen.py): base image + a scroll box over its content area. Widths cap at the native 1x size. */
.ts { width: 100%; max-width: var(--ts-native); margin-inline: auto; }
.ts--framed.ts--landscape { --ts-bezel: 1.6%; max-width: calc(var(--ts-native) / .968); }
.ts--framed.ts--portrait { --ts-bezel: 3.2%; max-width: calc(var(--ts-native) / .936); }
.ts__bezel { padding: var(--ts-bezel); border-radius: var(--radius-lg); background: #1B2026; box-shadow: 0 2px 4px rgb(0 0 0 / 12%), 0 14px 32px rgb(0 0 0 / 14%); }
.ts__screen { position: relative; overflow: hidden; }
.ts--framed .ts__screen { border-radius: var(--radius-sm); }
.ts__base { display: block; width: 100%; height: auto; }
/* overscroll-behavior: none = no rubber-band bounce at the top or bottom (which would show the base image through the gap)
   and no scroll chaining to the page. The white fill is the mockups' own background, a backstop so nothing shows through. */
.ts__scroll { position: absolute; overflow-x: hidden; overflow-y: auto; overscroll-behavior: none; touch-action: pan-y;
  scrollbar-width: none; background: #FFFFFF; }
.ts__scroll::-webkit-scrollbar { display: none; }  /* hidden so it never takes width from the content (which would misalign it); the fade is the cue */
.ts__scroll:focus-visible { outline: var(--focus-ring-width) solid var(--color-focus-ring); outline-offset: calc(-1 * var(--focus-ring-width)); }
.ts__content { position: relative; }
.ts__content > img { display: block; width: 100%; height: auto; }
.ts__pin { position: absolute; width: 0; height: 0; }
/* "More below" cue: a soft shadow rising from the bottom edge of the scroll box; gone once scrolled to the end */
.ts__fade { position: absolute; height: 9%; pointer-events: none; background: linear-gradient(to bottom, rgb(11 18 32 / 0%), rgb(11 18 32 / 11%)); }
.ts__screen[data-at-end] .ts__fade { opacity: 0; }
@media (prefers-reduced-motion: no-preference) { .ts__fade { transition: opacity .25s ease; } }
"""

JS = r"""
  // TabletScreen: hide the bottom fade once a screen is scrolled to its end; TabletScreen.reveal(el) scrolls el into the
  // middle of its screen's scroll box (and the screen into the page view). init() also runs on lightbox clones.
  window.TabletScreen = (function () {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function init(root) {
      [].forEach.call((root || document).querySelectorAll('.ts__scroll'), function (sc) {
        if (sc._ts) return; sc._ts = 1;
        var scr = sc.parentNode;
        function upd() { scr.toggleAttribute('data-at-end', sc.scrollTop + sc.clientHeight >= sc.scrollHeight - 2); }
        sc.addEventListener('scroll', upd, { passive: true });
        var img = sc.querySelector('img'); if (img) img.addEventListener('load', upd);
        window.addEventListener('resize', upd); upd();
      });
    }
    function reveal(el) {
      var sc = el.closest('.ts__scroll'), ts = el.closest('.ts'), b = reduce ? 'auto' : 'smooth';
      if (ts) { var r = ts.getBoundingClientRect(); if (r.top < 0 || r.bottom > window.innerHeight) ts.scrollIntoView({ block: r.height > window.innerHeight ? 'start' : 'nearest', behavior: b }); }
      if (sc) {
        var er = el.getBoundingClientRect(), sr = sc.getBoundingClientRect();
        sc.scrollTo({ top: sc.scrollTop + (er.top + er.height / 2) - (sr.top + sr.height / 2), behavior: b });
      }
    }
    init();
    return { init: init, reveal: reveal };
  })();
"""
