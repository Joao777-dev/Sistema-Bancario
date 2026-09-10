import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

def tabela_dados_pessoais():
    cursor.execute('''CREATE TABLE IF NOT EXISTS dados_pessoais(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(30) NOT NULL,
    data_nasc VARCHAR(8),
    cpf VARCHAR(11)
    )''')
    conexao.commit()
    conexao.close()



def inserir_dados_pessoais(nome_client, data_nasc, cpf_client):

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    sql_query = (''' INSERT INTO dados_pessoais (nome, data_nasc, cpf) VALUES (?, ?, ?)
''')
    cursor.execute(sql_query, (nome_client, data_nasc, cpf_client))

    conexao.commit()
    conexao.close()
    print('DADOS INSERIDOS COM SUCESSO!')
    
    return nome_client, data_nasc, cpf_client

def tabela_transacoes():
    cursor.execute('''CREATE TABLE IF NOT EXISTS transacoes(
    id_transacao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tipo_transacao VARCHAR(30),
    transacao_client INTEGER,
    CONSTRAINT fk_clientes_transactions 
    FOREIGN KEY (transacao_client)
    REFERENCES dados_pessoais(id)
)''') 
    conexao.commit()
    conexao.close()

def inserir_transacoes(tipo_transacao, transacao_client):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    sql_query = (''' INSERT INTO transacoes (tipo_transacao, transacao_client) VALUES (?,?)
''') 
    cursor.execute(sql_query, (tipo_transacao, transacao_client))
    conexao.commit()
    conexao.close()

def deletar_usuario(id):
    sql_query = ("DELETE FROM dados_pessoais WHERE id = ?")
    number_id = (id,)
    cursor.execute(sql_query,number_id )
    conexao.commit()
    conexao.close()
    print('USUARIO DELETADO COM SUCESSO! ')


def deletar_tabela():
    cursor.execute("DROP TABLE IF EXISTS dados_pessoais")
    print('TABELA DELETADA COM SUCESSO!')
    conexao.commit()
    conexao.close()


def buscar_usuarios():
    cursor.execute('SELECT * FROM dados_pessoais')
    usuarios_consultados = cursor.fetchall()
    for users in usuarios_consultados:
        print(users)

tabela_dados_pessoais()