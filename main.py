import random
from datetime import datetime

print("\nSISTEMA BANCÁRIO")
saldo = 2000
saldo_cofrinho = 0.0
chave_pix = ''
cpf = ''
email = ''
extrato = []
usuario_cadastrado = False
dados_pessoais = {}
nome = ''
data_nasc = ''


def relogio_transacoes():
    horario_transacoes = datetime.now()
    print(horario_transacoes)


def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11


def validar_email(email):
    if '@gmail.com' not in email:
        print('EMAIL INVALIDO!')
        return False
    else:
        print('EMAIL VALIDO!')
        return True

def validar_data_nasc(data_nasc):
    return len(data_nasc) == 8


def menu_cadastrar(dados_pessoais, cpf, email, nome, data_nasc):

    nome = input("NOME COMPLETO: ")
    while not nome:
        print('ESTE CAMPO É OBRIGATORIO!')       
        nome = input("NOME COMPLETO: ")
    
    while True:
        data_nasc = input("DATA NASC (DDMMAAAA): ")
        
        if validar_data_nasc(data_nasc):
            print('DATA DE NASCIMENTO CADASTRADA COM SUCESSO')
            break
        print('DATA DE NASCIMENTO INVALIDA OU INCORRETA')
    while True:
        cpf = input("CPF(SEM PONTUAÇÕES): ")

        if validar_cpf(cpf):
            print('CPF VALIDADO COM SUCESSO!')
            break
        print('CPF INVALIDO OU INEXISTENTE!')

    while True:
        email = input("EMAIL: ")
        if not email:
            print('CAMPO EMAIL NAO INFORMADO')
            continue
        if validar_email(email):
            print('EMAIL CADASTRADO COM SUCESSO')
            break

    dados_pessoais = {
             'nome' : nome,
             'dataNasc' : data_nasc,
             'cpf' : cpf,
             'email' : email
        }
    
    return dados_pessoais, cpf, email


def editar_cadastro(dados_pessoais, nome, cpf, email, data_nasc):

        print('[1]EDITAR DADOS')
        print('[2]VISUALIZAR DADOS')
        print('[3]INFORMAÇÕES BANCARIAS')
        opcao_dados = input("ESCOLHA UMA OPCAO: ")
        if opcao_dados == '1':
            dados_pessoais, cpf, email = menu_cadastrar(dados_pessoais, cpf, email, nome, data_nasc)
        elif opcao_dados == '2':
             print(f'''
|-------------------DADOS PESSOAIS--------------------|
NOME: {dados_pessoais['nome'].upper()}               
DATA NASCIMENTO: {dados_pessoais['dataNasc'].upper()}
CPF: {dados_pessoais['cpf'].upper()}                 
EMAIL: {dados_pessoais['email'].upper()}             
|-----------------------------------------------------|''')
        elif opcao_dados == '3':
            chaves_pix(cpf, email)
        else:
          print('DIGITE UMA OPCAO VALIDA!')
    
        return dados_pessoais, cpf, email

def chave_aleatoria():

    caracteres = list('abcdefryuiojna12789640')
    random.shuffle(caracteres)

    return ''.join(caracteres)


def chaves_pix(cpf, email):

    chaves_utilizadas = {
        'chave_aleatoria': chave_aleatoria(),
        'chave_cpf': cpf,
        'chave_email': email
    }

    print(f'''CHAVE ALEATORIA: {chaves_utilizadas['chave_aleatoria']}
CHAVE CPF: {chaves_utilizadas['chave_cpf']} 
CHAVE EMAIL: {chaves_utilizadas['chave_email']} 
''')
    
    return cpf, email

def mostrar_saldo():
    print(f"SEU SALDO ATUAL É R${saldo}")


def valor_saque(saldo, extrato):
    try:
        saque = int(input('VALOR DO SAQUE: R$ '))
        if saque > 0 and saque <= saldo:
            print(f'SAQUE REALIZADO R${saque}')
            saldo = saldo - saque
            extrato.append(f'SAQUE REALIZADO -R${saque}')
        else:
            print("VALOR INSUFICIENTE")

        return saldo
    except ValueError:
        print('''
    VALOR INVALIDO OU INSUFICIENTE
    TENTE NOVAMENTE!''')

def realizar_deposito(saldo, extrato):
    deposito = int(input('VALOR DO DEPOSITO: '))
    print(f'O VALOR DO DEPOSITO É DE {deposito}')
    saldo = saldo + deposito
    print(f"SEU NOVO SALDO É DE: {saldo}")
    extrato.append(f'DEPOSITO REALIZADO +R${deposito}')

    return saldo


def menu_transferencias(saldo, extrato):
    print('[1] TED')
    print('[2] PIX')
    print('[3] VOLTAR')
    opcao = input("ESCOLHA UMA OPCAO: ")
    if opcao == '1':
        saldo = ted_transferencias(saldo, extrato)
    elif opcao == '2':
        saldo = pix_transferencia(saldo, extrato)
    else:
        print('CARREGANDO...')
    return saldo


def ted_transferencias(saldo, extrato):
    try:
        nome_social = input('NOME COMPLETO: ')
        cpf_transferencia = input('CPF: ')
        cod_banco = input('BANCO: ')
        agencia = input('AGENCIA: ')
        num_conta = input('CONTA *****-*: ')

        dados_transferencias = [f'NOME: {nome_social}, CPF: {cpf_transferencia}, BANCO: {cod_banco}, AGENCIA: {agencia}, CONTA: {num_conta}']
        print(dados_transferencias)

        valor_transferencia = int(input('VALOR DA TRANSFERENCIA: '))
        if valor_transferencia > 0 and valor_transferencia <= saldo:
            saldo = saldo - valor_transferencia
            print(f'''TRANSFERENCIA CONCLUIDA
            R$ {valor_transferencia}''')
            extrato.append(f'TRANSFERENCIA TED -R${valor_transferencia}')
        else:
            print('VALOR INVALIDO')
        return saldo
    except ValueError:
        print('VALOR INVALIDO OU INSUFICIENTE')


def pix_transferencia(saldo, extrato):
    try:
        chave_pix = input("email, cpf, celular: ")
        print('DIGITE O VALOR ABAIXO')
        pix = int(input(' R$ : '))
        if pix > 0 and pix <= saldo:
            saldo = saldo - pix
            print(f'PIX REALIZADO COM SUCESSO: R${pix}')
            extrato.append(f'PIX REALIZADO -R${pix}')
        else:
            print('VALOR INVALIDO OU INSUFICIENTE ')

        return saldo
    except ValueError:
        print('VALOR INVALIDO OU INSUFICIENTE')


def extrato_bancario():
    print('---TRANSAÇÕES BANCARIAS:')
    for transaction in extrato:
        print(transaction)


def cofrinho_investimentos(saldo,extrato, saldo_cofrinho):
    print('------------------')
    print('AQUI O SEU DINHEIRO CRESCE!')
    print('110% DO CDI')
    mostrar_saldo()
    deposito_cofrinho = float(input('VALOR A GUARDAR: R$'))
    if deposito_cofrinho > 0 and deposito_cofrinho <= saldo:
        saldo -= deposito_cofrinho
        saldo_cofrinho += deposito_cofrinho
        print(f'VALOR GUARDADO NO COFRINHO R${saldo_cofrinho}')
        extrato.append(f'GUARDADO NO COFRINHO: -R${deposito_cofrinho}')
    else:
        print('VALOR INVALIDO OU INSUFICIENTE')
    return saldo, saldo_cofrinho


def rendimento_cofrinho(saldo_cofrinho):
    rend_diario = saldo_cofrinho * 0.00056
    return rend_diario


def extrato_cofrinho(saldo_cofrinho):
    rend_diario = rendimento_cofrinho(saldo_cofrinho)
    print(f' TOTAL GUARDADO R${saldo_cofrinho}')
    print(f'SEU DINHEIRO JA RENDEU R${rend_diario:.2f}!')


def menu_cofrinho(saldo, saldo_cofrinho, extrato):
    while True:
        print('''
        [1]GUARDAR DINHEIRO
        [2]VISUALIZAR RENDIMENTOS
        [3]VOLTAR   
        ''')
        opcao_cofrinho = input("ESCOLHA UMA OPCAO: ")
        if  opcao_cofrinho == '1':
            saldo, saldo_cofrinho = cofrinho_investimentos(saldo, saldo_cofrinho)
        elif opcao_cofrinho == '2':
            extrato_cofrinho(saldo_cofrinho)
        elif opcao_cofrinho == '3':
            print('PROCESSANDO...')
            break
        else:
            print('OPÇÃO INVALIDA!!')
    return saldo, saldo_cofrinho




def gerador_comprovante():
    for transaction in extrato:
        print('GERANDO COMPROVANTE...')
        print(f'''COMPROVANTE DE PAGAMENTO
        VALOR: R$ {transaction}
        CPF: {cpf}''')
    
  

def comprovante_transacoes(gerador_comprovante):
    print('''[1]VISUALIZAR COMPROVANTE
[2]SAIR ''')
    opcao = input('ESCOLHA UMA OPCAO: ')
    if opcao != '2':
        gerador_comprovante()
        relogio_transacoes()
        




def tela_cadastro(dados_pessoais, cpf, email, nome, data_nasc):
    global usuario_cadastrado
    while True:
        try:

            print('''                             
----------------------
[1] REALIZAR CADASTRO
----------------------                                                   
[2] SAIR
----------------------                                  
''')
            opcao_cadastro = input('ESCOLHA UMA OPCAO: ')

            if opcao_cadastro == '1':
                dados_pessoais, cpf, email = menu_cadastrar(
                    dados_pessoais, 
                    cpf, 
                    email, 
                    nome, 
                    data_nasc
                )

                usuario_cadastrado = True
                return dados_pessoais, cpf, email

            elif opcao_cadastro == '2':
                print('SAINDO...')
                exit()
            else:
                print('-'*50)
                print('DIGITE UMA OPÇÃO VALIDA!')
        except KeyboardInterrupt:
            print('\nPROCESSANDO...')
            print('OPERAÇÃO CANCELADA PELO USUARIO')
            break
dados_pessoais, cpf, email = tela_cadastro(
    dados_pessoais,
    cpf,
    email,
    nome,
    data_nasc
)


if usuario_cadastrado:
    try:
        while True:
            print("\n1-SALDO | 2-SAQUE | 3-DEPOSITO | 4-TRANSFERENCIAS | 5-INVESTIMENTOS | 6-EXTRATO | 7-EXIBIR/EDITAR CADASTRO | 8-SAIR\n ")
            opcao_menu = input('ESCOLHA UMA OPCAO: ')
            if opcao_menu == '1':
                mostrar_saldo()
            elif opcao_menu == '2':
                saldo = valor_saque(saldo, extrato)
                comprovante_transacoes(gerador_comprovante)
            elif opcao_menu == '3':
                saldo = realizar_deposito(saldo, extrato)
                comprovante_transacoes(gerador_comprovante)
            elif opcao_menu == '4':
                 saldo = menu_transferencias(saldo, extrato)
                 comprovante_transacoes(gerador_comprovante)
            elif opcao_menu == '5':
                saldo, saldo_cofrinho = menu_cofrinho(saldo, saldo_cofrinho, extrato)
                comprovante_transacoes(gerador_comprovante)
            elif opcao_menu == '6':
                extrato_bancario()
            elif opcao_menu == '7':
                    dados_pessoais, cpf, email = editar_cadastro(
        dados_pessoais,
        nome,
        cpf,
        email,
        data_nasc
        )
                    
            elif opcao_menu == '8':
                print('OBRIGADO PELA CONFIANÇA!')
                break
    except KeyboardInterrupt:
        print('\nPROCESSANDO...')
        print('OBRIGADO PELA CONFIANÇA!')
        exit()