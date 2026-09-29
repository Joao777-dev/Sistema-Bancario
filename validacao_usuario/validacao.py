def validar_cpf(cpf_client):
    return cpf_client.isdigit() and len(cpf_client) == 11

def validar_nasc(data_nasc):
    return data_nasc.isdigit() and len(data_nasc) == 8

def validar_tel(tel_cliente):
    return tel_cliente.isdigit() and len(tel_cliente) == 11