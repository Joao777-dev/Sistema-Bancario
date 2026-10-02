from database.sqlite_utils import (
    inserir_dados_pessoais,
)

from cadastro_usuario.cadastro import (
    cadastro_usuario
)

from transacoes_usuario.transacoes import (
    exibir_saldo,
    saque_usuario,
    deposito_usuario,
    extrato_usuario,
    validacao_pix,
    pix_usuario
)
from InquirerPy import inquirer


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
                #tela_login(cpf_client)
                id_cliente = inserir_dados_pessoais(nome_client, data_nasc, cpf_client, tel_cliente)
                return id_cliente
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


def area_usuario(id_cliente):
    saldo_usuario = 200
    extrato = []
    while True:

        opcao_menu = inquirer.select(message = '',
                                     choices = [{'name':'[1]SALDO','value':'1'},
                                                {'name':'[2]SAQUE','value':'2'},
                                                {'name':'[3]DEPOSITO','value':'3'}, 
                                                {'name':'[4]PIX', 'value': '4'},                                              
                                                {'name':'[5]EXTRATO', 'value': '5'},
                                                {'name':'[6]SAIR', 'value': '5'}
                                                ]).execute()
        match opcao_menu:
            case '1':
                exibir_saldo(saldo_usuario)
            case '2':
               saldo_usuario, extrato = saque_usuario(saldo_usuario, extrato, id_cliente)
            case '3':
                saldo_usuario, extrato = deposito_usuario(saldo_usuario, extrato, id_cliente)
            case '4':
                validacao_pix()
                saldo_usuario = pix_usuario(saldo_usuario, id_cliente)
            case '5':
                extrato_usuario()
            case '6':
                break
    return saldo_usuario, extrato

id_cliente = menu_cadastro()
if id_cliente:
    area_usuario(id_cliente)
