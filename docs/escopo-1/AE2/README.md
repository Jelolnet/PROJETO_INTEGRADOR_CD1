# ATIVIDADE DE ESTUDO 2 (AE2) - DESENHO DA SOLUÇÃO DE DADOS
**Aluno:** Jefferson Matos dos Santos  
**Tema:** Redução de Perdas Aparentes de Água e Fraudes em Franco da Rocha - SP

---

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

```text
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
