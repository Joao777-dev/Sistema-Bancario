from validacao_usuario.validacao import(
    validar_cpf,
    validar_nasc,
    validar_tel
)

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