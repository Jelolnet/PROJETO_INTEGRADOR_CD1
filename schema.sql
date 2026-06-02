-- =====================================================================
-- SCHEMA DE BANCO DE DADOS POSTGRESQL - PROJETO INTEGRADOR
-- REDUÇÃO DE PERDAS APARENTES - SABESP FRANCO DA ROCHA - SP
-- ALUNO: JEFFERSON MATOS DOS SANTOS
-- =====================================================================

-- 1. Criação da Tabela de Dimensão: Cadastro de Ligações
CREATE TABLE TB_CADASTRO_LIGACAO (
    id_ligacao INT PRIMARY KEY,
    setor_hidraulico VARCHAR(50) NOT NULL,
    classe_consumo VARCHAR(20) NOT NULL,
    idade_hidrometro_anos INT DEFAULT 10,
    volume_contratado DECIMAL(10,2) NOT NULL,
    
    -- Restrições de Qualidade de Dados (CHECK constraints)
    CONSTRAINT chk_classe_consumo CHECK (classe_consumo IN ('Residencial', 'Comercial', 'Industrial', 'Público')),
    CONSTRAINT chk_idade_hidrometro CHECK (idade_hidrometro_anos BETWEEN 0 AND 50),
    CONSTRAINT chk_volume_contratado CHECK (volume_contratado >= 0)
);

-- Indexação para otimizar buscas por setor hidráulico (Franco da Rocha)
CREATE INDEX idx_setor_hidraulico ON TB_CADASTRO_LIGACAO(setor_hidraulico);


-- 2. Criação da Tabela Fato: Histórico de Faturamento Mensal
CREATE TABLE TB_HISTORICO_FATURAMENTO (
    id_faturamento SERIAL PRIMARY KEY,
    id_ligacao INT NOT NULL,
    data_leitura DATE NOT NULL,
    consumo_mes_m3 DECIMAL(10,2) NOT NULL,
    status_leitura VARCHAR(20) DEFAULT 'Normal',
    
    -- Chave Estrangeira e Integridade Referencial
    FOREIGN KEY (id_ligacao) REFERENCES TB_CADASTRO_LIGACAO(id_ligacao) ON DELETE CASCADE,
    
    -- Restrições de Qualidade de Dados (CHECK constraints)
    CONSTRAINT chk_consumo_positivo CHECK (consumo_mes_m3 >= 0.0),
    CONSTRAINT chk_status_leitura CHECK (status_leitura IN ('Normal', 'Confirmada', 'Impedida', 'Média'))
);

CREATE INDEX idx_faturamento_ligacao ON TB_HISTORICO_FATURAMENTO(id_ligacao);
CREATE INDEX idx_faturamento_data ON TB_HISTORICO_FATURAMENTO(data_leitura);


-- 3. Criação da Tabela Fato: Alertas de Fiscalização Gerados
CREATE TABLE TB_ALERTAS_FISCALIZACAO (
    id_alerta SERIAL PRIMARY KEY,
    id_ligacao INT NOT NULL,
    data_alerta DATE NOT NULL,
    probabilidade_fraude DECIMAL(5,2) NOT NULL,
    status_alerta VARCHAR(20) DEFAULT 'Gerado',
    
    FOREIGN KEY (id_ligacao) REFERENCES TB_CADASTRO_LIGACAO(id_ligacao) ON DELETE CASCADE,
    CONSTRAINT chk_probabilidade CHECK (probabilidade_fraude BETWEEN 0.0 AND 100.0),
    CONSTRAINT chk_status_alerta CHECK (status_alerta IN ('Gerado', 'Em Campo', 'Resolvido', 'Descartado'))
);


-- =====================================================================
-- CRIAÇÃO DE VIEWS ANALÍTICAS (REQUISITO AVALIATIVO RLF)
-- =====================================================================

-- View 1: Alertas Prioritários para Direcionamento de Campo (Assertividade)
CREATE OR REPLACE VIEW vw_alertas_prioritarios AS
SELECT 
    a.id_alerta,
    c.id_ligacao,
    c.setor_hidraulico AS bairro,
    c.classe_consumo AS perfil,
    c.idade_hidrometro_anos AS idade_hidrometro,
    a.probabilidade_fraude
FROM TB_ALERTAS_FISCALIZACAO a
JOIN TB_CADASTRO_LIGACAO c ON a.id_ligacao = c.id_ligacao
WHERE a.status_alerta = 'Gerado' AND a.probabilidade_fraude > 80.0
ORDER BY a.probabilidade_fraude DESC;


-- View 2: Estatísticas de Submedição por Idade de Hidrômetro
CREATE OR REPLACE VIEW vw_eficiencia_hidrometro AS
SELECT 
    c.idade_hidrometro_anos AS idade,
    COUNT(c.id_ligacao) AS total_ligacoes,
    ROUND(AVG(c.volume_contratado), 2) AS media_contratada,
    ROUND(AVG(f.consumo_mes_m3), 2) AS media_consumida_atual
FROM TB_CADASTRO_LIGACAO c
LEFT JOIN TB_HISTORICO_FATURAMENTO f ON c.id_ligacao = f.id_ligacao
WHERE f.data_leitura >= CURRENT_DATE - INTERVAL '3 months'
GROUP BY c.idade_hidrometro_anos
ORDER BY c.idade_hidrometro_anos ASC;
