import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()




print('Sistema Bancario')


def tabela_dados_pessoais():
    cursor.execute('''CREATE TABLE IF NOT EXISTS dados_pessoais(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(30) NOT NULL,
    data_nasc DATE,
    cpf VARCHAR(11)
    )''')


def inserir_dados_pessoais(nome_client, data_nasc, cpf_client):
    sql = (''' INSERT INTO dados_pessoais (nome, data_nasc, cpf) VALUES (?, ?, ?)
''')
    cursor.execute(sql, (nome_client, data_nasc, cpf_client))

    conexao.commit()
    print('DADOS INSERIDOS COM SUCESSO!')
    
    return nome_client, data_nasc, cpf_client



def delete_table(id):
    sql = ("DELETE FROM dados_pessoais WHERE id = ?")
    number_id = (id,)
    cursor.execute(sql,number_id )
    conexao.commit()
    print('USUARIO DELETADO COM SUCESSO!')

#delete_table(10) 

def buscar_usuarios():
    cursor.execute =  ('''SELECT * FROM dados_pessoais''')
    usuarios_consultados = cursor.fetchall()
    for users in usuarios_consultados:
        print(users)
    conexao.commit()




def validar_cpf(cpf_client):
    return cpf_client.isdigit() and len(cpf_client) == 11

def validar_nasc(data_nasc):
    return data_nasc.isdigit() and len(data_nasc) == 8


def menu_cadastro():
    nome_client = input('NOME COMPLETO: ')
    while not nome_client: 
        nome_client = input('NOME COMPLETO: ')


    while True:
        data_nasc = input('DATA DE NASCIMENTO (DDMMAAAA): ')
        if validar_nasc(data_nasc):
            print('DATA DE NASCIMENTO CADASTRADA COM SUCESSO!')
            break
        else:
            print('DATA DE NASCIMENTO INVALIDA OU INCORETA!')
    while True:
        cpf_client = input('CPF: ')
        if validar_cpf(cpf_client):
            print('CPF CADASTRADO COM SUCESSO!')
            break
        else:
            print('CPF INVALIDO OU INCORRETO')

    return nome_client, data_nasc, cpf_client

#tabela_dados_pessoais()
#cursor.execute('''SELECT * FROM dados_pessoais''')






def tela_login(cpf_client):
    while True:
        cpf_login= input('CPF: ')
        if cpf_login == cpf_client:
            break
        else:
            print('CPF INCORRETO!')
    senha_client = input('CRIE SUA SENHA: ')
    return cpf_login, senha_client




def exibir_saldo(saldo_usuario):
    print(f'SEU SALDO É DE R${saldo_usuario}')
    return saldo_usuario


def saque_usuario(saldo_usuario):
    valor_saque = int(input('SAQUE R$: '))
    if valor_saque > 0 and valor_saque <= saldo_usuario:
        saldo_usuario -= valor_saque
        print(f'''
        SAQUE REALIZADO COM SUCESSO!
        R${valor_saque}
        ''')
    else:
        print(f'VALOR INVALIDO! {valor_saque}')
    return  saldo_usuario

def deposito_usuario(saldo_usuario):
    valor_deposito = int(input('DEPOSITO R$: '))
    if valor_deposito > 0 :
        saldo_usuario += valor_deposito
    else:
        print('VALOR INVALIDO')
    return saldo_usuario

def inciializar_cadastro():
    while True:
        print('''
        [1] REALIZAR CADASTRO
        [2] SAIBA MAIS
        [3] SAIR  
        ''')
        opcao_menu = input('OPCAO: ')
        if opcao_menu == '1':
            nome_client, data_nasc, cpf_client = menu_cadastro()
            nome_client, data_nasc, cpf_client = inserir_dados_pessoais(nome_client, data_nasc, cpf_client)
            break
        elif opcao_menu == '2':
            print('BLABLABLA')
            break
        elif opcao_menu == '3':
            break




print('''
TELA DE ACESSO!
BEM VINDO AO NOSSO APLICATVO!''')

#tela_login(cpf_client)

saldo_usuario = 200
def area_usuario():
    while True:
        print('''
        [1]SALDO
        [2]SAQUE
        [3]DEPOSITOS
        [4]SAIR
        ''')
        opcao = input('OPCAO: ')
        if opcao == '1':
            exibir_saldo(saldo_usuario)
        elif opcao == '2':
            saldo_usuario = saque_usuario(saldo_usuario)

        elif opcao == '3':
            saldo_usuario = deposito_usuario(saldo_usuario)
        elif opcao == '4':
            break
cursor.execute("DROP TABLE IF EXISTS transactions_clients")