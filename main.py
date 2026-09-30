from database.sqlite_utils import (
    tabela_dados_pessoais,
    inserir_dados_pessoais,
    buscar_usuarios,
    deletar_usuario,
    tabela_transacoes,
    inserir_transacoes
)
from validacao_usuario.validacao import(
    validar_cpf,
    validar_nasc,
    validar_tel
)

from cadastro_usuario.cadastro import (
    cadastro_usuario
)

from transacoes_usuario.transacoes import (
    exibir_saldo,
    saque_usuario,
    deposito_usuario,
    extrato_usuario
)
from InquirerPy import inquirer

from datetime import date, time, datetime



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
                                                {'name':'[4]EXTRATO', 'value': '4'},                                              
                                                {'name':'[5]SAIR', 'value': '5'}
                                                ]).execute()
        match opcao_menu:
            case '1':
                exibir_saldo(saldo_usuario)
            case '2':
               saldo_usuario, extrato = saque_usuario(saldo_usuario, extrato, id_cliente)
            case '3':
                saldo_usuario, extrato = deposito_usuario(saldo_usuario, extrato, id_cliente)
            case '4':
                extrato_usuario(extrato)
            case '5':
                break
    return saldo_usuario, extrato

id_cliente = menu_cadastro()
if id_cliente:
    area_usuario(id_cliente)
