// 2-step quote cards: one tap picks the job, step 2 takes postcode, name and mobile.
// Sample only: nothing is sent anywhere.
document.querySelectorAll('.qcard').forEach(card=>{
  const p1=card.querySelector('.p1'),p2=card.querySelector('.p2'),step=card.querySelector('.qstep'),bar=card.querySelector('.qbar i');
  const go=n=>{p1.hidden=n!==1;p2.hidden=n!==2;step.textContent=`Step ${n} of 2`;bar.style.width=n===1?'50%':'100%'};
  card.querySelectorAll('.opt').forEach(b=>b.addEventListener('click',()=>{
    card.querySelectorAll('.opt').forEach(o=>o.setAttribute('aria-pressed',o===b));
    card.querySelector('.ch').textContent=b.dataset.v;go(2);
    setTimeout(()=>p2.querySelector('input').focus({preventScroll:true}),60);
  }));
  card.querySelector('.back').addEventListener('click',()=>go(1));
  card.querySelector('form').addEventListener('submit',e=>{
    e.preventDefault();
    const name=p2.querySelectorAll('input')[1].value.trim().split(' ')[0];
    card.querySelector('.done').textContent=name?`Sample only: thanks ${name}, a real site would send this straight to the roofer.`:'Fill in your details to try it.';
  });
});
// count the trust numbers up when they scroll into view
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
if('IntersectionObserver' in window&&!reduce){
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;io.unobserve(e.target);
    const el=e.target,to=+el.dataset.to,from=to>1000?to-25:0,t0=performance.now();
    const step=t=>{const k=Math.min(1,(t-t0)/1100);el.textContent=Math.round(from+(to-from)*(1-Math.pow(1-k,3)));if(k<1)requestAnimationFrame(step)};
    requestAnimationFrame(step)}),{threshold:.6});
  document.querySelectorAll('.count').forEach(c=>io.observe(c));
}
