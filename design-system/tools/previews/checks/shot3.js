const {chromium}=require('playwright');
const names=process.argv.slice(2);
(async()=>{const b=await chromium.launch();
for (const spec of names){ const [n,w]=spec.split(':');
 const p=await b.newPage({viewport:{width:+w||1100,height:900}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,120))});
 await p.goto('file://'+__dirname+'/../.local/'+n+'.html'); await p.waitForTimeout(1200);
 const r=await p.evaluate(()=>({h:document.documentElement.scrollHeight,sw:document.documentElement.scrollWidth,
   fails:[...document.querySelectorAll('.pm-fail')].map(e=>e.title+' '+e.textContent),
   over:[...document.querySelectorAll('.pm-spec__viewport *')].filter(e=>e.scrollWidth>e.clientWidth+1 && getComputedStyle(e).overflowX==='visible').length}));
 console.log(n,JSON.stringify(r),errs.join(' | '));
 await p.screenshot({path:__dirname+'/../.local/'+n+'.png',fullPage:true});
}
await b.close();})();
