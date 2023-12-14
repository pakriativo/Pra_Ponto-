import sqlite3

def conectar_banco_dados(db_filename='db_ControleDePonto.db'):
    # Configurar a conexão
    connection = sqlite3.connect(db_filename)
    return connection

def criar_tabelas(connection):
    # Criar um cursor
    cursor = connection.cursor()

    # Criar a tabela de funcionários (se não existir)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            ID INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            FuncaoSetor TEXT NOT NULL,
            Nascimento TEXT,
            DataAdmissao TEXT,
            CargoPosto TEXT,
            CPF TEXT,
            HorarioEntradaNormal
        )
    ''')

    # Criar a tabela de controle de horas (se não existir)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS controle_horas (
            ID INTEGER PRIMARY KEY,
            Entrada TEXT,
            SaidaAlmoco TEXT,
            VoltaAlmoco TEXT,
            SaidaPausaPessoal TEXT,
            VoltaPausaPessoal TEXT,
            FimExpediente TEXT,
            FOREIGN KEY (ID) REFERENCES funcionarios(ID)
        )
    ''')

    # Salvar as alterações
    connection.commit()

def inserir_funcionario(connection, nome, funcao_setor, nascimento, data_admissao, cargo_posto, cpf, entrada):
# Criar um cursor
    cursor = connection.cursor()

    # Inserir dados na tabela de funcionários
    cursor.execute('''
        INSERT INTO funcionarios (Nome, FuncaoSetor, Nascimento, DataAdmissao, CargoPosto, CPF, HorarioEntradaNormal)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, funcao_setor, nascimento, data_admissao, cargo_posto, cpf, entrada))

    # Salvar as alterações
    connection.commit()

def inserir_controle_horas(connection, id_funcionario, entrada, saida_almoco, volta_almoco, saida_pausa, volta_pausa, fim_expediente):
    # Criar um cursor
    cursor = connection.cursor()

    # Inserir dados na tabela de controle de horas
    cursor.execute('''
        INSERT INTO controle_horas (ID, Entrada, SaidaAlmoco, VoltaAlmoco, SaidaPausaPessoal, VoltaPausaPessoal, FimExpediente)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (id_funcionario, entrada, saida_almoco, volta_almoco, saida_pausa, volta_pausa, fim_expediente))

    # Salvar as alterações
    connection.commit()

def consultar_dados_funcionario(connection):
    # Criar um cursor
    cursor = connection.cursor()

    # Consultar dados na tabela de funcionários
    cursor.execute('''
        SELECT * FROM funcionarios
    ''')

    # Retornar os resultados
    return cursor.fetchall()

def consultar_dados_controle_horas(connection):
    # Criar um cursor
    cursor = connection.cursor()

    # Consultar dados na tabela de controle de horas
    cursor.execute('''
        SELECT * FROM controle_horas
    ''')

    # Retornar os resultados
    return cursor.fetchall()

def fechar_conexao(connection):
 # Fechar a conexão
 connection.close() 
