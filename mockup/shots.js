// Gera todas as imagens em ../imagens. Uso: node shots.js
const { chromium } = require('playwright');
const path = require('path');
const D = path.join(__dirname, '..', 'imagens') + '/';
const U = p => 'file://' + path.join(__dirname, p);
const DESK = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
const MOB = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true };

async function open(b, page, opts) {
  const p = await b.newPage(opts);
  await p.goto(U(page), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  return p;
}
async function at(p, sel, out, offset = 0) {
  await p.evaluate(([s, o]) => { const e = document.querySelector(s); window.scrollTo(0, e.getBoundingClientRect().top + scrollY + o); }, [sel, offset]);
  await p.waitForTimeout(120);
  await p.screenshot({ path: D + out + '.png' });
}
async function full(p, out) {
  await p.evaluate(() => { window.scrollTo(0, 0); const f = document.querySelector('.wafab'); if (f) f.style.display = 'none'; const s = document.querySelector('.sticky-buy'); if (s) s.style.position = 'static'; });
  await p.screenshot({ path: D + out + '.png', fullPage: true });
}

(async () => {
  const b = await chromium.launch();
  for (const [dev, o] of [['desktop', DESK], ['mobile', MOB]]) {
    // home
    let p = await open(b, 'index.html', o);
    await p.screenshot({ path: D + `${dev}-inicio.png` });
    const secs = ['.products', '.festa', '.cons', '.info', '.visit'];
    for (let i = 0; i < secs.length; i++) await at(p, secs[i], `${dev}-secao-${i + 1}`);
    await at(p, '.vip', `${dev}-home-grupo-vip`, dev == 'desktop' ? -420 : -120);
    await at(p, '.cons', `${dev}-home-consultoras`);
    await at(p, '.fb', `${dev}-home-feedbacks`);
    await full(p, `${dev}-pagina-completa`);
    // internas
    for (const [pg, name] of [['produto.html', 'produto'], ['sacola.html', 'sacola'], ['categoria.html', 'categoria'], ['painel.html', 'painel']]) {
      p = await open(b, pg, o); await p.screenshot({ path: D + `${dev}-${name}.png` });
    }
    p = await open(b, 'produto.html', o); await at(p, '.look', `${dev}-produto-look`); await full(p, `${dev}-produto-pagina-completa`);
    p = await open(b, 'agendar.html', o);
    if (dev == 'mobile') await at(p, '.ag-form', 'mobile-agendar', -16); else await p.screenshot({ path: D + 'desktop-agendar.png' });
  }
  let p = await open(b, 'categoria-filtros.html', MOB); await p.screenshot({ path: D + 'mobile-categoria-filtros.png' });
  p = await open(b, 'whatsapp.html', MOB); await p.screenshot({ path: D + 'mobile-whatsapp.png' });
  // slides
  const slides = ['capa', 'desktop-telas', 'mobile-telas', 'home-novidades', 'produto', 'fluxo-whatsapp', 'categoria', 'agendamento', 'painel', 'pacotes'];
  for (const f of slides) {
    const s = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2 });
    await s.goto(U('apresentacao.html') + '#' + f, { waitUntil: 'networkidle' }); await s.evaluate(() => document.fonts.ready); await s.waitForTimeout(300);
    await s.screenshot({ path: D + `apresentacao-${String(slides.indexOf(f) + 1).padStart(2, '0')}-${f}.png` });
  }
  await b.close();
})();
