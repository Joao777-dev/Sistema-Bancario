from database.sqlite_utils import (
    tabela_dados_pessoais,
    inserir_dados_pessoais,
    buscar_usuarios,
    deletar_usuario
)
from InquirerPy import inquirer



def validar_cpf(cpf_client):
    return cpf_client.isdigit() and len(cpf_client) == 11

def validar_nasc(data_nasc):
    return data_nasc.isdigit() and len(data_nasc) == 8

def validar_tel(tel_cliente):
    return tel_cliente.isdigit() and len(tel_cliente) == 11

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
    if valor_deposito > 0 and valor_deposito <= 5000:
        saldo_usuario += valor_deposito
    else:
        print(f'VALOR INVALIDO OU EXCEDEU O LIMITE {valor_deposito}')
    return saldo_usuario



def cadastro_usuario():
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
    while True:
        tel_cliente = input('TEL: +55')
        if validar_tel:
            print('TELEFONE CADASTRADO COM SUCESSO!')
            break
        else:
            print(f'NUMERO INVALIDO OU INCORRETO {tel_cliente}')

    return nome_client, data_nasc, cpf_client, tel_cliente




def menu_cadastro():
    while True:
        opcao_menu = inquirer.select(
        message = 'CADASTRE-SE',
        choices =[{'name':'[1] REALIZAR CADASTRO',"value":"1"},
                  {'name':'[2] SAIBA MAIS', "value": "2"},
                  {'name':'[3] SAIR', 'value':'3'}]
        ).execute()
        match opcao_menu:
            case '1':
                nome_client, data_nasc, cpf_client, tel_cliente = cadastro_usuario()
                tela_login(cpf_client)
                nome_client, data_nasc, cpf_client, tel_cliente = inserir_dados_pessoais(nome_client, data_nasc, cpf_client, tel_cliente)
                break
            case '2':
                print('BLABLABLA')
            case '3':
                break


def tela_login(cpf_client):
    while True:
        cpf_login= input('CPF: ')
        if cpf_login == cpf_client:
            break
        else:
            print('CPF INCORRETO!')
    senha_client = input('CRIE SUA SENHA: ')
    return cpf_login, senha_client


def area_usuario():
    saldo_usuario = 200
    while True:

        opcao_menu = inquirer.select(message = '',
                                     choices = [{'name':'[1]SALDO','value':'1'},
                                                {'name':'[2]SAQUE','value':'2'},
                                                {'name':'[3]DEPOSITO','value':'3'}, 
                                                {'name':'[4]SAIR', 'value': '4'}
                                                ]).execute()
        match opcao_menu:
            case '1':
                exibir_saldo(saldo_usuario)
            case '2':
                saldo_usuario = saque_usuario(saldo_usuario)
            case '3':
                saldo_usuario = deposito_usuario(saldo_usuario)
            case '4':
                break
    return saldo_usuario

menu_cadastro()
area_usuario()