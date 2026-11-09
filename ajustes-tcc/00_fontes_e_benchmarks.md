# Fontes e Benchmarks — Savá (Etapa 0)

Levantamento feito em 09/11/2026. Este arquivo vai virar a aba "Fontes e Benchmarks" da planilha (Etapa 3).

**Regra de uso:** nenhum número abaixo é dado da Savá. No texto do TCC, escrever sempre "referência de mercado (fonte, ano)".

**Como ler a coluna "Status":**
- **Confirmado:** achei a fonte primária, ou uma página oficial da própria fonte.
- **Secundário:** o número aparece em blogs ou matérias que citam a fonte, mas não abri o relatório original.
- **Não encontrado:** não achei o número em nenhuma fonte. Não usar sem conferir.
- **Corrigido:** o número existe, mas a fonte certa é outra.

**Confiabilidade:**
- **Alta:** instituto de pesquisa ou relatório com metodologia aberta.
- **Média:** fornecedor ou plataforma (por exemplo, Recharge e Nuvemshop) ou matéria jornalística com fonte citada.
- **Baixa:** blog, agência ou número sem metodologia.

---

## 1. Conversão do site (pedidos ÷ sessões)

| # | Métrica | Valor | Fonte | Ano | Status | Confiab. | Como será usada |
|---|---|---|---|---|---|---|---|
| 1.1 | Conversão média do e-commerce brasileiro | 1,65% | Neotrust (citada em blogs de CRO) | 2024 | Secundário: não achei o relatório da Neotrust | Média | Cenário **base** |
| 1.2 | Conversão média global | 2,9% | Citada em compilações; os relatórios variam entre 1,4% e 2,9% conforme a metodologia (Crevio) | — | Secundário | Baixa | Só como contexto. Não usar como meta. |
| 1.3 | Conversão Brasil (Experian Hitwise) | 1,92% | Experian Hitwise | — | Não encontrado nesta rodada | Baixa | Não usar sem conferir |
| 1.4 | Saúde e bem-estar 3,2% / cosméticos 2,9% (E-Commerce Radar/edrone) | — | — | 2024 | **Não encontrado.** O estudo da edrone que aparece nas buscas mede *inscrição em pop-up* (saúde e bem-estar: 6,57%), não conversão em compra. | — | **Não usar** |
| 1.5 | Saúde e bem-estar, mediana (benchmark internacional) | 3,31% | Crevio, benchmarks 2026 | 2026 | Secundário | Baixa a média | Teto de referência para o cenário **otimista** |
| 1.6 | Saúde e bem-estar (internacional) | 3,5% | Ruler Analytics, via Thunderbit | 2026 | Secundário | Baixa | Idem |
| 1.7 | Saúde e bem-estar em lojas Shopify | 3,0% a 3,4% | Shopify, via Launchtip | 2026 | Secundário | Baixa | Idem |
| 1.8 | Conversão mobile x desktop no Brasil | 1,2% x 2,8%; cerca de 63% das sessões em mobile | Neotrust (citada em blog) | 2024 | Secundário | Média a baixa | Separar o funil por dispositivo |
| 1.9 | Participação do mobile | 64% do tráfego e 42% das transações | ABComm (citada em blog) | 2024 | Secundário | Média a baixa | Confirma que o mobile converte menos |

**Cenários propostos para a conversão do site (o grupo decide na Etapa 2):**

| Cenário | Taxa | Justificativa |
|---|---|---|
| Conservador | 1,0% | Marca nova, sem avaliações nem prova social, num tema sensível. Começa abaixo da média do Brasil. |
| Base | 1,65% | Média do e-commerce brasileiro (Neotrust, 2024, a validar). |
| Otimista | 2,5% | Abaixo das referências internacionais de saúde e bem-estar (3,0% a 3,5%). Supõe avaliações, página de produto otimizada e tráfego mais qualificado (indicação e lista de espera). |

## 2. Abandono de carrinho (carrinhos sem compra ÷ carrinhos criados)

| # | Métrica | Valor | Fonte | Ano | Status | Confiab. | Como será usada |
|---|---|---|---|---|---|---|---|
| 2.1 | Abandono médio global | 70,22% | Baymard Institute. Média de 50 estudos (2006–2025), atualizada em 22/09/2025. https://baymard.com/lists/cart-abandonment-rate | 2025 | **Confirmado** | Alta | Cenário **otimista** |
| 2.2 | Abandono no Brasil | 82% | **E-Commerce Radar**, citado pela imprensa. Não é Neotrust. | — | **Corrigido** (a fonte não é a Neotrust) | Média | Cenário **conservador** |
| 2.3 | Abandono na América Latina | 75,3% | E-Commerce Radar (citado pela imprensa) | — | Secundário | Média | Cenário **base** |
| 2.4 | Frete como motivo de abandono | 51% dos abandonos | nstech / Frete Rápido | — | Secundário | Média | Justificar frete grátis ou frete fixo como alavanca |
| 2.5 | Sazonalidade do abandono | 77% em dezembro x 82% em janeiro | Blog Shopify Brasil | — | Secundário | Baixa | Contexto |
| 2.6 | Parte do abandono é de quem estava "só olhando" | — | Baymard | 2025 | Confirmado | Alta | Explicar à banca por que 100% de recuperação é impossível |
| 2.7 | Abandono mobile x desktop | Varia muito: 73–75% x 65–68%, ou 80% x 66% (Dynamic Yield) | Várias | — | **Divergente** | Baixa | Usar só "mobile é pior", sem um número exato |

**Cenários propostos para o abandono de carrinho:** conservador 82% (Brasil), base 75% (América Latina), otimista 70% (média global da Baymard).

## 3. Recompra (compra avulsa)

| # | Métrica | Valor | Fonte | Ano | Status | Confiab. | Como será usada |
|---|---|---|---|---|---|---|---|
| 3.1 | Recompra média de 41%; recorrentes geram 47% da receita | — | Flowbiz | — | **Não encontrado.** O "41%" que aparece nas buscas é outro dado: clientes fiéis geram 41% da receita, em estudo genérico. | — | **Não usar** |
| 3.2 | Recompra saudável de cliente novo: até 30% | — | Fonte do varejo (não identificada) | — | Não verificado nesta rodada | Baixa | A validar |
| 3.3 | Segunda compra em cosméticos: cerca de 25% a 26% | — | Shopify Brasil | — | Não verificado nesta rodada | Baixa | A validar |
| 3.4 | Retenção anual sem assinatura: 23% a 31% | — | Fontes secundárias | — | Não verificado | Baixa | A validar |

**Observação:** as premissas de recompra do próprio TCC (30% ou 20%) são **premissas do grupo**, não dados. Na planilha vou montar a recompra por coorte (por mês de entrada) com faixa conservador/base/otimista. Abro as fontes 3.2 e 3.3 na Etapa 3.

## 4. Assinatura e cancelamento (churn)

| # | Métrica | Valor | Fonte | Ano | Status | Confiab. | Como será usada |
|---|---|---|---|---|---|---|---|
| 4.1 | Churn na primeira renovação (ciclos 2 e 3), saúde e bem-estar | 26,5% | Recharge, "Subscription churn is front-loaded" (conteúdo publicado pela Recharge) | 2026 | **Confirmado** (página da própria Recharge) | Média (fornecedor, sem metodologia aberta) | Curva de churn: ciclos iniciais |
| 4.2 | Churn em ciclos maduros (ciclo 6 em diante), saúde e bem-estar | 7,5% | Recharge (mesmo conteúdo) | 2026 | Confirmado | Média | Curva de churn: ciclos maduros |
| 4.3 | Concentração dos cancelamentos | Cerca de 61% dos cancelamentos voluntários nas duas primeiras renovações; cerca de 72% nas quatro primeiras | Recharge (citada de segunda mão) | 2026 | Secundário | Média | Justificar a régua anticancelamento |
| 4.4 | Primeira recompra em suplementos | 86,6% dos que compram suplemento pela primeira vez fazem a 1ª recompra | Recharge, análise de suplementos | 2026 | Secundário. É uma métrica diferente da 4.1. | Média | Contexto (não misturar com a 4.1) |
| 4.5 | Churn mensal | 4% a 7% em programa bem gerido; 8% a 12% na categoria saúde (Eightx citando Finsi); cerca de 4,2% (Recharge 2023, via Eightx) | Várias | — | **Divergente** | Baixa | Só para checar se a curva faz sentido |
| 4.6 | Cerca de 44% dos cancelamentos nos primeiros 90 dias | — | Fonte secundária | — | Não verificado | Baixa | A validar |

**Atenção:** o "ciclo" da Recharge é um ciclo de cobrança, em geral mensal. A assinatura da Savá foi descrita de formas diferentes ao longo do TCC (ver o diagnóstico). Antes de aplicar a curva, preciso saber o que é um ciclo na Savá.

## 5. Mídia paga e políticas de anúncio

| # | Métrica | Valor | Fonte | Ano | Status | Confiab. | Como será usada |
|---|---|---|---|---|---|---|---|
| 5.1 | CPM no Meta | R$ 15–35 (Feed); R$ 8–20 (Stories/Reels); saúde de 2x a 3x a média | Trafius (agência) | 2026 | Não verificado nesta rodada | Baixa | Faixa de CPM nos três cenários (a validar) |
| 5.2 | CPC no Meta | R$ 0,40 a R$ 6,00 | Trafius (agência) | 2026 | Não verificado | Baixa | Tráfego comprado = verba ÷ CPC |
| 5.1b | CPC no Meta (Brasil) | R$ 0,30 a R$ 4,50 por clique | Trafius, "CPC médio no Meta Ads em 2026 por segmento" (agência). https://trafius.com.br/blog/cpc-medio-no-meta-ads-em-2026-por-segmento | 2026 | Secundário | Baixa | Faixa do CPC |
| 5.1c | CPC no Meta, objetivo tráfego (Brasil) | R$ 0,50 a R$ 2,00 (faixa ampliada: R$ 0,20 a R$ 8,00) | ViniEnsina (blog). https://viniensina.com.br/quanto-custa-anunciar-no-facebook/ | 2026 | Secundário | Baixa | Faixa do CPC |
| 5.1d | CPM no Meta (Brasil) | R$ 8 a R$ 45, conforme segmento e posicionamento | Trafius. https://trafius.com.br/blog/cpm-meta-ads-o-que-e-como-reduzir | 2026 | Secundário | Baixa | Faixa do CPM |
| 5.1e | CPM de saúde e bem-estar (global) | O mais alto entre os setores (US$ 12 a 21, conforme a fonte) | Influee / ViniEnsina | 2026 | Divergente; não é Brasil | Baixa | Justifica usar a faixa **alta** de CPC para saúde |
| 5.1f | **Cenários de CPC adotados (premissa a validar)** | Otimista R$ 1,50 · Base R$ 2,50 · Conservador R$ 4,00 | Faixa acima da média geral (5.1b e 5.1c) porque saúde é mais caro (5.1e) | — | **Premissa** | — | Calcular quantos cliques a verba compra. **Validar com a simulação no Gerenciador de Anúncios (feita pelo grupo).** |
| 5.3 | Política do Meta: atributos pessoais | Proibido afirmar ou insinuar que a pessoa tem uma condição de saúde ("Você sofre de candidíase?") | Padrões de Publicidade do Meta (resumidos por fontes secundárias) | 2026 | Secundário. Conferir o texto oficial. | Média | Regras de criativo e copy |
| 5.4 | Política do Meta: autopercepção negativa | Proibido gerar autopercepção negativa para vender produto de saúde ou bem-estar | Idem | 2026 | Secundário | Média | Idem |
| 5.5 | Política do Meta: revisão de saúde e bem-estar | Fontes falam numa revisão em 22/07/2026 que passa a restringir por alegação, e numa categoria "Produtos adultos e saúde reprodutiva". **Não achei o detalhe para saúde reprodutiva.** | Fontes secundárias | 2026 | **A validar** | Baixa | Tratar como risco: pode limitar segmentação e criativo |

## 6. Influenciadores

| # | Métrica | Valor | Fonte | Ano | Status | Confiab. | Como será usada |
|---|---|---|---|---|---|---|---|
| 6.1 | Engajamento de nano no Instagram | 2,19% (relatório 2025); mediana de 1,78% (relatório 2026) | HypeAuditor, State of Influencer Marketing 2025 e 2026 | 2025/2026 | Confirmado (relatório da HypeAuditor) | Média a alta | **Substitui o "2–5%"** do levantamento inicial |
| 6.2 | Engajamento de nano no TikTok | 11,9% | HypeAuditor 2025 | 2025 | Confirmado | Média a alta | Comparar plataformas |
| 6.3 | Macro e mega no Instagram | Cerca de 0,33% a 0,35% | HypeAuditor 2026 | 2026 | Confirmado | Média a alta | Argumento a favor de nano e micro |
| 6.4 | "Engajamento de nano 113% superior" | — | — | — | **Não encontrado.** Pode ser uma razão entre faixas, mas não achei. | — | **Não usar** |
| 6.5 | Preço por post no Instagram | Nano US$ 10–100; micro US$ 100–500 | Influee (blog de plataforma) | 2025/2026 | Secundário | Baixa | Só referência internacional. As influenciadoras são brasileiras: usar as faixas em reais (6.7b e 6.7c) |
| 6.6 | Preço por post no TikTok | Micro US$ 50–300; nano US$ 85–135 (plataforma Dok3, fonte secundária) | Influee; Dok3 | 2025 | Secundário | Baixa | Idem |
| 6.7 | Micro no Brasil | "Algumas centenas de reais" por post; não há tabela única | Metricool / Shopify BR | 2025 | Secundário | Baixa | Faixa em reais (a validar com cotação real) |
| 6.7b | Story patrocinado, a partir de cerca de 10 mil seguidores (Brasil) | R$ 300 a R$ 1.500 por story; abaixo disso, em geral permuta ou envio de produto | Agenciagram (blog), 2026. https://agenciagram.com.br/blog/como-ser-micro-influenciador-instagram-2026 | 2026 | Secundário | Baixa | **Faixa em reais** de micro (substitui a conversão do dólar) |
| 6.7c | Reels de criadoras com 5 a 20 mil seguidores (Brasil) | Piso de cerca de R$ 300 por Reels | Inteligência Setorial (blog). https://inteligenciasetorial.com.br/quanto-cobrar-por-publipost-no-tiktok/ | 2026 | Secundário | Baixa | Faixa em reais de nano e micro |
| 6.8 | Engajamento da Lela Brandão | 5,05% | Dado do próprio TCC (sem fonte indicada) | — | **Sem fonte** | — | Citar a ferramenta e a data da medição |

## 7. Jornada de compra e canais no Brasil (novos benchmarks)

| # | Métrica | Valor | Fonte | Ano | Status | Confiab. | Como será usada |
|---|---|---|---|---|---|---|---|
| 7.1 | Compraram por redes sociais (últimos 12 meses) | 54% | CNDL/SPC Brasil (via Monitor Mercantil) | 2025/2026 | Secundário | Média | Jornada: compra social |
| 7.2 | Antes de comprar online | 64% checam o preço; 39% leem comentários de outros consumidores | CNDL/SPC Brasil (idem) | 2025/2026 | Secundário | Média | Jornada: consideração (avaliações) |
| 7.3 | Participam de grupos VIP de WhatsApp de empresas | 41% | CNDL/SPC Brasil (via Diário do Pará; edição a confirmar) | — | Secundário | Média a baixa | Canal WhatsApp/CRM |
| 7.4 | WhatsApp como canal preferido de atendimento | 37% | E-commerce Trends (via Meio & Mensagem) | 2026 | Secundário | Média | Política de atendimento |
| 7.5 | Avaliações de consumidores como formato mais influente | 43,5% | Optimiza, Mapa da Busca 2026 (via Central do Varejo) | 2026 | Secundário | Média | Prova social e growth |
| 7.6 | Influência na decisão: publicidade x influenciadores | 61% x 48% | Brain Inteligência Estratégica (via Meio & Mensagem) | — | Secundário | Média | Argumento: influenciadora não basta |
| 7.7 | Faturamento de Saúde e Beleza nas lojas Nuvemshop | +44% em 2025 | NuvemCommerce 2026 | 2026 | Secundário | Média | Contexto de mercado |
| 7.8 | Ticket médio D2C (lojas Nuvemshop) | R$ 283,53 em set/2026 (+6,1% sobre 2025) | Nuvemshop, Radar D2C | 2026 | Confirmado (página da Nuvemshop) | Média | Comparar com o ticket da Savá |
| 7.9 | Fonte de informação sobre saúde | 59% usam o digital como fonte principal; 34% sites e fóruns; 15% grupos; 12% influenciadores | Ipsos/Bayer (já está no TCC) | 2025 | Já usado no TCC | Média a alta | Jornada: descoberta |

---

## O que você precisa conferir (lista "a validar")

1. **Neotrust 2024:** abrir o relatório e confirmar 1,65%, mobile 1,2% x desktop 2,8% e 63% de sessões em mobile.
2. **E-Commerce Radar:** confirmar a fonte e o ano do abandono de 82% no Brasil e de 75,3% na América Latina.
3. **Flowbiz:** se o grupo tiver o material de onde saíram os 41% e 47%, me mande. Sem ele, não uso o número.
4. **E-Commerce Radar/edrone (conversão por categoria):** se existir o relatório com 3,2% e 2,9%, me mande. Sem ele, uso as faixas 1.5 a 1.7.
5. **Trafius (CPM e CPC):** abrir a fonte. O ideal é complementar com uma simulação real no Gerenciador de Anúncios, que é de graça e mostra o alcance estimado para mulheres de 18 a 45 anos em SP com a verba planejada.
6. **Política do Meta para saúde reprodutiva:** ler o texto oficial nos Padrões de Publicidade (transparency.meta.com).
7. **Preço de influenciadores no Brasil:** o melhor é pedir 3 a 5 orçamentos reais (mídia kit). Vale mais que qualquer tabela.
8. ~~Cotação do dólar~~: não é necessária. As influenciadoras são brasileiras e os valores ficam em reais (6.7b e 6.7c).
9. **Engajamento da Lela Brandão (5,05%):** indicar a ferramenta e a data da medição.

## Links consultados

- [Baymard: taxa de abandono de carrinho](https://baymard.com/lists/cart-abandonment-rate)
- [Recharge: o churn de assinatura se concentra no início](https://getrecharge.com/?p=27190)
- [Recharge: suplementos têm a primeira recompra mais frágil](https://getrecharge.com/?p=27176)
- [Recharge: categoria saúde e bem-estar](https://getrecharge.com/vertical/health-and-wellness/)
- [Eightx: benchmark de churn em assinatura de suplementos](https://eightx.co/blog/supplement-subscription-churn-rate-benchmark)
- [HypeAuditor: State of Influencer Marketing 2025](https://hypeauditor.com/state-of-influencer-marketing-2025/)
- [HypeAuditor: State of Influencer Marketing 2026 (PDF)](https://hypeauditor.com/uploaded-files/state-of-im-2026.pdf)
- [Influee: tipos de influenciadores](https://influee.co/br/blog/types-of-influencers)
- [Metricool: quanto ganha um influenciador](https://metricool.com/pt/quanto-ganha-influenciador/)
- [Crevio: benchmarks de conversão no e-commerce](https://crevio.co/pt/blog/ecommerce-conversion-rate)
- [Thunderbit: estatísticas de conversão no e-commerce](https://thunderbit.com/pt/blog/ecommerce-conversion-statistics)
- [Launchtip: benchmarks de conversão Shopify por setor 2026](https://www.launchtip.com/pt-BR/blog/benchmarks-taxa-de-conversao-shopify-por-setor-2026)
- [Central do Varejo: estudo da edrone sobre pop-ups](https://centraldovarejo.com.br/pop-ups-convertem-ate-25-no-e-commerce-brasileiro-aponta-estudo-formato-gamificado-supera-versao-tradicional-em-42-vezes/?amp=1)
- [Babitonhela: taxa de conversão média no e-commerce brasileiro](https://babitonhela.com/blog/taxa-conversao-media-ecommerce-brasileiro-dados)
- [Monitor Mercantil: abandono de carrinho chega a 82% no Brasil](https://monitormercantil.com.br/abandono-de-carrinhos-no-comercio-eletronico-chega-a-82-no-brasil/)
- [Mundo Logística: frete como motivo de abandono (nstech)](https://mundologistica.com.br/noticias/frete-motivo-abandono-carrinhos-nstech)
- [Shopify Brasil: abandono de carrinho](https://www.shopify.com/br/blog/abandono-de-carrinho?)
- [Accelerated Digital Media: políticas de anúncio de saúde 2026](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/)
- [AuditSocials: padrões de anúncio do Meta 2026](https://www.auditsocials.com/blog/meta-ad-misleading-claims-personal-attributes-prohibited-content-policy-2026)
- [Monitor Mercantil: e-commerce levou 139 milhões de consumidores às compras em 2025 (CNDL/SPC)](https://monitormercantil.com.br/e-commerce-levou-139-milhoes-de-consumidores-as-compras-em-2025/)
- [Diário do Pará: sete em cada dez brasileiros compram online todo mês](https://diariodopara.com.br/seu-bolso/sete-em-cada-dez-brasileiros-compram-online-todo-mes/)
- [Meio & Mensagem: IA já impacta o consumo](https://www.meioemensagem.com.br/marketing/ia-ja-impacta-consumo-e-maioria-compra-a-noite)
- [Meio & Mensagem: brasileiros confiam mais em preço do que em influenciadores](https://www.meioemensagem.com.br/marketing/brasileiros-confiam-mais-em-preco-do-que-em-influenciadores)
- [Central do Varejo: avaliações lideram a decisão de compra online](https://centraldovarejo.com.br/avaliacoes-de-consumidores-lideram-decisao-de-compra-online/)
- [NuvemCommerce 2026 (PDF)](https://site.nuvemshop.com.br/hubfs/%5BBR%5D%20Descarreg%C3%A1veis/NuvemCommerce%202026.pdf)
- [Nuvemshop: Radar D2C, setembro de 2026](https://www.nuvemshop.com.br/radar-ecommerce-d2c/2026/setembro)
