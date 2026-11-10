const {chromium}=require('playwright');
const names=process.argv.slice(2);
(async()=>{const b=await chromium.launch();
for (const spec of names){const [n,w]=spec.split(':');
 const p=await b.newPage({viewport:{width:+w||1100,height:900}});
 await p.goto('file://'+__dirname+'/../.local/'+n+'.html');await p.waitForTimeout(1500);
 const r=await p.evaluate(()=>{
  const HOST='.pm-choice,.pm-btn,.pm-status,.pm-badge,.pm-field__error,.pm-link,.pm-sidenav__item,.pm-panel__title,.pm-panel__toggle,.pm-tabs__tab,.pm-status-message,.pm-topnav__item,.pm-media__fallback,.pm-toc__item';
  const icons=[...document.querySelectorAll('svg.pm-icon, svg.pm-status__icon, .pm-choice > input, .pm-tabs__count, .pm-sidenav__count, .pm-toc__num')];
  const out=[]; let n=0;
  for(const ic of icons){const ir=ic.getBoundingClientRect(); if(!ir.width||!ir.height) continue;
    const host=ic.closest(HOST); if(!host) continue; if(host.matches('.pm-media__fallback')) continue;
    const tw=document.createTreeWalker(host,NodeFilter.SHOW_TEXT,{acceptNode:t=>t.textContent.trim()&&!ic.contains(t)&&!t.parentElement.closest('.pm-sr,.pm-choice__desc,.pm-status__desc,.pm-tabs__count,.pm-sidenav__count,.pm-toc__num')&&!(ic.contains&&false)?1:3});
    let t=tw.nextNode(); if(ic.matches('.pm-tabs__count,.pm-sidenav__count,.pm-toc__num')){ /* compare count to label text */ }
    if(!t) continue;
    const rg=document.createRange(); if(ic.closest('.pm-link')){rg.selectNodeContents(host);} else rg.selectNodeContents(t); const ic_c=ir.top+ir.height/2; const rs=[...rg.getClientRects()].filter(x=>x.height>0); if(!rs.length) continue; const lr=ic.closest('.pm-link')?rs.reduce((a,c)=>Math.abs(c.top+c.height/2-ic_c)<Math.abs(a.top+a.height/2-ic_c)?c:a):rs[0];
    // first line box of the text's element (line-height), not glyph box
    const el=t.parentElement, cs=getComputedStyle(el); const lh=parseFloat(cs.lineHeight)||lr.height;
    const lineCenter=lr.top+lr.height/2; // content box centre of first line
    const d=(ir.top+ir.height/2)-lineCenter; n++;
    if(Math.abs(d)>1.01) out.push((ic.getAttribute('class')||ic.tagName)+' in '+host.className.split(' ')[0]+' “'+t.textContent.trim().slice(0,18)+'” off by '+d.toFixed(1)+'px');
  }
  return {n,out:[...new Set(out)]};});
 console.log(n,'checked',r.n, r.out.length? '\n  '+r.out.slice(0,15).join('\n  '):'all centred within 1px');
}
await b.close();})();
