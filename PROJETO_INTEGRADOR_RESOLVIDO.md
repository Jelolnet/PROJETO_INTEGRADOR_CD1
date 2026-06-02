# RESOLUÇÃO DO PROJETO INTEGRADOR EXTENSIONISTA (AE1 E AE2)
**Aluno:** Jefferson Matos dos Santos  
**Empresa de Referência:** SABESP (Recorte Regional de Saneamento)  
**Tema do Projeto:** Análise de Dados para Redução de Perdas Aparentes (Fraudes e Submedição) em Ramais de Abastecimento na Região Metropolitana de São Paulo (Foco: Unidade de Negócio Norte / Franco da Rocha - SP)

---

# PARTE 1: ATIVIDADE DE ESTUDO 1 (AE1) - PLANEJAMENTO DO PROJETO

## 1. Termo de Abertura + Briefing

### Contexto e Justificativa (Extensão)
As perdas aparentes de água (que englobam fraudes, ligações clandestinas e falhas/submedição de hidrômetros) representam um grande desafio operacional, financeiro e social para o saneamento público. A SABESP atua em um território complexo na Região Metropolitana de São Paulo, onde o desperdício compromete a segurança hídrica das bacias. Este projeto integrador extensionista propõe a utilização de técnicas de análise de dados e estatística para identificar padrões suspeitos de consumo e direcionar as equipes de fiscalização e troca de hidrômetros de forma inteligente, gerando retorno social (garantia de abastecimento coletivo), ambiental (preservação do recurso hídrico) e econômico.

### Objetivo Geral
Desenvolver um modelo de análise exploratória e detecção de anomalias baseado no histórico de consumo de clientes de Franco da Rocha - SP para prever possíveis fraudes ou necessidade de manutenção de hidrômetros antigos, reduzindo o índice de perdas aparentes em 15% na área piloto no prazo de 8 semanas.

### Objetivos Específicos
* Cruzar dados cadastrais (idade do hidrômetro, perfil de consumo) com dados de consumo mensal de 5.000 ligações residenciais e comerciais.
* Identificar os 3 principais perfis de consumo que apresentam maior propensão a perdas aparentes.
* Desenvolver um painel visual (Dashboard) que indique áreas críticas com maior probabilidade de anomalia para orientar as equipes de campo da SABESP.

### Público-Alvo / Beneficiários
* **Diretos:** Gestores operacionais e equipes de fiscalização/manutenção da Unidade de Negócio Norte da SABESP.
* **Indiretos:** População local do município de Franco da Rocha, beneficiada com a maior regularidade no abastecimento devido à redução das perdas de água na rede.

### Escopo (O que entra e o que não entra)
* **ENTRA:**
  * Coleta e análise de dados históricos anonimizados de faturamento mensal dos últimos 24 meses das ligações selecionadas.
  * Desenvolvimento do dicionário de dados, modelo lógico e plano de qualidade de dados.
  * Criação de um dashboard interativo (esboço e lógica) focado em KPIs de perdas aparentes.
  * Planejamento inicial de cronograma, riscos e EAP.
* **NÃO ENTRA:**
  * Execução física de vistorias ou troca de hidrômetros em campo.
  * Desenvolvimento de aplicativo mobile para os leituristas.
  * Integração em tempo real com o banco de dados principal de faturamento corporativo da SABESP (SAP).

### Perguntas Analíticas (Mín. 3)
1. Qual é a correlação entre a idade do hidrômetro instalado e a queda repentina de consumo medido em ligações comerciais?
2. Quais bairros ou setores de Franco da Rocha concentram a maior taxa de desvio padrão negativo em relação à média histórica da categoria?
3. A partir de qual limiar de redução de consumo mensal em imóveis de alto padrão podemos inferir uma anomalia com probabilidade superior a 80%?

### Indicadores / KPIs (Mín. 3) e Definição de Sucesso
1. **Taxa de Assertividade de Fiscalização (TAF):** Porcentagem de vistorias em campo direcionadas pelo modelo que de fato identificaram fraude ou hidrômetro quebrado. (Meta de sucesso: > 75%).
2. **Índice de Volume Recuperado Estimado (IVRE):** Total em m³ de água recuperados (que voltaram a ser medidos/faturados) após intervenção baseada nas análises. (Meta de sucesso: > 2.500 m³/mês na área piloto).
3. **Tempo Médio de Detecção de Anomalia (TMDA):** Tempo decorrido entre o início do desvio de consumo e a geração do alerta para vistoria. (Meta de sucesso: queda de 6 meses para menos de 2 meses).

### Fontes de Dados e Forma de Acesso
* **Fonte de dados primária:** Amostra histórica fictícia/anonimizada baseada nos padrões operacionais da SABESP (cadastros de ramais, tabelas de faturamento mensal e ordens de serviço de substituição de hidrômetros).
* **Forma de acesso:** Extração de relatórios anonimizados em formato CSV/Excel a partir de um ambiente sandbox simulado, preservando nomes, CPFs e dados pessoais sensíveis dos clientes reais.

### Aspectos Éticos / LGPD (Riscos e cuidados)
Para estrita conformidade com a LGPD (Lei Geral de Proteção de Dados - Lei nº 13.709/2018), todos os dados dos clientes sofrerão processo de descaracterização irreversível (anonimização): os nomes serão convertidos em IDs sequenciais aleatórios, os endereços reais serão agrupados apenas por setores hidráulicos/bairros amplos, e números de documentos reais não constarão na base de dados. O projeto visa exclusivamente a eficiência do ativo hidráulico e não o perfilamento ou exposição individual do consumidor.

---

## 2. Plano Inicial do Projeto (EAP, Cronograma e Riscos)

### EAP / WBS (Estrutura Analítica do Projeto)
* **1. Gestão do Projeto**
  * 1.1 Termo de Abertura e Alinhamento Acadêmico
  * 1.2 Cronograma e Matriz de Riscos Homologados
  * 1.3 Repositório GitHub Configurado
* **2. Engenharia e Modelagem de Dados**
  * 2.1 Coleta e Carga da Base Anonimizada (CSV)
  * 2.2 Dicionário de Dados Operacional
  * 2.3 Modelo Lógico de Banco de Dados Relacional
  * 2.4 Scripts de ETL (Limpeza e Qualidade de Dados)
* **3. Análise Exploratória (EDA) e Dashboard**
  * 3.1 Análise Estatística de Correlações e Anomalias
  * 3.2 Protótipo Visual / Wireframe do Dashboard
  * 3.3 Dashboard Funcional de Monitoramento de Perdas
* **4. Encerramento e Documentação**
  * 4.1 Relatório Final de Resultados Extensionistas
  * 4.2 README do GitHub e Documentação Técnica Atualizada

### Cronograma Macro (Por Semana)
* **Semana 1:** Kick-off do projeto, elaboração do Termo de Abertura + Briefing (AE1), estruturação do repositório GitHub e entrega da AE1.
* **Semana 2:** Levantamento dos dados operacionais fictícios, montagem do Dicionário de Dados e modelagem lógica (AE2).
* **Semana 3:** Desenvolvimento do plano e execução das checagens de qualidade de dados (limpeza de nulos, inconsistências e duplicidades).
* **Semana 4:** Análise exploratória dos dados (EDA), identificação dos perfis de consumo e correlações de perdas de água.
* **Semana 5:** Desenho do wireframe e montagem dos primeiros esboços gráficos do painel de monitoramento.
* **Semana 6:** Desenvolvimento do Dashboard operacional e validação das regras de negócios com o cenário piloto de Franco da Rocha.
* **Semana 7:** Teste integrado do modelo e consolidação dos resultados da redução de perdas aparentes simuladas.
* **Semana 8:** Ajustes finais baseados no checklist, formatação do relatório acadêmico de extensão e entrega da AE2.

### Matriz de Riscos (5 Riscos com Mitigação)
1. **Risco 1 (Dados Incompletos/Sujeira):** Ausência de campos importantes como idade do hidrômetro nas planilhas.  
   * *Mitigação:* Estabelecer valor padrão baseado na média do setor hidráulico ou descartar registros muito antigos que representem viés.
2. **Risco 2 (Vazamento de Dados Pessoais - LGPD):** Exposição acidental de chaves de identificação de clientes da SABESP.  
   * *Mitigação:* Aplicar criptografia (hash SHA-256) ou remoção total de IDs e endereços no momento da extração dos arquivos CSV originais.
3. **Risco 3 (Falta de engajamento do patrocinador local):** Pouco tempo dos gestores da SABESP para validar os dashboards.  
   * *Mitigação:* Agendar reuniões curtas de 15 minutos semanais focadas em atas objetivas contendo apenas decisões chaves.
4. **Risco 4 (Falsa identificação de fraude):** O modelo sinalizar que uma residência desabitada por férias está cometendo fraude (queda de consumo legítima).  
   * *Mitigação:* Cruzar dados de faturamento de energia elétrica (quando disponível) ou definir regras de qualidade temporais mais flexíveis.
5. **Risco 5 (Estouro de Prazo do Cronograma):** Gargalo nas tarefas de modelagem lógica impedindo o início da análise.  
   * *Mitigação:* Usar controle visual de WIP (Work in Progress) no quadro Kanban com limite máximo de 2 tarefas ativas simultaneamente.

---

## 3. Repositório GitHub Sugerido
* **Estrutura de Pastas:**
  * `/docs/escopo-1/AE1` - Armazenamento do PDF de planejamento e Termo de Abertura.
  * `/docs/escopo-1/AE2` - Armazenamento da modelagem, dicionário e wireframes.
  * `/src/etl` - Scripts Python de carga e qualidade de dados.
  * `/src/analysis` - Cadernos Jupyter (EDA) e arquivos de visualização.
* **Conteúdo Inicial do README.md:**
  Descrever brevemente o projeto integrador de Redução de Perdas da SABESP, o público-alvo de Franco da Rocha e como rodar as análises estatísticas contidas no repositório.

---
---

# PARTE 2: ATIVIDADE DE ESTUDO 2 (AE2) - DESENHO DA SOLUÇÃO DE DADOS

## 1. Dicionário de Dados (Versão 1)

| Campo | Tipo Esperado | Descrição | Origem | Regra de Preenchimento / Validação |
| :--- | :--- | :--- | :--- | :--- |
| `id_ligacao` | INT (PK) | Identificador numérico e anonimizado do cliente. | Cadastro Comercial | Gerado sequencialmente. Obrigatório (Not Null). |
| `setor_hidraulico` | VARCHAR(50) | Setor hidráulico correspondente em Franco da Rocha. | Cadastro Técnico | Domínio de valores válidos pré-definidos (Ex: 'FR-01', 'FR-02'). |
| `classe_consumo` | VARCHAR(20) | Tipo de ligação ('Residencial', 'Comercial', 'Industrial'). | Faturamento | Obrigatório. Validação: Apenas valores do domínio permitido. |
| `idade_hidrometro_anos`| INT | Anos decorridos desde a última substituição. | Ordens de Serviço | Inteiro entre 0 e 50. Nulo preencher com valor padrão 10. |
| `media_consumo_24m` | DECIMAL(10,2) | Consumo médio mensal histórico em m³. | Histórico Faturamento| Valor numérico >= 0. |
| `consumo_mes_atual` | DECIMAL(10,2) | Volume medido no mês de referência atual. | Leitura Mensal | Valor numérico >= 0. Não pode ser nulo. |
| `flag_anomalia` | BOOLEAN | Marcador de suspeita de fraude/submedição (0 ou 1). | Regra de Negócio | Padrão: 0. Alterado para 1 se consumo atual for < 30% da média histórica. |

---

## 2. Modelo Lógico (Versão 1)

### Tabelas, PK/FK e Relacionamentos

```
[TB_CADASTRO_LIGACAO] (Tabela de Dimensão das Ligações)
  - id_ligacao : INT (PK)
  - setor_hidraulico : VARCHAR(50)
  - classe_consumo : VARCHAR(20)
  - idade_hidrometro_anos : INT
  - volume_contratado : DECIMAL(10,2)

[TB_HISTORICO_FATURAMENTO] (Tabela Fato de Leituras e Consumos)
  - id_faturamento : INT (PK)
  - id_ligacao : INT (FK referenciando TB_CADASTRO_LIGACAO)
  - data_leitura : DATE
  - consumo_mes_m3 : DECIMAL(10,2)
  - status_leitura : VARCHAR(20) ('Normal', 'Confirmada', 'Impedida')

[TB_ALERTAS_FISCALIZACAO] (Tabela de Ações e Ocorrências em Campo)
  - id_alerta : INT (PK)
  - id_ligacao : INT (FK referenciando TB_CADASTRO_LIGACAO)
  - data_alerta : DATE
  - probabilidade_fraude : DECIMAL(5,2)
  - status_alerta : VARCHAR(20) ('Gerado', 'Em Campo', 'Resolvido')
```

### Relacionamentos:
* `TB_CADASTRO_LIGACAO` (1) ----> (N) `TB_HISTORICO_FATURAMENTO` (Uma ligação tem várias leituras históricas mensais).
* `TB_CADASTRO_LIGACAO` (1) ----> (N) `TB_ALERTAS_FISCALIZACAO` (Uma ligação pode gerar vários alertas de anomalia ao longo do tempo).

---

## 3. Plano de Qualidade de Dados (Mín. 6 Checagens)

1. **Checagem de Duplicidade (id_ligacao):** Garantir que não existam linhas duplicadas com a mesma chave primária na tabela de cadastro comercial.
2. **Checagem de Nulos em Campos Obrigatórios:** Validar que `id_ligacao`, `classe_consumo` e `consumo_mes_atual` nunca sejam nulos na carga mensal de leituras.
3. **Validação de Domínio de Valores:** Garantir que o campo `classe_consumo` contenha exclusivamente as opções permitidas ('Residencial', 'Comercial', 'Industrial', 'Público').
4. **Consistência Temporal de Leituras:** Validar que a `data_leitura` da tabela fato nunca seja superior à data atual do sistema (dados futuros bloqueados).
5. **Faixa Plausível de Consumo:** Sinalizar leituras individuais absurdas (Ex: consumo residencial individual > 500 m³ em um único mês) para validação de erro de digitação do leiturista.
6. **Integridade Referencial:** Impedir a inserção de registros na tabela fato `TB_HISTORICO_FATURAMENTO` cujo `id_ligacao` correspondente não exista previamente na tabela cadastral `TB_CADASTRO_LIGACAO`.

---

## 4. Plano de Análise (EDA) e Produto Final

### Gráficos e Tabelas Necessários
* **Gráfico de Dispersão (Scatter Plot):** Eixo X: Idade do Hidrômetro | Eixo Y: Desvio do consumo mensal em relação à média. Objetivo: Identificar visualmente a partir de quantos anos o hidrômetro perde precisão mecânica (submedição).
* **Gráfico de Barras de Distribuição:** Total de alertas gerados agregados por bairro/setor hidráulico de Franco da Rocha, identificando os hot-spots de fraudes hidráulicas.
* **Tabela de Ranqueamento Crítico (Top 100):** Tabela contendo ligações com maior desvio percentual de consumo negativo, ordenadas pela probabilidade estimada de anomalia.

### Insights Esperados Respondidos
* A partir de 8 anos de idade do hidrômetro, há uma redução média estatística de 18% no volume de consumo faturado legítimo (comprovando submedição ativa por desgaste mecânico do aparelho).
* Ligações da classe comercial apresentam comportamento de anomalia de consumo mais abrupto que ligações residenciais, facilitando a detecção em até 2 leituras consecutivas.

### Esboço do Dashboard (Wireframe Simples)
O dashboard final (construído simuladamente no Power BI ou Web app Python) conterá 3 painéis dinâmicos principais:
* **Painel Geral (Visão Macro):** 
  * Indicadores gigantes no topo (Total de Água Recuperada em m³ | Assertividade do Modelo % | Total de Fiscalizações Pendentes).
  * Mapa calor de Franco da Rocha indicando áreas prioritárias.
* **Painel Setorial (Visão Operacional):** 
  * Gráfico de barras de alertas por Bairro e classe de consumo.
  * Tabela de hidrômetros antigos elegíveis para substituição prioritária.
* **Painel de Detalhe da Ligação (Filtro por Cliente ID):** 
  * Gráfico de linha temporal contendo consumo histórico vs. consumo atual, evidenciando o momento exato em que ocorreu a anomalia operacional.

---

## 5. Atualização do GitHub (Gestão de Issues)

Criação das seguintes 6 Issues no Kanban do repositório para a fase de execução técnica do projeto:
1. **Issue 1:** Criar scripts Python para anonimização dos dados de faturamento e conformidade LGPD.
2. **Issue 2:** Implementar banco de dados relacional simulado usando SQLite/PostgreSQL com base no modelo lógico definido.
3. **Issue 3:** Escrever testes de qualidade de dados de saneamento para checar integridade referencial e nulos.
4. **Issue 4:** Realizar Análise Exploratória de Dados (EDA) de consumo em Franco da Rocha e gerar estatísticas de desvio padrão.
5. **Issue 5:** Criar o protótipo funcional do Dashboard de redução de perdas no Streamlit/Power BI.
6. **Issue 6:** Gerar relatório conclusivo comparando o índice de assertividade do modelo com os dados de ordens de serviço.
