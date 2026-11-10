const {chromium}=require('playwright');
const names=process.argv.slice(2);
(async()=>{const b=await chromium.launch();
for (const spec of names){const [n,w]=spec.split(':');
 const p=await b.newPage({viewport:{width:+w||1100,height:900}});
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+__dirname+'/../.local/'+n+'.html');await p.waitForTimeout(1000);
 const r=await p.evaluate(()=>{
  const MOL='.pm-card,.pm-panel,.pm-topnav,.pm-sidenav,.pm-toc,.pm-video,.pm-lightbox,.pm-frame,.pm-thumbs,[role=toolbar],.pm-status-message,.pm-tooltip-anchor,.pm-spec__row,.pm-card__meta,.pm-topnav__actions,.pm-video__controls,.pm-lightbox__bar';
  const ATOM='button,a,input,.pm-badge,.pm-status,.pm-thumb,.pm-media,.pm-card__eyebrow,.pm-card__summary,.pm-card__cta,.pm-panel__title,.pm-video__time,.pm-lightbox__count,.pm-lightbox__caption,.pm-frame__caption';
  const OK='.pm-frame__expand,.pm-frame__marker,.pm-video__big-play,.pm-thumb__check,.pm-video__controls,.pm-video__controls *,.pm-sr,.pm-tooltip';
  const atoms=[...document.querySelectorAll(ATOM)].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&getComputedStyle(e).visibility!=='hidden';});
  const out=[];
  function ring(e){const cs=getComputedStyle(e);if(cs.outlineStyle==='none'||!e.classList.contains('is-focus'))return null;const ow=parseFloat(cs.outlineWidth),oo=parseFloat(cs.outlineOffset);const d=ow+oo;if(d<=0)return null;const r=e.getBoundingClientRect();return {left:r.left-d,top:r.top-d,right:r.right+d,bottom:r.bottom+d};}
  for(let i=0;i<atoms.length;i++)for(let j=0;j<atoms.length;j++){if(i===j)continue;const a=atoms[i],c=atoms[j];
    if(a.contains(c)||c.contains(a))continue;
    const ma=a.parentElement.closest(MOL),mc=c.parentElement.closest(MOL);if(!ma||ma!==mc)continue;
    const okA=a.matches(OK)||a.closest('.pm-video'), okC=c.matches(OK)||c.closest('.pm-video'); 
    const rb=c.getBoundingClientRect();
    const boxes=[[a.getBoundingClientRect(),'box']]; const rr=ring(a); if(rr)boxes.push([rr,'focus-ring']);
    for(const [ra,kind] of boxes){ if(kind==='box'&&(okA||okC||j<i))continue;
      const x=Math.min(ra.right,rb.right)-Math.max(ra.left,rb.left), y=Math.min(ra.bottom,rb.bottom)-Math.max(ra.top,rb.top);
      if(x>1&&y>1) out.push(kind+': '+(a.className||a.tagName).toString().slice(0,40)+' ⟂ '+(c.className||c.tagName).toString().slice(0,40)+' '+Math.round(x)+'x'+Math.round(y));}}
  return [...new Set(out)];});
 console.log(n, errs.join('|'), r.length? '\n  '+r.slice(0,12).join('\n  '):'no overlaps');
}
await b.close();})();
