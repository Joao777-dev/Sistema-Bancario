from database.sqlite_utils import(
    tabela_transacoes,
    inserir_transacoes
)

def exibir_saldo(saldo_usuario):
    print(f'SEU SALDO É DE R${saldo_usuario}')
    return saldo_usuario


def saque_usuario(saldo_usuario, extrato, id_cliente):
    valor_saque = int(input('SAQUE R$: '))
    if valor_saque > 0 and valor_saque <= saldo_usuario:
        saldo_usuario -= valor_saque
        print(f'''
        SAQUE REALIZADO COM SUCESSO!
        R${valor_saque}
        ''')
        extrato.append(f'SAQUE R$ -{valor_saque}')
        inserir_transacoes("SAQUE", valor_saque, id_cliente)
    else:
        print(f'VALOR INVALIDO! {valor_saque}')
    return  saldo_usuario, extrato


def deposito_usuario(saldo_usuario, extrato, id_cliente):
    valor_deposito = int(input('DEPOSITO R$: '))
    if valor_deposito > 0 and valor_deposito <= 5000:
        saldo_usuario += valor_deposito
        extrato.append(f'DEPOSITO R$ +{valor_deposito}')
        inserir_transacoes("DEPOSITO", valor_deposito, id_cliente)
    else:
        print(f'VALOR INVALIDO OU EXCEDEU O LIMITE {valor_deposito}')
    return saldo_usuario, extrato

def extrato_usuario(extrato):
    for transacao in extrato:
        print(f'''
TIPO: {transacao}
DATA: 
''')