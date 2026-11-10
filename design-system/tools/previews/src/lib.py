import urllib.parse

import json as _json, os as _os
LUCIDE = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'lucide.json')))  # lucide-static 0.460.0 (ISC)

def _l(name, cls='pm-icon'):
    # Lucide as shadcn/ui ships it: 24px grid, stroke 2, round caps/joins, currentColor
    return ('<svg class="' + cls + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' + LUCIDE[name] + '</svg>')

I = {
 'chev': _l('chevron-down'), 'arrow': _l('arrow-right'), 'ext': _l('external-link'), 'close': _l('x'),
 'prev': _l('chevron-left'), 'next': _l('chevron-right'), 'play': _l('play'), 'pause': _l('pause'),
 'cc': _l('captions'), 'vol': _l('volume-2'), 'full': _l('maximize'), 'copy': _l('copy'), 'info': _l('info'),
 'check': _l('check'), 'image': _l('image'), 'broken': _l('image-off'), 'expand': _l('maximize-2'),
 'menu': _l('menu'), 'moon': _l('moon'), 'download': _l('download'), 'edit': _l('pencil'), 'lock': _l('lock'), 'user': _l('user-round'),
}

# Status glyphs: Lucide outline shapes, one distinct shape per status (never colour alone)
S = {
 'success': _l('circle-check', 'pm-status__icon'),
 'warning': _l('triangle-alert', 'pm-status__icon'),
 'error': _l('octagon-x', 'pm-status__icon'),
 'info': _l('info', 'pm-status__icon'),
 'progress': _l('circle-dot', 'pm-status__icon'),
 'neutral': _l('circle-dashed', 'pm-status__icon'),
}

def svg_uri(svg):
    return 'data:image/svg+xml,' + urllib.parse.quote(svg)

# Simulated project imagery (stand-in screenshots; literal hex is content, not chrome)
def _ui(bg, panel, line, accent, w=1600, h=1000, kind='queue'):
    if kind == 'queue':
        rows = ''.join(f'<rect x="440" y="{180+i*120}" width="1060" height="96" rx="12" fill="{panel}"/>'
                       f'<rect x="480" y="{212+i*120}" width="{420-i*40}" height="14" rx="7" fill="{line}"/>'
                       f'<rect x="480" y="{240+i*120}" width="260" height="10" rx="5" fill="{line}" opacity=".6"/>'
                       f'<rect x="1340" y="{214+i*120}" width="120" height="28" rx="14" fill="{accent if i==0 else line}" opacity="{1 if i==0 else .5}"/>' for i in range(6))
        body = (f'<rect width="{w}" height="{h}" fill="{bg}"/><rect x="0" y="0" width="360" height="{h}" fill="{panel}"/>'
                f'<rect x="40" y="60" width="200" height="16" rx="8" fill="{line}"/>' +
                ''.join(f'<rect x="40" y="{130+i*56}" width="{240-i*20}" height="12" rx="6" fill="{line}" opacity=".7"/>' for i in range(7)) +
                f'<rect x="440" y="60" width="520" height="40" rx="8" fill="{line}"/><rect x="1300" y="56" width="200" height="48" rx="10" fill="{accent}"/>' + rows)
    elif kind == 'grid':
        cells = ''.join(f'<rect x="{80+(i%5)*296}" y="{140+(i//5)*270}" width="256" height="230" rx="16" fill="{panel}"/>'
                        f'<rect x="{110+(i%5)*296}" y="{170+(i//5)*270}" width="80" height="80" rx="10" fill="{accent if i%4==0 else line}" opacity="{1 if i%4==0 else .55}"/>'
                        f'<rect x="{110+(i%5)*296}" y="{290+(i//5)*270}" width="160" height="12" rx="6" fill="{line}"/>' for i in range(15))
        body = f'<rect width="{w}" height="{h}" fill="{bg}"/><rect x="80" y="60" width="420" height="28" rx="8" fill="{line}"/>' + cells
    elif kind == 'form':
        fields = ''.join(f'<rect x="420" y="{200+i*110}" width="180" height="12" rx="6" fill="{line}"/><rect x="420" y="{224+i*110}" width="760" height="52" rx="8" fill="{panel}" stroke="{line}" stroke-width="2"/>' for i in range(5))
        body = (f'<rect width="{w}" height="{h}" fill="{bg}"/><rect x="380" y="100" width="840" height="820" rx="20" fill="{bg}" stroke="{line}" stroke-width="2"/>'
                f'<rect x="420" y="140" width="340" height="24" rx="8" fill="{line}"/>' + fields +
                f'<rect x="980" y="780" width="200" height="56" rx="10" fill="{accent}"/>')
    elif kind == 'chart':
        pts = [820, 760, 780, 640, 600, 520, 470, 420, 330, 300]
        path = 'M120 ' + ' L'.join(f'{120+i*150} {p}' for i, p in enumerate(pts))
        body = (f'<rect width="{w}" height="{h}" fill="{bg}"/>' +
                ''.join(f'<rect x="120" y="{200+i*160}" width="1360" height="2" fill="{line}" opacity=".6"/>' for i in range(5)) +
                f'<path d="{path}" fill="none" stroke="{accent}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<rect x="120" y="80" width="360" height="28" rx="8" fill="{line}"/>')
    else:  # mobile
        body = (f'<rect width="{w}" height="{h}" fill="{bg}"/><rect x="60" y="80" width="{w-120}" height="40" rx="10" fill="{line}"/>' +
                ''.join(f'<rect x="60" y="{180+i*170}" width="{w-120}" height="140" rx="16" fill="{panel}"/><rect x="90" y="{210+i*170}" width="{200-i*20}" height="16" rx="8" fill="{line}"/>' for i in range(5)) +
                f'<rect x="60" y="{h-140}" width="{w-120}" height="72" rx="16" fill="{accent}"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{body}</svg>'

IMG = {
 'queue': svg_uri(_ui('#F6F7F9', '#FFFFFF', '#C9D1DC', '#2F5BFF', kind='queue')),
 'grid': svg_uri(_ui('#0F1B2D', '#1C2B41', '#3B4B62', '#7EA0FF', kind='grid')),
 'form': svg_uri(_ui('#FFFFFF', '#F3F5F8', '#C9D1DC', '#1D37B8', kind='form')),
 'chart': svg_uri(_ui('#FBFBF9', '#FFFFFF', '#D5DBE3', '#2448D8', kind='chart')),
 'mobile': svg_uri(_ui('#F6F7F9', '#FFFFFF', '#C9D1DC', '#2F5BFF', w=780, h=1560, kind='mobile')),
 'white': svg_uri('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 10"><rect width="16" height="10" fill="#FFFFFF"/></svg>'),
}
IMG_ALT = {
 'queue': 'Review queue: a ranked list of six evaluations, the top one flagged high risk.',
 'grid': 'Token library in dark mode: a grid of fifteen colour and type tokens.',
 'form': 'Permissions console: a five-field role form with a save button.',
 'chart': 'Line chart: median triage time falling over ten weeks.',
 'mobile': 'Mobile review queue: five stacked cards and a primary action.',
}

def img(key, alt=None, cls=''):
    a = IMG_ALT.get(key, '') if alt is None else alt
    return f'<img src="{IMG[key]}" alt="{a}" width="1600" height="1000" loading="lazy" decoding="async"{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>'

def frames(html, wide=1024, narrow=375, wl=None, nl=None):
    wl = wl or f'Wide container · {wide}px'
    nl = nl or f'Narrow container · {narrow}px'
    return ('<div class="pm-spec__frames">'
            f'<div class="pm-spec__frame"><span class="pm-spec__cap">{wl}</span><div class="pm-spec__viewport pm-cq" style="width:{wide}px;max-width:100%">{html.replace("{V}", "w")}</div></div>'
            f'<div class="pm-spec__frame"><span class="pm-spec__cap">{nl}</span><div class="pm-spec__viewport pm-cq" style="width:{narrow}px;max-width:100%">{html.replace("{V}", "n")}</div></div>'
            '</div>')

def cell(inner, cap):
    return f'<div class="pm-spec__cell">{inner}<span class="pm-spec__cap">{cap}</span></div>'

def h(text):
    return f'<h2 class="pm-spec__h">{text}</h2>'


def showcase(img_key, title, sub, badges, eyebrow='', state='', href='#c', alt='', more='Read case study'):
    """Card --showcase markup (v1.8). Same markup full-width or two-up: the card lays itself out by its own width."""
    b = ''.join(f'<li class="pm-badge">{x}</li>' for x in badges)
    return (f'<article class="pm-card pm-card--showcase{state}"><div class="pm-card__layout"><div class="pm-card__copy">'
            + (f'<p class="pm-card__eyebrow">{eyebrow}</p>' if eyebrow else '') +
            f'<h3 class="pm-card__title"><a href="{href}">{title}</a></h3>'
            + (f'<p class="pm-card__sub">{sub}</p>' if sub else '') +
            (f'<ul class="pm-card__meta" aria-label="Disciplines">{b}</ul>' if b else '') +
            f'<span class="pm-card__more" aria-hidden="true">{more}{I["arrow"]}</span></div>'
            f'<div class="pm-card__shot"><img src="{IMG[img_key]}" alt="{alt}" width="1600" height="1000" loading="lazy"></div></div></article>')
