import csv
import random
from datetime import datetime, timedelta

# Configurações de simulação
NUM_LIGACOES = 5000
BAIRROS = ["Centro", "Parque Vitoria", "Jardim Luciana", "Vila Irma", "Jardim Uniao"]
CLASSES = ["Residencial", "Comercial", "Industrial"]

def gerar_cadastro():
    print("Gerando cadastro de ligações...")
    cadastro = []
    for i in range(1, NUM_LIGACOES + 1):
        id_ligacao = i
        setor = random.choice(BAIRROS)
        classe = random.choices(CLASSES, weights=[0.80, 0.17, 0.03])[0]
        
        # Hidrômetros antigos propensos a submedição
        idade = random.randint(0, 15)
        
        # Volume contratado baseado na classe
        if classe == "Residencial":
            vol_contratado = 10.0
        elif classe == "Comercial":
            vol_contratado = 20.0
        else:
            vol_contratado = 50.0
            
        cadastro.append({
            "id_ligacao": id_ligacao,
            "setor_hidraulico": setor,
            "classe_consumo": classe,
            "idade_hidrometro_anos": idade,
            "volume_contratado": vol_contratado
        })
        
    with open("cadastro_ligacoes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=cadastro[0].keys())
        writer.writeheader()
        writer.writerows(cadastro)
    return cadastro

def gerar_faturamento(cadastro):
    print("Gerando histórico de faturamento (24 meses)...")
    faturamento = []
    id_fat = 1
    
    start_date = datetime(2024, 6, 1)
    
    for lig in cadastro:
        id_lig = lig["id_ligacao"]
        classe = lig["classe_consumo"]
        idade = lig["idade_hidrometro_anos"]
        
        # Consumo base mensal do cliente
        if classe == "Residencial":
            consumo_base = random.uniform(8.0, 25.0)
        elif classe == "Comercial":
            consumo_base = random.uniform(20.0, 80.0)
        else:
            consumo_base = random.uniform(100.0, 400.0)
            
        # Simular injeção de anomalias (Fraude ou Desgaste)
        tipo_anomalia = "nenhuma"
        # 4% de chance de fraude (queda abrupta)
        if random.random() < 0.04:
            tipo_anomalia = "fraude"
        # Hidrômetros com mais de 8 anos sofrem submedição gradual
        elif idade >= 8 and random.random() < 0.35:
            tipo_anomalia = "submedicao"
            
        # Gera 24 leituras mensais
        for m in range(24):
            leitura_date = start_date + timedelta(days=m * 30.5)
            
            # Consumo normal com variação sazonal de 15%
            consumo = consumo_base * random.uniform(0.85, 1.15)
            
            # Aplicação dos padrões de anomalia
            if tipo_anomalia == "fraude" and m >= 18:
                # Queda abrupta de 85% após o 18º mês (simulando desvio/fraude)
                consumo = consumo * 0.15
            elif tipo_anomalia == "submedicao" and m >= 12:
                # Perda mecânica gradual a partir do 12º mês
                consumo = consumo * (1.0 - (idade * 0.04))
                
            faturamento.append({
                "id_faturamento": id_fat,
                "id_ligacao": id_lig,
                "data_leitura": leitura_date.strftime("%Y-%m-%d"),
                "consumo_mes_m3": round(max(0.1, consumo), 2),
                "status_leitura": "Normal" if random.random() < 0.98 else "Confirmada"
            })
            id_fat += 1
            
    with open("historico_faturamento.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=faturamento[0].keys())
        writer.writeheader()
        writer.writerows(faturamento)
    print("Dados mocados da SABESP gerados com sucesso!")

if __name__ == "__main__":
    cad = gerar_cadastro()
    gerar_faturamento(cad)
