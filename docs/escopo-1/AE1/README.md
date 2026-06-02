# ATIVIDADE DE ESTUDO 1 (AE1) - PLANEJAMENTO DO PROJETO
**Aluno:** Jefferson Matos dos Santos  
**Tema:** Redução de Perdas Aparentes de Água e Fraudes em Franco da Rocha - SP

---

## 1. Termo de Abertura + Briefing

### Contexto e Justificativa (Extensão)
As perdas aparentes de água (fraudes, ligações clandestinas e falhas/submedição de hidrômetros) são um enorme problema operacional, financeiro e socioambiental para o saneamento público. A SABESP atua em um território complexo na Região Metropolitana de São Paulo, onde o desperdício compromete a segurança hídrica. Este projeto propõe o uso de análise de dados e estatística para identificar padrões suspeitos de consumo e direcionar as equipes de fiscalização e troca de hidrômetros de forma inteligente, gerando retorno social (garantia de abastecimento coletivo), ambiental (preservação do recurso hídrico) e econômico.

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

## 2. Plano Inicial do Projeto

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
4. **Risco 4 (Falsa identificação de fraude):** O modelo sinalizar que uma residência desabitada por férias está cometendo fraude.  
   * *Mitigação:* Cruzar dados de faturamento de energia elétrica ou definir regras de qualidade temporais mais flexíveis.
5. **Risco 5 (Estouro de Prazo do Cronograma):** Gargalo nas tarefas de modelagem lógica impedindo o início da análise.  
   * *Mitigação:* Usar controle visual de WIP (Work in Progress) no quadro Kanban com limite máximo de 2 tarefas ativas simultaneamente.
