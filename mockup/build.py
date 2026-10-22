"""Gera as páginas internas do mockup reaproveitando cabeçalho e rodapé do index.html.

Uso: python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
index = (ROOT / 'index.html').read_text()
HEAD = index[:index.index('</header>') + len('</header>')]
HEAD = HEAD.replace('<link rel="stylesheet" href="css/site.css">',
                    '<link rel="stylesheet" href="css/site.css">\n<link rel="stylesheet" href="css/pages.css">')
FOOT = index[index.index('<footer>'):]
HEART = '<svg class="ico" viewBox="0 0 24 24"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/></svg>'
WA = '<svg class="wa-i" viewBox="0 0 24 24"><use href="#wa"/></svg>'


def card(img, name, price, pix, badge='', badge_cls='', sw=(), extra=''):
    b = f'<span class="badge {badge_cls}">{badge}</span>' if badge else ''
    s = ''.join(f'<i style="background:{c}"></i>' for c in sw)
    return (f'<div class="card"><div class="ph"><img src="img/{img}.jpg">{b}<span class="fav">{HEART}</span>{extra}</div>'
            f'<h3>{name}</h3><div class="price"><b>{price}</b></div><div class="pix">{pix}</div>'
            f'<div class="sw">{s}</div></div>')


def page(name, title, body, body_cls='', with_footer=True):
    html = HEAD.replace('<title>Urze | Exclusiva pra você — Recife</title>', f'<title>{title} | Urze</title>')
    html = html.replace('<body>', f'<body class="{body_cls}">')
    html += '\n' + body + '\n'
    html += FOOT if with_footer else '</body>\n</html>\n'
    (ROOT / name).write_text(html)


# ---------------------------------------------------------------- produto + sacola
SIZES = '''
<div class="opt-h"><span>Tamanho: <b>M</b></span><a href="#" class="u"><svg class="ico" viewBox="0 0 24 24"><path d="M3 8h18v8H3zM7 8v3M11 8v4M15 8v3M19 8v4"/></svg>Guia de medidas</a></div>
<div class="sizes"><span>P</span><span class="on">M</span><span class="out">G</span><span>GG</span></div>
<div class="notify"><svg class="ico" viewBox="0 0 24 24"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg><div><b>G esgotado</b><span>Avise-me pelo WhatsApp quando voltar</span></div><a href="#">Avise-me</a></div>
<div class="fit"><svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/></svg>Veste justo no busto. A Amanda (1,65m) usa M.</div>
'''

produto_body = f'''
<div class="wrap crumbs">Início <i>/</i> Macacões <i>/</i> <b>Macacão Gabriela</b></div>
<section class="pdp">
  <div class="wrap pdp-grid">
    <div class="gallery">
      <div class="thumbs">
        <div class="on"><img src="img/macacao-gabriela.jpg"></div>
        <div><img src="img/gabriela-2.jpg"></div>
        <div><img src="img/macacao-gabriela.jpg" style="transform:scale(2);transform-origin:50% 30%"></div>
        <div class="vid"><img src="img/gabriela-2.jpg"><span>▶</span></div>
      </div>
      <div class="main">
        <img src="img/macacao-gabriela.jpg">
        <span class="badge g">Mais vendido</span>
        <span class="fav">{HEART}</span>
        <div class="reel"><div class="reel-ph"><img src="img/gabriela-2.jpg"><span>▶</span></div><div><b>Ver no corpo</b><small>Vídeo de 15s · provador Urze</small></div></div>
        <div class="gdots"><i class="on"></i><i></i><i></i><i></i></div>
      </div>
    </div>
    <div class="buy">
      <div class="eyebrow">Coleção nova · Macacões</div>
      <h1>Macacão Gabriela</h1>
      <div class="rev"><span class="stars">★★★★★</span><a href="#">48 avaliações</a><span class="views">🔥 23 pessoas viram hoje</span></div>
      <div class="pp"><b>R$ 159,99</b><s>R$ 189,99</s><span class="off">-16%</span></div>
      <div class="pix-line"><span class="pix-tag">PIX</span><b>R$ 151,99</b> à vista no Pix, sem taxas · ou 3x de R$ 53,33</div>
      <div class="opt-h"><span>Cor: <b>Verde Sálvia</b></span></div>
      <div class="colors"><span class="on" style="background:#8FB79A"></span><span style="background:#C8D86A"></span><span style="background:#1E2433"></span><span style="background:#E9E1D2"></span></div>
      {SIZES}
      <div class="actions">
        <div class="qty"><span>−</span><b>1</b><span>+</span></div>
        <a class="btn btn-dark" href="#">Adicionar à sacola</a>
      </div>
      <a class="btn-wa" href="#">{WA}Comprar pelo WhatsApp</a>
      <div class="with"><img src="img/amanda.jpg"><div>Atendimento com <b>Amanda</b> <span class="on-dot">● online</span><small>Responde em média em 5 min · <a href="#" class="u">trocar consultora</a></small></div></div>
      <div class="perks">
        <div><svg class="ico" viewBox="0 0 24 24"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.5"/><circle cx="17" cy="17.5" r="1.5"/></svg><span><b>Entrega hoje</b>em Recife, pedindo até 15h</span></div>
        <div><svg class="ico" viewBox="0 0 24 24"><path d="M3 10l9-6 9 6v10H3zM9 20v-6h6v6"/></svg><span><b>Retire grátis</b>na loja do Coqueiral</span></div>
        <div><svg class="ico" viewBox="0 0 24 24"><path d="M21 12a9 9 0 1 1-3-6.7M21 4v5h-5"/></svg><span><b>Troca em 7 dias</b>com etiqueta na peça</span></div>
      </div>
      <div class="acc">
        <details open><summary>Descrição</summary><p>Macacão de alça frente única com amarração no pescoço, cintura marcada e pantalona fluida. Leve, não amassa e vai do almoço de domingo ao jantar.</p></details>
        <details><summary>Composição e cuidados</summary></details>
        <details><summary>Medidas da peça</summary></details>
      </div>
    </div>
  </div>
</section>

<section class="look">
  <div class="wrap">
    <div class="sec-head"><div><div class="eyebrow">Monte com a consultora</div><h2 class="title">Complete o <em>look</em></h2></div></div>
    <div class="look-row">
      <div class="look-main"><img src="img/gabriela-2.jpg"><span class="pin" style="left:44%;top:46%">1</span><span class="pin" style="left:22%;top:20%">2</span></div>
      <div class="look-items">
        <label class="li"><span class="ck on">✓</span><img src="img/macacao-gabriela.jpg"><div><b>Macacão Gabriela</b><small>Verde Sálvia · M</small></div><em>R$ 159,99</em></label>
        <label class="li"><span class="ck on">✓</span><span class="zoom"><img src="img/conjunto-marrom.jpg" style="transform:scale(3.2);transform-origin:22% 72%"></span><div><b>Bolsa Palha Mini</b><small>Natural · Único</small></div><em>R$ 89,99</em></label>
        <label class="li"><span class="ck">✓</span><span class="zoom"><img src="img/macacao-gabriela.jpg" style="transform:scale(4.5);transform-origin:64% 50%"></span><div><b>Bracelete Dourado</b><small>Dourado · Único</small></div><em>R$ 49,99</em></label>
        <div class="look-tot"><div><small>2 peças selecionadas</small><b>R$ 249,98</b><span>R$ 237,48 no Pix</span></div><a class="btn btn-dark" href="#">Levar o look</a></div>
      </div>
    </div>
  </div>
</section>

<section class="products" style="padding-top:20px">
  <div class="wrap">
    <div class="sec-head"><div><div class="eyebrow">Combina com você</div><h2 class="title">Você também vai <em>amar</em></h2></div><a class="more" href="#">Ver macacões</a></div>
    <div class="grid">
      {card('macacao-preto','Macacão Ágatha','R$ 139,99','R$ 132,99 no Pix','Novo','',('#1E2433','#8FB79A','#E9E1D2'))}
      {card('vestido-verde','Vestido Lima Frente Única','R$ 149,99','R$ 142,49 no Pix','','',('#C8D86A',))}
      {card('conjunto-azul','Conjunto Capa Céu','R$ 179,99','R$ 170,99 no Pix','','',('#7FB1E3','#F2EDE4'))}
      {card('conjunto-marrom','Conjunto Linho Cacau','R$ 169,99','R$ 161,49 no Pix','Novo','',('#4A2A22',))}
    </div>
  </div>
</section>

<div class="sticky-buy"><div><small>Macacão Gabriela · M</small><b>R$ 151,99 <span>no Pix</span></b></div><a class="btn-wa" href="#">{WA}Comprar</a></div>

<div class="overlay"></div>
<aside class="drawer">
  <div class="dr-h"><h3>Sua sacola <span>(2)</span></h3><span class="x">✕</span></div>
  <div class="dr-ok">✓ Macacão Gabriela adicionado</div>
  <div class="dr-items">
    <div class="it"><img src="img/macacao-gabriela.jpg"><div class="it-tx"><b>Macacão Gabriela</b><small>Verde Sálvia · M</small><div class="qty sm"><span>−</span><b>1</b><span>+</span></div></div><div class="it-p"><b>R$ 159,99</b><a href="#">Remover</a></div></div>
    <div class="it"><img src="img/tomara-que-caia.jpg"><div class="it-tx"><b>Top Animal Print</b><small>Onça · P</small><div class="qty sm"><span>−</span><b>1</b><span>+</span></div></div><div class="it-p"><b>R$ 89,99</b><a href="#">Remover</a></div></div>
  </div>
  <div class="dr-sec">
    <div class="dr-l">Como quer receber?</div>
    <div class="ship">
      <label class="on"><span class="rd"></span><div><b>Motoboy hoje</b><small>Coqueiral → Boa Viagem</small></div><em>R$ 12,00</em></label>
      <label><span class="rd"></span><div><b>Retirar na loja</b><small>R. Guanabara, 34 · a partir das 14h</small></div><em class="free">Grátis</em></label>
    </div>
    <div class="cep"><input value="Boa Viagem, Recife"><a href="#">Alterar</a></div>
  </div>
  <div class="dr-sec">
    <div class="dr-l">Sua consultora</div>
    <div class="who"><img src="img/amanda.jpg"><div><b>Amanda</b><small>● online · responde em ~5 min</small></div><a href="#" class="u">Trocar</a></div>
  </div>
  <div class="dr-sum">
    <div><span>Subtotal</span><span>R$ 249,98</span></div>
    <div><span>Entrega</span><span>R$ 12,00</span></div>
    <div class="pixd"><span>Desconto Pix (5%)</span><span>− R$ 12,50</span></div>
    <div class="tot"><span>Total no Pix</span><b>R$ 249,48</b></div>
  </div>
  <a class="btn-wa big" href="#">{WA}Enviar pedido para a Amanda</a>
  <p class="dr-note">Você finaliza o pagamento com a consultora pelo WhatsApp: Pix, cartão ou link.</p>
</aside>
'''
page('produto.html', 'Macacão Gabriela', produto_body, 'pg-produto')
page('sacola.html', 'Sacola', produto_body, 'pg-produto open-drawer')

# ---------------------------------------------------------------- whatsapp (mobile)
whats = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>WhatsApp | Urze</title><link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500&display=swap" rel="stylesheet"><link rel="stylesheet" href="css/pages.css"></head>
<body class="wa-body">
<div class="wa-top"><span>‹</span><img src="img/amanda.jpg"><div><b>Amanda · Urze</b><small>online</small></div><span class="wa-ic">📹</span><span class="wa-ic">📞</span></div>
<div class="wa-chat">
  <div class="wa-day">HOJE</div>
  <div class="wa-msg me">
    <div class="wa-card"><img src="img/macacao-gabriela.jpg"><div><b>Pedido #1048 · urze.com.br</b><small>2 peças · R$ 249,48 no Pix</small></div></div>
    Oi, Amanda! 💛 Vim pelo site e quero fechar este pedido:<br><br>
    🛍️ <b>1x Macacão Gabriela</b> · Verde Sálvia · M · R$ 159,99<br>
    🛍️ <b>1x Top Animal Print</b> · Onça · P · R$ 89,99<br><br>
    🛵 Entrega: Motoboy hoje · Boa Viagem (R$ 12,00)<br>
    💳 Pagamento: Pix (5% off)<br>
    <b>Total: R$ 249,48</b>
    <span class="wa-t">14:32 ✓✓</span>
  </div>
  <div class="wa-msg">Oiii! Que escolha linda 😍 Já separei suas peças aqui na loja. Segue a chave Pix pra confirmar 👇<span class="wa-t">14:34</span></div>
  <div class="wa-msg pix"><div class="pix-b"><span class="pix-tag">PIX</span><div><b>Chave CNPJ · Urze Exclusiva</b><small>00.000.000/0001-00</small></div><span class="cp">Copiar</span></div>Assim que cair, o motoboy sai pra você! 🛵<span class="wa-t">14:34</span></div>
  <div class="wa-msg me">Perfeito, pagando agora! 🙌<span class="wa-t">14:35 ✓✓</span></div>
</div>
<div class="wa-bar"><div>Mensagem</div><span>🎤</span></div>
</body></html>
'''
(ROOT / 'whatsapp.html').write_text(whats)

# ---------------------------------------------------------------- categoria
filters = '''
<div class="f-blk"><h4>Categoria</h4>
  <label class="cb on"><i>✓</i>Macacões <em>18</em></label><label class="cb"><i></i>Vestidos <em>42</em></label><label class="cb"><i></i>Conjuntos <em>27</em></label><label class="cb"><i></i>Calças e saias <em>31</em></label></div>
<div class="f-blk"><h4>Tamanho</h4><div class="chips"><span>PP</span><span>P</span><span class="on">M</span><span>G</span><span>GG</span></div></div>
<div class="f-blk"><h4>Cor</h4><div class="swatches"><span style="background:#111"></span><span style="background:#F2EDE4"></span><span class="on" style="background:#8FB79A"></span><span style="background:#4A2A22"></span><span style="background:#7FB1E3"></span><span style="background:#C8D86A"></span><span style="background:#D8C3A5"></span><span style="background:#B3201F"></span></div></div>
<div class="f-blk"><h4>Preço</h4><div class="range"><i style="left:12%"></i><i style="left:70%"></i><b style="left:12%;right:30%"></b></div><div class="range-v"><span>R$ 60</span><span>R$ 200</span></div></div>
<div class="f-blk"><h4>Ocasião</h4><div class="chips"><span>Dia a dia</span><span class="on">Almoço</span><span>Trabalho</span><span>Festa</span><span>Praia</span></div></div>
<label class="cb sw-on"><span class="tg on"></span>Só peças com entrega hoje</label>
'''
out_card = card('festa-costas', 'Vestido Cetim Champagne', 'R$ 219,99', 'R$ 208,99 no Pix', '', '', (),
                '<div class="soldout"><b>Esgotado no M</b><a href="#">Avise-me quando chegar</a></div>')
cat_body = f'''
<div class="cat-hero"><div class="wrap"><div class="crumbs" style="padding:0 0 10px">Início <i>/</i> <b>Macacões</b></div><h1 class="title">Macacões</h1><p>Peça única, look pronto. Do linho ao cetim, para o dia a dia e para a festa.</p></div></div>
<section class="plp"><div class="wrap plp-grid">
  <aside class="filters"><div class="f-top"><b>Filtrar</b><a href="#" class="u">Limpar</a></div>{filters}</aside>
  <div>
    <div class="plp-bar"><span><b>12</b> peças encontradas</span>
      <div class="act-chips"><span>Macacões ✕</span><span>Tamanho M ✕</span><span>Verde ✕</span><span>Almoço ✕</span></div>
      <div class="sort">Ordenar: <b>Mais vendidos ▾</b></div>
      <a class="m-filter" href="#"><svg class="ico" viewBox="0 0 24 24"><path d="M4 6h16M7 12h10M10 18h4"/></svg>Filtrar (4)</a><a class="m-filter" href="#">Ordenar ▾</a>
    </div>
    <div class="grid g3">
      {card('macacao-gabriela','Macacão Gabriela','R$ 159,99','R$ 151,99 no Pix','Mais vendido','g',('#8FB79A','#C8D86A'))}
      {card('macacao-preto','Macacão Ágatha','R$ 139,99','R$ 132,99 no Pix','Novo','',('#1E2433','#8FB79A','#E9E1D2'))}
      {card('conjunto-verde','Macaquinho Menta','R$ 119,99','R$ 113,99 no Pix','Entrega hoje','',('#A8D5A0',))}
      {out_card}
      {card('gabriela-2','Macacão Gabriela Longo','R$ 169,99','R$ 161,49 no Pix','','',('#8FB79A',))}
      {card('conjunto-cinza','Macacão Grafite Amplo','R$ 149,99','R$ 142,49 no Pix','Novo','',('#5A5D63','#111'))}
    </div>
    <div class="more-btn"><span>Você viu 6 de 12 peças</span><div class="bar"><i style="width:50%"></i></div><a class="btn btn-line" href="#">Carregar mais</a></div>
  </div>
</div></section>

<div class="overlay"></div>
<div class="sheet">
  <div class="grab"></div>
  <div class="sh-h"><b>Filtrar</b><a href="#" class="u">Limpar tudo</a></div>
  <div class="sh-body">{filters}</div>
  <div class="sh-f"><a class="btn btn-dark" href="#">Ver 12 peças</a></div>
</div>
'''
page('categoria.html', 'Macacões', cat_body, 'pg-cat')
page('categoria-filtros.html', 'Macacões', cat_body, 'pg-cat open-sheet')

# ---------------------------------------------------------------- agendar
days = [('Qui', '23', ''), ('Sex', '24', 'on'), ('Sáb', '25', ''), ('Seg', '27', ''), ('Ter', '28', ''), ('Qua', '29', '')]
slots = [('10:00', ''), ('11:00', ''), ('13:00', 'off'), ('14:00', ''), ('15:00', 'on'), ('16:00', ''), ('17:00', 'off'), ('18:00', '')]
ag_body = f'''
<section class="ag"><div class="wrap ag-grid">
  <div class="ag-side">
    <div class="ag-img"><img src="img/loja.jpg"><div class="ag-badge">☕ Café por nossa conta</div></div>
    <div class="eyebrow" style="margin-top:28px">Provador reservado</div>
    <h1 class="title">Agende sua <em>visita</em></h1>
    <p>Reserve um horário e encontre suas peças separadas no provador, no seu tamanho, com uma consultora só pra você.</p>
    <ul class="ag-list"><li>Peças separadas antes de você chegar</li><li>Atendimento sem fila</li><li>Sem compromisso de compra</li></ul>
  </div>
  <div class="ag-form">
    <div class="step-h"><span class="n">1</span>Escolha o dia</div>
    <div class="days">{''.join(f'<span class="{c}"><small>{d}</small><b>{n}</b><small>out</small></span>' for d, n, c in days)}</div>
    <div class="step-h"><span class="n">2</span>Horário</div>
    <div class="slots">{''.join(f'<span class="{c}">{t}</span>' for t, c in slots)}</div>
    <div class="step-h"><span class="n">3</span>O que você quer provar?</div>
    <div class="chips big"><span class="on">Linha Festa</span><span>Coleção nova</span><span class="on">Jeans</span><span>Retirar pedido</span></div>
    <div class="step-h"><span class="n">4</span>Seus dados</div>
    <div class="inputs"><input value="Mariana Souza"><input value="(81) 9 9876-5432"></div>
    <div class="ag-sum"><div><small>Sexta, 24 de outubro · 15:00</small><b>Com a consultora Amanda</b></div><span>R. Guanabara, 34 · Coqueiral</span></div>
    <a class="btn-wa big" href="#">{WA}Confirmar pelo WhatsApp</a>
    <p class="dr-note">Você recebe um lembrete no dia anterior. Pode remarcar a qualquer momento.</p>
  </div>
</div></section>
'''
page('agendar.html', 'Agende sua visita', ag_body, 'pg-ag')

# ---------------------------------------------------------------- painel (admin)
bars = [('Seg', 11), ('Ter', 9), ('Qua', 14), ('Qui', 12), ('Sex', 19), ('Sáb', 24), ('Hoje', 18)]
mx = 24
bar_html = ''.join(
    f'<div class="b{" now" if d == "Hoje" else ""}"><em>{v}</em><i style="height:{v / mx * 100:.0f}%"></i><span>{d}</span></div>'
    for d, v in bars)
rows = [
    ('macacao-gabriela', 'Macacão Gabriela', 'Macacões', 'R$ 159,99', [('P', 3), ('M', 5), ('G', 0), ('GG', 2)], True, 'Mais vendido'),
    ('macacao-preto', 'Macacão Ágatha', 'Macacões', 'R$ 139,99', [('P', 4), ('M', 2), ('G', 3), ('GG', 1)], True, ''),
    ('vestido-marrom', 'Vestido Sereia Canelado', 'Vestidos', 'R$ 119,99', [('P', 1), ('M', 0), ('G', 2), ('GG', 0)], True, 'Estoque baixo'),
    ('festa-costas', 'Vestido Cetim Champagne', 'Linha Festa', 'R$ 219,99', [('P', 0), ('M', 0), ('G', 0), ('GG', 0)], False, 'Esgotado · 14 avisos'),
    ('conjunto-azul', 'Conjunto Capa Céu', 'Conjuntos', 'R$ 179,99', [('P', 2), ('M', 4), ('G', 3), ('GG', 2)], True, ''),
]


def row(r):
    img, nm, cat, pr, st, on, note = r
    chips = ''.join(f'<span class="{"z" if q == 0 else ("lo" if q < 2 else "")}">{s}<b>{q}</b></span>' for s, q in st)
    tag = f'<small class="note{" bad" if "Esgot" in note or "baixo" in note else ""}">{note}</small>' if note else ''
    return (f'<tr><td><div class="pn"><img src="img/{img}.jpg"><div><b>{nm}</b>{tag}</div></div></td><td>{cat}</td><td>{pr}</td>'
            f'<td><div class="stk">{chips}</div></td><td><span class="tg{" on" if on else ""}"></span></td><td class="dots3">⋯</td></tr>')


painel_body = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Painel | Urze</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Jost:wght@300;400;500;600&family=Playfair+Display:ital,wght@1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css"><link rel="stylesheet" href="css/pages.css"></head>
<body class="adm">
{index[index.index('<svg width="0"'):index.index('</svg>', index.index('<symbol id="seal"')) + 6]}
<aside class="adm-side">
  <div class="brand"><svg><use href="#seal"/></svg><div class="wm">URZE<small>PAINEL DA LOJA</small></div></div>
  <nav>
    <a class="on">▦ <span>Visão geral</span></a><a>◱ <span>Peças</span><em>212</em></a><a>✉ <span>Pedidos WhatsApp</span><em class="hot">6</em></a><a>☕ <span>Agendamentos</span><em>3</em></a><a>♡ <span>Avise-me</span><em>27</em></a><a>✦ <span>Consultoras</span></a><a>☰ <span>Banners da home</span></a><a>★ <span>Feedbacks</span></a>
  </nav>
  <div class="adm-help">Dúvidas? Fale com o suporte <b>valdev</b></div>
</aside>
<main class="adm-main">
  <div class="adm-top"><div><small>Sexta, 24 de outubro</small><h1>Bom dia, Urze ✨</h1></div><div class="adm-act"><input placeholder="Buscar peça, pedido ou cliente…"><a class="btn btn-dark" href="#">+ Nova peça</a></div></div>
  <div class="kpis">
    <div class="kpi"><small>Pedidos pelo WhatsApp · hoje</small><b>18</b><span class="up">▲ 29% vs. sexta passada</span></div>
    <div class="kpi"><small>Visitas no site · hoje</small><b>1.240</b><span class="up">▲ 12%</span></div>
    <div class="kpi"><small>Visitas agendadas · semana</small><b>14</b><span>3 para hoje</span></div>
    <div class="kpi warn"><small>Peças esgotadas</small><b>9</b><span>27 clientes pediram aviso</span></div>
  </div>
  <div class="adm-row">
    <div class="panel"><div class="p-h"><b>Pedidos pelo WhatsApp</b><span>Últimos 7 dias</span></div><div class="bars">{bar_html}</div></div>
    <div class="panel"><div class="p-h"><b>Mais vistas hoje</b><span>Visualizações</span></div>
      <div class="top">
        <div><img src="img/macacao-gabriela.jpg"><span>Macacão Gabriela</span><b>412</b></div>
        <div><img src="img/festa-cetim.jpg"><span>Vestido Cetim Capa</span><b>298</b></div>
        <div><img src="img/vestido-marrom.jpg"><span>Vestido Sereia</span><b>187</b></div>
        <div><img src="img/conjunto-azul.jpg"><span>Conjunto Capa Céu</span><b>140</b></div>
      </div></div>
  </div>
  <div class="panel">
    <div class="p-h"><b>Peças</b><div class="tabs sm"><a class="on">Todas</a><a>Estoque baixo</a><a>Esgotadas</a><a>Rascunhos</a></div></div>
    <table class="tbl"><thead><tr><th>Peça</th><th>Categoria</th><th>Preço</th><th>Estoque por tamanho</th><th>No site</th><th></th></tr></thead>
    <tbody>{''.join(row(r) for r in rows)}</tbody></table>
  </div>
</main>

<div class="adm-m">
  <div class="am-top"><span>‹</span><b>Nova peça</b><a>Salvar rascunho</a></div>
  <div class="am-body">
    <div class="up-row"><div class="up add">＋<small>Foto ou vídeo</small></div><div class="up"><img src="img/vestido-verde.jpg"><i>Capa</i></div><div class="up"><img src="img/vestido-verde.jpg" style="transform:scale(1.8);transform-origin:50% 30%"></div></div>
    <label class="fld"><span>Nome da peça</span><input value="Vestido Lima Frente Única"></label>
    <div class="two"><label class="fld"><span>Preço</span><input value="R$ 149,99"></label><label class="fld"><span>Preço no Pix</span><input value="R$ 142,49"></label></div>
    <label class="fld"><span>Categoria</span><input value="Vestidos  ▾"></label>
    <div class="fld"><span>Estoque por tamanho</span><div class="stk-ed"><div>P<b>2</b></div><div>M<b>4</b></div><div>G<b>3</b></div><div>GG<b>0</b></div></div></div>
    <div class="fld"><span>Cores</span><div class="swatches"><span class="on" style="background:#C8D86A"></span><span style="background:#8FB79A"></span><span class="add">＋</span></div></div>
    <label class="tgl"><span class="tg on"></span>Mostrar em “Novidades da semana”</label>
    <label class="tgl"><span class="tg on"></span>Avisar o Grupo VIP quando publicar</label>
  </div>
  <div class="am-foot"><a class="btn btn-dark" href="#">Publicar no site</a></div>
</div>
</body></html>
'''
(ROOT / 'painel.html').write_text(painel_body)
print('ok')
