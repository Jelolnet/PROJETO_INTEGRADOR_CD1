# Projeto Integrador CD1: Redução de Perdas Aparentes de Água (SABESP)

Este repositório contém o planejamento e desenho de solução para o **Projeto Integrador Extensionista**, recortado regionalmente para a **Unidade de Negócio Norte da SABESP (Município de Franco da Rocha - SP)**.

O objetivo do projeto é o desenvolvimento de uma solução de dados que utilize inteligência de negócios e estatística para monitorar e detectar anomalias de consumo de água, identificando de forma proativa possíveis fraudes (ligações clandestinas) e submedição decorrente de hidrômetros antigos desgastados mecanicamente.

## 📁 Estrutura do Repositório

```text
├── docs/
│   └── escopo-1/
│       ├── AE1/
│       │   └── README.md   # Termo de Abertura, Briefing, EAP, Cronograma e Matriz de Riscos
│       └── AE2/
│           └── README.md   # Dicionário de Dados, Modelo Lógico, Plano de Qualidade e Análise
├── .gitignore
└── README.md               # Apresentação Geral do Projeto
```

## 🛠️ Tecnologias Planejadas
* **Banco de Dados:** PostgreSQL / SQLite para armazenamento estruturado do histórico.
* **Linguagem:** Python (Pandas, Numpy, Scikit-learn para detecção de anomalias/desvio padrão).
* **Visualização:** Power BI / Streamlit para o Dashboard dinâmico das equipes de fiscalização em campo.

## 👤 Autor
* **Jefferson Matos dos Santos**
* Projeto de Extensão Universitária - Big Data Analytics / Engenharia de Dados
