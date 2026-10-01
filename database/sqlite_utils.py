import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

def tabela_dados_pessoais():
    cursor.execute('''CREATE TABLE IF NOT EXISTS dados_pessoais(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(30) NOT NULL,
    data_nasc VARCHAR(8),
    cpf VARCHAR(11),
    telefone VARCHAR(11)
    )''')
    conexao.commit()
    conexao.close()


def inserir_dados_pessoais(nome_client, data_nasc, cpf_client, tel_cliente):

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    sql_query = (''' INSERT INTO dados_pessoais (nome, data_nasc, cpf, telefone) VALUES (?, ?, ?, ?)
''')
    cursor.execute(sql_query, (nome_client, data_nasc, cpf_client, tel_cliente))
    id_cliente = cursor.lastrowid
    conexao.commit()
    conexao.close()
    print('DADOS INSERIDOS COM SUCESSO!')
    return id_cliente

def tabela_transacoes():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()        
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('''CREATE TABLE IF NOT EXISTS transacoes(
    id_transacao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tipo_transacao VARCHAR(30) NOT NULL,
    valor_transacao INTEGER NOT NULL,
    transacao_client INTEGER NOT NULL,
    data_transacao TEXT,
    CONSTRAINT fk_clientes_transactions 
    FOREIGN KEY (transacao_client)
    REFERENCES dados_pessoais(id)
)''') 
    conexao.commit()
    conexao.close()
    print('TABELA CRIADA COM SUCESSO!')

def inserir_transacoes(tipo_transacao, valor_transacao, transacao_client, data_transacao):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    sql_query = (''' INSERT INTO transacoes (tipo_transacao, valor_transacao, transacao_client, data_transacao) VALUES (?,?,?,?)
''') 
    cursor.execute(sql_query, (tipo_transacao, valor_transacao, transacao_client, data_transacao))
    conexao.commit()
    conexao.close()

def deletar_usuario(id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    sql_query = ("DELETE FROM dados_pessoais WHERE id = ?")
    number_id = (id,)
    cursor.execute(sql_query,number_id )
    conexao.commit()
    conexao.close()
    print('USUARIO DELETADO COM SUCESSO! ')


def deletar_tabela():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("DROP TABLE IF EXISTS transacoes")
    print('TABELA DELETADA COM SUCESSO!')
    conexao.commit()
    conexao.close()


def buscar_usuarios():
    cursor.execute('SELECT * FROM dados_pessoais')
    usuarios_consultados = cursor.fetchall()
    for users in usuarios_consultados:
        print(users)


def buscar_saldo(transacao_client):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    sql_query = ('''
    SELECT SUM (valor_transacao) FROM transacoes
    WHERE transacao_client = ?''')
    cursor.execute(sql_query, (transacao_client,))
    total_transacoes = cursor.fetchone()[0]
    
    saldo_atual = 200 - total_transacoes
    print(saldo_atual)

tabela_transacoes()