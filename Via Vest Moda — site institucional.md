# Via Vest Moda — site institucional

Site de uma página (one-page) para a Via Vest Moda, atacado e varejo em Manaus/AM.
HTML + CSS + JavaScript puros, sem framework, sem build e sem dependências além das fontes do Google.

## Arquivos

| Arquivo | Para que serve |
| --- | --- |
| `index.html` | Versão para publicar no servidor. Usa a pasta `img/`. |
| `img/*.webp` | Fotos do site otimizadas em WebP, com peças masculinas e femininas. |
| `via-vest-moda.html` | Versão **única e portátil**, com as imagens embutidas em base64. Serve para abrir com duplo clique ou enviar por WhatsApp/e-mail sem perder as fotos. |

## Como publicar (rápido)

1. **Netlify Drop** — entre em app.netlify.com/drop e arraste a pasta com `index.html` + `img/`. O site fica no ar em segundos, com HTTPS.
2. **Vercel** — `vercel` na pasta do projeto, ou arraste a pasta no painel.
3. **Hospedagem tradicional (cPanel/FTP)** — envie `index.html` e a pasta `img/` para `public_html`.
4. **GitHub Pages** — suba os arquivos no repositório e ative o Pages na branch principal.

Domínio próprio: aponte o DNS para o serviço escolhido e depois atualize a tag `canonical` no `<head>`.

## O que editar

- **WhatsApp**: o número `5592991193584` aparece nos links `wa.me`. Use localizar e substituir no arquivo.
- **Textos**: todo o conteúdo está em português, dentro das seções comentadas (`<!-- ===== HERO ===== -->`, etc.).
- **Produtos**: cada item é um `<article class="product">`. Para adicionar outro, copie um bloco inteiro e ajuste `data-cat`, `data-name`, `data-desc`, `data-specs` (pares separados por `|`) e a imagem.
- **Fotos**: substitua os arquivos em `img/` mantendo o mesmo nome, ou troque o `src`. Proporção ideal: 3:4 nas peças, 4:5 no hero, 16:9 no lookbook.
- **Cores e fontes**: tudo centralizado em `:root` no começo do `<style>` (`--wine`, `--ink`, `--bone`, `--ochre`).

## Antes de publicar — checklist

- [ ] Trocar o link `canonical` (está comentado no `<head>`) pelo domínio real.
- [ ] Trocar `og:image` por uma URL absoluta (ex.: `https://seudominio.com.br/img/lookbook.webp`) para o preview no WhatsApp/Instagram ficar correto.
- [ ] Revisar os **depoimentos** da seção “Quem compra, volta”: são exemplos de layout, não avaliações reais. Substitua por avaliações verdadeiras ou remova o bloco.
- [ ] Confirmar **horários de atendimento** e condições de **troca/entrega** (hoje escritos de forma genérica, sem prometer prazos).
- [ ] Criar/atualizar o **Google Meu Negócio** com o mesmo endereço e telefone — é o que mais traz cliente local.
- [ ] Se tiver Instagram/Facebook, adicionar os links nos ícones do rodapé.

## Campanha Black Friday

- A oferta está anunciada como **brinde em compras a partir de R$ 400**.
- O site não divulga preços ou percentuais inventados: o texto informa que os preços promocionais serão comunicados no dia pelo grupo oficial do WhatsApp.
- O convite para o grupo foi adicionado ao topo, hero, faixa de campanha, CTA final e barra fixa mobile.
- A vitrine tem quatro produtos femininos demonstrativos (três vestidos e um conjunto) além das peças masculinas. Preços, tamanhos e estoque são indicados para consulta; confirme com a loja antes da publicação.
- Fotografias femininas: imagens de Unsplash. A licença permite uso comercial e não exige atribuição; a atribuição é recomendada: [licença Unsplash](https://unsplash.com/license), [busca vestidos florais](https://unsplash.com/s/photos/floral-dress), [busca vestido de verão](https://unsplash.com/s/photos/summer-dress), [busca look feminino](https://unsplash.com/s/photos/summer-outfits).

## Notas técnicas

- Layout responsivo testado de 360 px a 1920 px, sem rolagem horizontal.
- Acessibilidade: navegação por teclado, `aria-expanded` no menu, `aria-modal` no lightbox, foco visível, `prefers-reduced-motion`.
- O mapa do Google é carregado **só quando o visitante clica** em “Ver no mapa” (mais rápido e sem cookies de terceiros na abertura).
- Imagens: `.webp` com `width`/`height` declarados e `loading="lazy"` fora da primeira dobra, para evitar salto de layout.
- SEO: title, description, Open Graph, Twitter Card e JSON-LD `ClothingStore` com endereço e telefone.
- As fotos deste pacote foram geradas por IA para servir de demonstração. Ao publicar com fotos reais dos produtos, a conversão melhora — e evita qualquer dúvida sobre a peça mostrada.
