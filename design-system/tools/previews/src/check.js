(function(){
  function rgb(el, v){ var s=document.createElement('span'); s.style.color='var('+v+')'; el.appendChild(s); var c=getComputedStyle(s).color; s.remove(); var m=(c.match(/[\d.]+/g)||[0,0,0]).map(Number); var a=m.length>3?m[3]:1; return m.slice(0,3).map(function(x){return a*x+(1-a)*255;}); }
  function lum(c){ c=c.map(function(x){x/=255; return x<=0.04045?x/12.92:Math.pow((x+0.055)/1.055,2.4);}); return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]; }
  function ratio(a,b){ var x=lum(a), y=lum(b); return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05); }
  window.pmCheck=function(){ document.querySelectorAll('[data-fg]').forEach(function(el){
    var r=ratio(rgb(el, el.dataset.fg), rgb(el, el.dataset.bg)), min=parseFloat(el.dataset.min||'4.5');
    var deco=el.hasAttribute('data-deco');
    el.textContent=r.toFixed(2)+':1'+(deco?' · decorative':'');
    el.className=deco?'pm-ratio':(r>=min?'pm-ratio pm-pass':'pm-fail');
    el.setAttribute('title', el.dataset.fg+' on '+el.dataset.bg+' (needs '+min+':1)');
  }); };
  pmCheck();
  if (document.fonts) document.fonts.ready.then(function(){ window.pmAfterFonts && pmAfterFonts(); });
  new MutationObserver(function(){ pmCheck(); }).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme','style','class']});
})();
