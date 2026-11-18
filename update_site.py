from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')
group='https://chat.whatsapp.com/ITpQTGPnrFE5r9HhYYKJb3?s=sh&amp;p=a&amp;iam=2&amp;fbclid=PAZXh0bgNhZW0CMTEAcGRvZgJzcnRjBmFwcF9pZA85MzY2MTk3NDMzOTI1NTkAAac4EAggZI5aPxnOSjI_tXvWgOeceVLbXbY1LUN9CbUP4-eRCtQkHRXfM4C-Kg_aem_RxnMKsu3LKcHNH5VFVqZAw'
# Match the supplied invite exactly apart from HTML escaping ampersands.
# Preserve original invite payload (corrected below from exact raw URL in user request).
group='https://chat.whatsapp.com/ITpQTGPnrFE5r9HhYYKJb3?s=sh&amp;p=a&amp;iam=2&amp;fbclid=PAZXh0bgNhZW0CMTEAcGRvZgJzcnRjBmFwcF9pZA85MzY2MTk3NDMzOTI0NTkAAac4EAggZI5aPxnOSjI_tXvWgOeceVLbXbY1LUN9CbUP4-eRCtQkHRXfM4C-Kg_aem_RxnMKsu3LKcHNH5VFVqZAw'

# Update search/social metadata for the campaign and broaden the product positioning.
s=s.replace('<title>Via Vest Moda | Atacado e Varejo em Manaus – AM</title>', '<title>Black Friday Via Vest | Moda Feminina, Vestidos, Atacado e Varejo</title>')
s=s.replace('Camisas, calças cargo, sarja e moda casual em atacado e varejo no bairro Flores, Manaus – AM. Grade completa para lojistas e peças avulsas para você. Atendimento direto no WhatsApp.', 'Black Friday Via Vest Moda em Manaus: vestidos e moda feminina, peças masculinas, atacado e varejo. Ganhe um brinde em compras a partir de R$ 400. Preços promocionais no dia pelo grupo WhatsApp.')
s=s.replace('<meta property="og:title" content="Via Vest Moda | Atacado e Varejo em Manaus – AM">', '<meta property="og:title" content="Black Friday Via Vest | Moda Feminina e Atacado em Manaus">')
s=s.replace('<meta property="og:description" content="Moda casual, calças cargo, sarja e camisas com preço de atacado para lojistas e varejo para você. Loja física no Flores, Manaus.">', '<meta property="og:description" content="Vestidos, moda feminina e masculina. Brinde em compras a partir de R$ 400. Preços promocionais no dia pelo grupo WhatsApp.">')
s=s.replace('<meta name="twitter:title" content="Via Vest Moda | Atacado e Varejo em Manaus">', '<meta name="twitter:title" content="Black Friday Via Vest | Moda Feminina e Atacado em Manaus">')
s=s.replace('<meta name="twitter:description" content="Atacado para lojistas, varejo para você. Moda casual em Manaus – AM.">', '<meta name="twitter:description" content="Brinde em compras a partir de R$ 400. Preços promocionais no dia pelo grupo WhatsApp. Moda feminina e masculina em Manaus.">')
s=s.replace('"description": "Loja de moda em atacado e varejo: camisas, calças cargo, sarja e moda casual em Manaus – AM.",','"description": "Black Friday, vestidos e moda feminina e masculina em atacado e varejo em Manaus – AM.",')

# Campaign announcement bar.
s=s.replace('''<div class="topbar">
  <span>
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>
    R. Visconde de Utinga, 620 — Flores, Manaus/AM
  </span>
  <i class="dot hide-sm"></i>
  <span class="hide-sm">Atacado &amp; Varejo · Atendimento no WhatsApp</span>
</div>''', f'''<div class="topbar topbar--bf">
  <span class="topbar__campaign">BLACK FRIDAY</span>
  <span class="hide-sm">Brinde em compras a partir de <strong>R$ 400</strong></span>
  <a href="{group}" target="_blank" rel="noopener">Preços promocionais no dia · Entre no grupo <span aria-hidden="true">↗</span></a>
</div>''')

# Header and mobile drawer promote the WhatsApp group.
s=re.sub(r'<a class="btn btn--wa" href="https://wa\.me/5592991193584\?text=Ol%C3%A1!%20Vim%20pelo%20site%20da%20Via%20Vest%20e%20quero%20saber%20mais%20sobre%20as%20pe%C3%A7as\." target="_blank" rel="noopener">(.*?)<span>WhatsApp</span>',
         lambda m: f'<a class="btn btn--wa" href="{group}" target="_blank" rel="noopener" aria-label="Entrar no grupo de ofertas Black Friday">{m.group(1)}<span>Ofertas BF</span>',s,count=1,flags=re.S)
s=s.replace('<a href="#catalogo">Vitrine <span>03</span></a>', '<a href="#catalogo">Vitrine <span>03</span></a>\n    <a href="#catalogo" data-filter-link="feminino">Moda feminina <span>04</span></a>')
s=s.replace('<a href="#como-comprar">Como comprar <span>04</span></a>', '<a href="#como-comprar">Como comprar <span>05</span></a>')
s=s.replace('<a href="#localizacao">Localização <span>05</span></a>', '<a href="#localizacao">Localização <span>06</span></a>')
# add a campaign join button to the drawer footer before phone small text
needle='''    <a class="btn btn--ghost btn--block" href="https://maps.google.com/?q=R.+Visconde+de+Utinga,+620+-+Flores,+Manaus+-+AM" target="_blank" rel="noopener">Ver rota até a loja</a>'''
s=s.replace(needle, f'''    <a class="btn btn--dark btn--block" href="{group}" target="_blank" rel="noopener">Entrar no grupo Black Friday</a>
'''+needle)

# Hero campaign and feminine collection positioning.
s=s.replace('<b>Novo</b> Coleção 2026 · Manaus/AM','<b>Black Friday</b> Moda feminina &amp; masculina · Manaus')
s=s.replace('Estilo de rua,<br>preço de <span class="serif">atacado</span>.','Black Friday<br>com muito <span class="serif">estilo</span>.')
s=s.replace('Camisas, calças cargo, sarja e peças casuais para quem <strong>revende</strong> e para quem <strong>veste</strong>. Grade completa no atacado e peças avulsas no varejo, no bairro Flores.','Vestidos, looks femininos e peças casuais para quem <strong>revende</strong> e para quem <strong>veste</strong>. Nas compras a partir de R$ 400, ganhe um brinde. Os preços promocionais serão divulgados no dia pelo nosso grupo no WhatsApp.')
s=s.replace('''          <a class="btn btn--wine" href="https://wa.me/5592991193584?text=Ol%C3%A1!%20Quero%20receber%20o%20cat%C3%A1logo%20com%20fotos%20e%20pre%C3%A7os%20de%20atacado." target="_blank" rel="noopener">''',f'''          <a class="btn btn--wine" href="{group}" target="_blank" rel="noopener">''',1)
s=s.replace('Catálogo no WhatsApp','Entrar no grupo Black Friday',1)
s=s.replace('Preço de atacado para lojistas','Preços promocionais no grupo WhatsApp')
s=s.replace('Venda avulsa no varejo','Moda feminina e vestidos')
s=s.replace('<img src="img/hero.webp" alt="Modelo vestindo camisa e calça cargo da Via Vest Moda"', '<img src="img/fem-blue-dress.webp" alt="Modelo usando vestido feminino azul estampado em uma área externa"')
s=s.replace('<b>Loja física no Flores</b>\n            <small>R. Visconde de Utinga, 620 — Manaus/AM</small>', '<b>Moda feminina em destaque</b>\n            <small>Vestidos, looks leves e novidades para a Black Friday</small>')

# Make marquee inclusive.
marquee_old='<span>Camisas</span><i>✦</i><span>Calças Cargo</span><i>✦</i><span>Sarja</span><i>✦</i><span>Camisetas</span><i>✦</i><span>Conjuntos</span><i>✦</i><span>Atacado</span><i>✦</i><span>Varejo</span><i>✦</i><span>Manaus</span><i>✦</i>'
marquee_new='<span>Vestidos</span><i>✦</i><span>Moda feminina</span><i>✦</i><span>Looks leves</span><i>✦</i><span>Calças Cargo</span><i>✦</i><span>Atacado</span><i>✦</i><span>Varejo</span><i>✦</i><span>Black Friday</span><i>✦</i><span>Manaus</span><i>✦</i>'
s=s.replace(marquee_old,marquee_new)

# Add high contrast campaign panel immediately after marquee.
marker='''  <!-- ================= MODALIDADES ================= -->'''
bf_section=f'''  <!-- ================= BLACK FRIDAY ================= -->
  <section class="bf-section" id="black-friday" aria-labelledby="bf-title">
    <div class="container">
      <div class="bf-card" data-reveal>
        <div class="bf-card__copy">
          <span class="bf-kicker"><span></span> BLACK FRIDAY VIA VEST</span>
          <h2 id="bf-title">Comprou <span>R$ 400</span> ou mais?<br><em>Tem brinde pra você.</em></h2>
          <p>Os preços promocionais serão divulgados no dia pelo nosso grupo no WhatsApp. Entre agora para acompanhar as ofertas e conferir as condições do brinde.</p>
          <a class="btn btn--bf" href="{group}" target="_blank" rel="noopener">
            Entrar no grupo de ofertas
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <small>Brinde em compras a partir de R$ 400. Consulte disponibilidade e regras no grupo.</small>
        </div>
        <div class="bf-card__stamp" aria-hidden="true"><span>BLACK</span><b>FRI</b><span>DAY · VV</span></div>
      </div>
    </div>
  </section>

'''
assert marker in s
s=s.replace(marker,bf_section+marker,1)

# Vitrine copy and feminine filter.
s=s.replace('<span class="eyebrow">Vitrine</span>\n          <h2>Peças que <span class="serif">giram</span> rápido</h2>\n          <p>Uma amostra do que sai da nossa loja toda semana. Toque em uma peça para ver detalhes e chamar no WhatsApp.</p>', '<span class="eyebrow">Feminino &amp; masculino</span>\n          <h2>Looks para <span class="serif">toda ocasião</span></h2>\n          <p>Mais vestidos, peças femininas e os clássicos masculinos da Via Vest. Toque em uma peça para ver detalhes e consultar no WhatsApp.</p>')
s=s.replace('''          <button class="chip" data-filter="conjuntos" role="tab" aria-selected="false">Conjuntos</button>''', '''          <button class="chip" data-filter="conjuntos" role="tab" aria-selected="false">Conjuntos</button>
          <button class="chip" data-filter="feminino" role="tab" aria-selected="false">Feminino</button>''')

# Insert four feminine product cards (images are free Unsplash assets; no watermarks).
wa_icon='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.1-1.3A10 10 0 1 0 12 2Zm5.8 14.2c-.2.7-1.4 1.3-2 1.4-.5.1-1.1.1-1.8-.1-.4-.1-1-.3-1.7-.6-3-1.3-4.9-4.3-5-4.5-.2-.2-1.2-1.6-1.2-3 0-1.4.7-2.1 1-2.4.2-.3.5-.4.7-.4h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.4.5-.4.5c-.1.1-.3.3-.1.6.1.3.6 1 1.3 1.6.9.8 1.6 1 1.9 1.2.2.1.4 0 .5-.1l.7-.9c.2-.2.4-.2.6-.1l2 1c.2.1.4.2.4.3.1.1.1.6-.1 1.3Z"/></svg>'

def product(name, label, desc, specs, wa, img, alt, flag, delay=''):
    delay_attr=f' data-delay="{delay}"' if delay else ''
    return f'''        <article class="product" data-cat="feminino" data-reveal{delay_attr}
          data-name="{name}" data-cat-label="{label}" data-desc="{desc}" data-specs="{specs}" data-wa="Ol%C3%A1!%20Quero%20consultar%20{wa}%20e%20as%20ofertas%20Black%20Friday.">
          <div class="product__media">
            <span class="product__flag product__flag--dark">{flag}</span>
            <img src="img/{img}" alt="{alt}" width="900" height="1200" loading="lazy" decoding="async">
            <button class="product__quick" data-quick aria-label="Ver detalhes de {name}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>Ver detalhes</button>
          </div>
          <div class="product__body">
            <span class="product__cat">{label}</span><h3 class="product__name">{name}</h3>
            <p class="product__desc">{desc}</p>
            <div class="product__foot"><span class="product__price">Atacado &amp; varejo<small>Consulte valores no WhatsApp</small></span>
              <a class="product__wa" href="https://wa.me/5592991193584?text=Ol%C3%A1!%20Quero%20consultar%20{wa}%20e%20as%20ofertas%20Black%20Friday." target="_blank" rel="noopener" aria-label="Consultar {name} no WhatsApp">{wa_icon}</a>
            </div>
          </div>
        </article>'''

fem_cards='\n'.join([
    product('Vestido Floral Midi','Feminino · Vestidos','Vestido floral leve com saia ampla, perfeito para passeios e ocasiões especiais.','Estilo:Midi floral|Caimento:Leve e fluido|Tamanhos:Consulte disponibilidade|Cores:Estampas disponíveis no grupo','Vestido%20Floral%20Midi','fem-floral.webp','Modelo usando vestido feminino midi branco com estampa floral colorida','Destaque Black Friday'),
    product('Vestido Longo Azul','Feminino · Vestidos','Vestido longo estampado de caimento solto para um look fresco e elegante.','Estilo:Longo estampado|Caimento:Solto|Tamanhos:Consulte disponibilidade|Cores:Consulte opções','Vestido%20Longo%20Azul','fem-blue-dress.webp','Modelo vestindo vestido longo azul estampado','Novidade feminina','1'),
    product('Vestido Floral de Verão','Feminino · Vestidos','Vestido floral com amarração, ideal para compor produções leves e coloridas.','Estilo:Floral de verão|Modelagem:Transpassada com amarração|Tamanhos:Consulte disponibilidade|Cores:Estampa floral','Vestido%20Floral%20de%20Ver%C3%A3o','fem-summer.webp','Detalhe de vestido feminino floral em cenário de verão','Look da estação','2'),
    product('Conjunto Feminino Leve','Feminino · Conjuntos','Conjunto feminino de top e saia midi, com visual clean para montar um look completo.','Peças:Top + saia midi|Estilo:Casual elegante|Tamanhos:Consulte disponibilidade|Cores:Consulte opções','Conjunto%20Feminino%20Leve','fem-set.webp','Modelo em conjunto feminino de top e saia midi claros','Look completo','3'),
])
product_marker='''      <div class="grid-products" id="product-grid">\n'''
assert product_marker in s
s=s.replace(product_marker,product_marker+fem_cards+'\n',1)
s=s.replace('6 peças na vitrine. O catálogo completo, com fotos, tamanhos e tabela de atacado, vai direto no seu WhatsApp.','10 peças na vitrine, incluindo vestidos e looks femininos. Entre no grupo para receber os preços promocionais no dia.',1)

# Feminine lookbook uses a wide unwatermarked free photo.
s=s.replace('''<img src="img/lookbook.webp" alt="Lookbook Via Vest Moda: dois modelos em looks casuais nas ruas de Manaus"''', '''<img src="img/fem-summer.webp" alt="Look feminino com vestido floral para a coleção feminina Via Vest"''')
s=s.replace('<span class="eyebrow">Lookbook 2026</span>\n          <h2>Monte a vitrine da sua loja com a estação certa.</h2>\n          <p>Tons terrosos, linho, sarja e cargo. Peças que conversam entre si e vendem em conjunto — não só avulsas.</p>', '<span class="eyebrow">Moda feminina Via Vest</span>\n          <h2>Vestidos e looks leves para renovar o guarda-roupa.</h2>\n          <p>Peças femininas para usar, presentear ou levar para sua loja. Entre no grupo para acompanhar as ofertas da Black Friday.</p>')
s=s.replace('Ver lookbook completo','Ver preços no grupo WhatsApp',1)
s=s.replace('href="https://wa.me/5592991193584?text=Ol%C3%A1!%20Quero%20ver%20o%20lookbook%20completo%20e%20as%20grades%20dispon%C3%ADveis."',f'href="{group}"',1)

# Add an FAQ for the promotional condition and channel.
faq_insert='''          <details class="faq-item">
            <summary>Como funciona o brinde da Black Friday?
              <span class="faq-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></span>
            </summary>
            <p>Nas compras a partir de R$ 400, você leva um brinde. Os preços promocionais serão divulgados no dia pelo nosso grupo no WhatsApp. Entre no grupo para consultar as condições e a disponibilidade do brinde.</p>
          </details>

'''
faq_end='''          </details>
        </div>
      </div>
    </div>
  </section>
  <!-- ================= LOCALIZAÇÃO ================= -->'''
assert faq_end in s
s=s.replace(faq_end,'''          </details>
'''+faq_insert+'''        </div>
      </div>
    </div>
  </section>
  <!-- ================= LOCALIZAÇÃO ================= -->''',1)

# Final CTA campaign button plus WhatsApp service CTA.
s=s.replace('<h2 style="margin-top:.9rem">Renove o estoque<br>ou o seu guarda-roupa.</h2>', '<h2 style="margin-top:.9rem">Black Friday:<br>renove seu <span class="serif">look</span>.</h2>')
s=s.replace('<p>Manda uma mensagem contando o que você procura. A gente responde com fotos, tamanhos e o preço certinho — atacado ou varejo.</p>', '<p>Brinde em compras a partir de R$ 400. Os preços promocionais serão divulgados no dia pelo grupo oficial da Via Vest no WhatsApp.</p>')
cta_anchor='''          <div class="cta__actions">'''
# Put group link before regular service CTA.
s=s.replace(cta_anchor,cta_anchor+f'''\n            <a class="btn btn--light" href="{group}" target="_blank" rel="noopener">Entrar no grupo Black Friday</a>''',1)
s=s.replace('Atacado &amp; varejo · Manaus/AM</p>','Consulte no grupo as condições do brinde e as ofertas do dia.</p>',1)

# Mobile sticky bar: main customer service + Black Friday group invitation.
s=s.replace('''    WhatsApp
  </a>
</div>
<!-- ================= LIGHTBOX ================= -->''',f'''    WhatsApp
  </a>
  <a class="btn btn--dark" href="{group}" target="_blank" rel="noopener" aria-label="Entrar no grupo de ofertas Black Friday">Black Friday</a>
</div>
<!-- ================= LIGHTBOX ================= -->''')

# CSS campaign styles, high-contrast black and champagne.
css='''
/* ============ BLACK FRIDAY CAMPAIGN ============ */
.topbar--bf{gap:.85rem;background:#171411;color:#fff3d3}
.topbar--bf .topbar__campaign{font-size:.62rem;font-weight:800;letter-spacing:.18em;color:#f5cf65}
.topbar--bf a{font-weight:700;color:#fff;text-decoration:underline;text-decoration-color:rgba(245,207,101,.55);text-underline-offset:3px}
.topbar--bf a span{color:#f5cf65}
.bf-section{padding:clamp(1.4rem,3.5vw,2.5rem) 0;background:var(--bone)}
.bf-card{position:relative;overflow:hidden;display:flex;align-items:center;justify-content:space-between;gap:2rem;min-height:260px;padding:clamp(1.7rem,4.5vw,3.6rem);border-radius:var(--r-lg);background:radial-gradient(circle at 80% 20%,rgba(192,138,70,.23),transparent 33%),linear-gradient(120deg,#171411,#241916 65%,#3b1a1f);color:#fff;box-shadow:0 24px 55px -32px rgba(16,14,12,.7)}
.bf-card::before{content:"";position:absolute;inset:0;opacity:.16;background-image:repeating-linear-gradient(135deg,transparent 0 18px,rgba(255,255,255,.14) 19px,transparent 20px 38px);pointer-events:none}
.bf-card__copy{position:relative;z-index:1;max-width:720px}
.bf-kicker{display:inline-flex;align-items:center;gap:.55rem;color:#f5cf65;font-size:.67rem;font-weight:700;letter-spacing:.2em}
.bf-kicker span{width:8px;height:8px;border-radius:50%;background:#f5cf65;box-shadow:0 0 0 5px rgba(245,207,101,.12)}
.bf-card h2{margin-top:.85rem;font-size:clamp(1.8rem,4vw,3.1rem);line-height:1.04;color:#fff;letter-spacing:-.04em}
.bf-card h2 span{color:#f5cf65}
.bf-card h2 em{font-family:'Instrument Serif',Georgia,serif;font-weight:400;color:#f3dfb0}
.bf-card__copy>p{max-width:620px;margin-top:.85rem;color:rgba(255,249,236,.76);font-size:.94rem}
.btn--bf{margin-top:1.25rem;background:#f5cf65;color:#211914}
.btn--bf:hover{background:#ffe39a}
.bf-card__copy small{display:block;margin-top:.75rem;color:rgba(255,249,236,.55);font-size:.7rem}
.bf-card__stamp{position:relative;z-index:1;flex:none;width:clamp(110px,16vw,180px);aspect-ratio:1;border:1px solid rgba(245,207,101,.55);border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#f5cf65;transform:rotate(9deg);box-shadow:0 0 0 9px rgba(245,207,101,.055),0 0 0 18px rgba(245,207,101,.035)}
.bf-card__stamp span{font-size:.62rem;letter-spacing:.24em;font-weight:700}
.bf-card__stamp b{font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(1.4rem,4vw,2.5rem);letter-spacing:-.07em}
@media(max-width:720px){
  .topbar--bf{gap:.45rem;font-size:.59rem;padding:.55rem .65rem;flex-wrap:wrap}
  .bf-card{align-items:flex-start;min-height:0;padding:1.5rem 1.2rem;border-radius:20px}
  .bf-card__stamp{position:absolute;right:1.2rem;top:1.2rem;width:70px;opacity:.72}
  .bf-card__stamp span{font-size:.42rem}.bf-card__stamp b{font-size:1.1rem}
  .bf-card__copy{padding-right:.2rem}.bf-card h2{font-size:1.85rem;max-width:75%}
  .bf-card__copy>p{font-size:.86rem}
  .bf-card .btn{white-space:normal;text-align:center}
}
@media(max-width:380px){.bf-card__stamp{display:none}.bf-card h2{max-width:none}}
'''
s=s.replace('/* ============ 21. RESPONSIVE ============ */',css+'\n/* ============ 22. RESPONSIVE ============ */',1)

# Update footer product category links and about copy.
s=s.replace('Moda casual em atacado e varejo no bairro Flores, Manaus — AM. Camisas, calças cargo, sarja e peças que giram na sua loja.', 'Moda feminina e masculina, vestidos e looks completos em atacado e varejo no bairro Flores, Manaus — AM.')
s=s.replace('<a href="#catalogo">Conjuntos</a>', '<a href="#catalogo">Conjuntos</a>\n          <a href="#catalogo">Vestidos e moda feminina</a>')

# Add group link to social/float CTA nowhere else; preserve regular contact WhatsApp button.

p.write_text(s,encoding='utf-8')
print('updated',len(s),'chars')
