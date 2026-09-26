// Theme switch for comparing looks. ?theme=editorial turns the editorial theme on
// (remembered per browser); ?theme=rose turns it off. See STYLE.md, Themes.
(function(){
  var q = null, t = null;
  try { q = new URLSearchParams(location.search).get('theme'); } catch(e){}
  try {
    if (q === 'rose') localStorage.removeItem('theme');
    else if (q) localStorage.setItem('theme', q);
    t = q || localStorage.getItem('theme');
  } catch(e){ t = q; }
  if (t !== 'editorial') return;
  document.documentElement.setAttribute('data-theme', 'editorial');
  var f = document.createElement('link');
  f.rel = 'stylesheet';
  f.href = 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap';
  document.head.appendChild(f);
})();
