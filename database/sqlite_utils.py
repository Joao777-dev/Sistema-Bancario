import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

def tabela_dados_pessoais():
    cursor.execute('''CREATE TABLE IF NOT EXISTS dados_pessoais(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(30) NOT NULL,
    data_nasc DATE,
    cpf VARCHAR(11)
    )''')


def inserir_dados_pessoais(nome_client, data_nasc, cpf_client):
    sql_query = (''' INSERT INTO dados_pessoais (nome, data_nasc, cpf) VALUES (?, ?, ?)
''')
    cursor.execute(sql_query, (nome_client, data_nasc, cpf_client))

    conexao.commit()
    print('DADOS INSERIDOS COM SUCESSO!')
    
    return nome_client, data_nasc, cpf_client



def deletar_usuario(id):
    sql_query = ("DELETE FROM dados_pessoais WHERE id = ?")
    number_id = (id,)
    cursor.execute(sql_query,number_id )
    conexao.commit()
    print('USUARIO DELETADO COM SUCESSO! ')


def deletar_tabela():
    cursor.execute("DROP TABLE IF EXISTS name_table")
    print('TABELA DELETADA COM SUCESSO!')
    conexao.commit()


def buscar_usuarios():
    cursor.execute('SELECT * FROM dados_pessoais')
    usuarios_consultados = cursor.fetchall()
    for users in usuarios_consultados:
        print(users)