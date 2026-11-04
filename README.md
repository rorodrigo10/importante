# Shopenis — checkout demonstrativo

Página estática responsiva com visual baseado nas referências: produto, carrinho e checkout com endereço em janela modal e opções de pagamento. O anúncio deve apontar para a raiz do site publicado (`index.html`). Comprar com cupom abre diretamente o checkout e o endereço; adicionar ao carrinho permite passar pela tela de carrinho.

## Abrir no computador

No GitHub, selecione a branch `checkout/shopenis-visual`, clique em **Code → Download ZIP** e extraia o ZIP. Abra `ABRIR-CHECKOUT.html` com Chrome ou Edge. Esse arquivo contém estilos, scripts e imagem e funciona sem instalação ou servidor. Não abra o HTML dentro do ZIP: extraia antes.

Para verificar, escolha a cor e capacidade, clique em **Compre Com Cupom**, preencha o endereço e veja as opções de pagamento. **Adicionar Ao Carrinho** abre a tela de carrinho. Tudo é demonstrativo; nenhum pedido ou cobrança é criado.

## Executar

No diretório `/workspace/importante`:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Abra a raiz no navegador local. Não há dependências para instalar nem build. Os arquivos `index.html`, `style.css` e `app.js` podem ser hospedados em um serviço de sites estáticos com HTTPS. `Taina.txt` é o arquivo original e foi preservado.

## Comportamento

- Cinco cores e capacidades de 256/512 GB; resumo atualizado automaticamente.
- Preços ilustrativos definidos em `app.js`: R$ 5.850,16 e R$ 6.650,16. Substituir pelos valores comerciais aprovados antes de vender.
- Imagem ilustrativa em `assets/iphone-blue.png`, recriada com geração de imagem a partir da referência fornecida. Não é a fotografia original. Cores alternativas são simulações por filtro CSS; substituir por fotografias autorizadas de cada variante antes de usar comercialmente.
- Campos de entrega com validação básica do navegador. Não há consulta de CEP nem cálculo de frete.
- Endereço mantido somente em memória; desaparece ao recarregar. Nenhum dado é enviado ou armazenado.
- Pagamento demonstrativo; não coleta cartão, não cria pedido e não efetua cobrança.

## InfinitePay — pendente

É necessário escolher entre links de checkout existentes ou integração de API, e fornecer o identificador público/link correspondente da conta. Não inserir senhas ou chaves privadas no JavaScript.

Para uma operação real, implementar criação de pedido em backend com validação de produto, variante, preço e frete; preservar o endereço associado ao pedido; encaminhar ao checkout hospedado da InfinitePay conforme a documentação vigente; confirmar o pagamento pelo mecanismo oficial do provedor antes de liberar o pedido. A seleção de Pix/cartão desta demonstração ainda não controla um provedor real. Links fixos isolados não enviam os dados de entrega automaticamente.

Antes de publicar para vendas, configurar fotos, valores, estoque, frete, dados da loja, políticas e integração de pagamento. O protótipo não deve ser usado para cobrar clientes.

## Validação executada

Teste com Playwright e Chromium: seleção Sálvia/512 GB, preço atualizado, carrinho, abertura da janela de endereço, bloqueio de formulário vazio, preenchimento e resumo do endereço, troca de método de pagamento e conclusão demonstrativa. Tipografia e proporções de desktop alinhadas às referências de 1480 px; detalhes em duas colunas com largura de rótulo de 225 px e descrição com avisos legais contínuos. Produto, carrinho e checkout sem overflow horizontal em 390, 768 e 1024 px. Nenhum erro JavaScript observado. `node --check app.js` passou.
