import os
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def executar_pipeline():
    print("--- INICIANDO PIPELINE DE ETL & EDA DA SABESP ---")
    
    # 1. CARGA DOS DADOS
    if not os.path.exists("cadastro_ligacoes.csv") or not os.path.exists("historico_faturamento.csv"):
        print("Erro: Arquivos CSV de entrada não encontrados. Execute gerar_dados_sabesp.py primeiro.")
        return
        
    df_cad = pd.read_csv("cadastro_ligacoes.csv")
    df_fat = pd.read_csv("historico_faturamento.csv")
    
    print(f"Cadastro carregado: {df_cad.shape[0]} registros.")
    print(f"Histórico carregado: {df_fat.shape[0]} faturamentos.")
    
    # 2. AS 6 CHECAGENS DE QUALIDADE DE DADOS (AE2)
    print("\n[QUALIDADE DE DADOS] Executando as 6 checagens de validação...")
    
    # Checagem 1: Duplicidade na PK (id_ligacao)
    duplicados_pk = df_cad.duplicated(subset=['id_ligacao']).sum()
    print(f"1. Checagem de Duplicidades na PK: {duplicados_pk} duplicados encontrados.")
    
    # Checagem 2: Valores Nulos em Campos Críticos
    nulos_cad = df_cad[['id_ligacao', 'classe_consumo', 'setor_hidraulico']].isnull().sum().sum()
    nulos_fat = df_fat[['id_faturamento', 'id_ligacao', 'consumo_mes_m3']].isnull().sum().sum()
    print(f"2. Checagem de Nulos: {nulos_cad + nulos_fat} valores nulos encontrados.")
    
    # Checagem 3: Validação de Domínio (classe_consumo)
    classes_validas = ["Residencial", "Comercial", "Industrial"]
    invalidos_classe = (~df_cad['classe_consumo'].isin(classes_validas)).sum()
    print(f"3. Validação de Domínio (classes permitidas): {invalidos_classe} registros inválidos.")
    
    # Checagem 4: Consistência Temporal (Sem datas futuras)
    df_fat['data_leitura'] = pd.to_datetime(df_fat['data_leitura'])
    datas_futuras = (df_fat['data_leitura'] > pd.Timestamp('2026-06-02')).sum()
    print(f"4. Consistência Temporal (Datas futuras): {datas_futuras} registros inválidos.")
    
    # Checagem 5: Faixas Plausíveis de Consumo (Sem consumos negativos ou absurdos > 1000m3)
    consumo_invalido = ((df_fat['consumo_mes_m3'] < 0) | (df_fat['consumo_mes_m3'] > 1000)).sum()
    print(f"5. Faixas Plausíveis de Consumo (0 a 1000 m³): {consumo_invalido} registros inválidos.")
    
    # Checagem 6: Integridade Referencial (FK id_ligacao no faturamento)
    orfaos = (~df_fat['id_ligacao'].isin(df_cad['id_ligacao'])).sum()
    print(f"6. Integridade Referencial (FKs órfãs): {orfaos} órfãos encontrados.")
    
    # 3. ETL & DETECÇÃO DE ANOMALIAS
    print("\n[ETL] Executando regras de detecção de anomalias (Perdas Aparentes)...")
    
    # Calcular média de consumo histórico (primeiros 12 meses, meses de 0 a 11)
    df_fat_ordenado = df_fat.sort_values(by=['id_ligacao', 'data_leitura'])
    df_fat_12m = df_fat_ordenado.groupby('id_ligacao').head(12)
    df_media_12m = df_fat_12m.groupby('id_ligacao')['consumo_mes_m3'].mean().reset_index()
    df_media_12m = df_media_12m.rename(columns={'consumo_mes_m3': 'media_historica'})
    
    # Obter o último mês (mês 24, índice de faturamento mais recente)
    df_ultimo_mes = df_fat_ordenado.groupby('id_ligacao').tail(1)
    
    # Mesclar dados para análise
    df_analise = pd.merge(df_cad, df_media_12m, on='id_ligacao')
    df_analise = pd.merge(df_analise, df_ultimo_mes, on='id_ligacao')
    
    # Regra de Detecção: Consumo atual < 30% da média histórica E média histórica > 3 m³ (para evitar falsos alertas em consumos baixos legítimos)
    df_analise['porcentagem_consumo'] = (df_analise['consumo_mes_m3'] / df_analise['media_historica'])
    df_analise['flag_anomalia'] = ((df_analise['porcentagem_consumo'] < 0.3) & (df_analise['media_historica'] > 3.0)).astype(int)
    
    anomalias_totais = df_analise['flag_anomalia'].sum()
    print(f"ETL Concluído: {anomalias_totais} anomalias (suspeitas de fraude/submedição) identificadas nas ligações.")
    
    # 4. GERAÇÃO DOS GRÁFICOS OPERACIONAIS (EDA)
    print("\n[EDA] Gerando gráficos de análise operacional...")
    os.makedirs(os.path.join("docs", "escopo-1"), exist_ok=True)
    
    # Gráfico 1: Idade do Hidrômetro vs Queda de Consumo (Submedição mecânica)
    plt.figure(figsize=(8, 5))
    df_filtrado_idade = df_analise[df_analise['flag_anomalia'] == 1]
    plt.scatter(df_analise['idade_hidrometro_anos'], df_analise['porcentagem_consumo'] * 100, alpha=0.3, color='#184c78')
    plt.axhline(30, color='red', linestyle='--', label='Limiar de Alerta (30% do Consumo Médio)')
    plt.title("Relação: Idade do Hidrômetro vs Desempenho de Medição", fontsize=12, fontweight='bold', color='#184c78')
    plt.xlabel("Idade do Hidrômetro (Anos)")
    plt.ylabel("Desempenho de Consumo em Relação à Média (%)")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join("docs", "escopo-1", "grafico_dispersao.png"))
    plt.close()
    print("Gráfico 1 (Dispersão) salvo em docs/escopo-1/grafico_dispersao.png")
    
    # Gráfico 2: Alertas de Anomalia por Bairro em Franco da Rocha - SP
    plt.figure(figsize=(8, 5))
    df_bairros = df_analise.groupby('setor_hidraulico')['flag_anomalia'].sum().sort_values(ascending=False)
    df_bairros.plot(kind='bar', color='#3c8dbc', edgecolor='#184c78')
    plt.title("Alertas de Perda Aparente por Setor Hidráulico (Franco da Rocha)", fontsize=12, fontweight='bold', color='#184c78')
    plt.xlabel("Setor Hidráulico (Bairro)")
    plt.ylabel("Total de Alertas Gerados (Queda de Medição)")
    plt.grid(axis='y', linestyle=':', alpha=0.6)
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(os.path.join("docs", "escopo-1", "grafico_barras.png"))
    plt.close()
    print("Gráfico 2 (Barras) salvo em docs/escopo-1/grafico_barras.png")
    
    # 5. BANCO DE DADOS LOCAL (SIMULAÇÃO POSTGRESQL COM SQLITE)
    print("\n[BANCO DE DADOS] Carregando as bases limpas no SQLite relacional...")
    conn = sqlite3.connect("SABESP_Franco_da_Rocha.db")
    cursor = conn.cursor()
    
    # Salvar tabelas
    df_cad.to_sql("TB_CADASTRO_LIGACAO", conn, if_exists="replace", index=False)
    df_fat.to_sql("TB_HISTORICO_FATURAMENTO", conn, if_exists="replace", index=False)
    
    # Criar tabela de Alertas
    df_alertas_salvar = df_analise[df_analise['flag_anomalia'] == 1][['id_ligacao', 'data_leitura', 'porcentagem_consumo']]
    df_alertas_salvar['probabilidade_fraude'] = (1.0 - df_alertas_salvar['porcentagem_consumo']) * 100
    df_alertas_salvar['status_alerta'] = "Gerado"
    df_alertas_salvar = df_alertas_salvar.rename(columns={'data_leitura': 'data_alerta'}).reset_index(drop=True)
    df_alertas_salvar['id_alerta'] = df_alertas_salvar.index + 1
    df_alertas_salvar = df_alertas_salvar[['id_alerta', 'id_ligacao', 'data_alerta', 'probabilidade_fraude', 'status_alerta']]
    df_alertas_salvar.to_sql("TB_ALERTAS_FISCALIZACAO", conn, if_exists="replace", index=False)
    
    # Testar uma view SQL complexa de auditoria
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS vw_alertas_prioritarios AS
        SELECT a.id_alerta, c.id_ligacao, c.setor_hidraulico, c.classe_consumo, c.idade_hidrometro_anos, a.probabilidade_fraude
        FROM TB_ALERTAS_FISCALIZACAO a
        JOIN TB_CADASTRO_LIGACAO c ON a.id_ligacao = c.id_ligacao
        WHERE a.probabilidade_fraude > 80.0
        ORDER BY a.probabilidade_fraude DESC;
    """)
    conn.commit()
    
    print("Sucesso: Banco relacional SQLite simulado criado com tabelas e Views operacionais!")
    
    # Amostra de resultado da View
    cursor.execute("SELECT * FROM vw_alertas_prioritarios LIMIT 5;")
    res = cursor.fetchall()
    print("\n--- AMOSTRA DA VIEW SQL DE ALERTAS PRIORITÁRIOS (TOP 5 DE FRAUDES) ---")
    for r in res:
        print(f"Alerta ID: {r[0]} | Ligação: {r[1]} | Bairro: {r[2]} | Perfil: {r[3]} | Idade Hidrômetro: {r[4]} anos | Risco Fraude: {r[5]:.2f}%")
    print("---------------------------------------------------------------------")
    
    conn.close()

if __name__ == "__main__":
    executar_pipeline()
