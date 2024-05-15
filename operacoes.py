def menu_principal():
    menu = """
    OPERAÇÕES
    1 - Sacar
    2 - Depositar
    3 - Extrato
    4 - Cadastrar Cliente
    5 - Listar Clientes
    0 - Sair
    """
    return menu

def saque(operacao, saldo, quantidade):
    print("\n >>>>>", operacao)
    print("OBS.: Pode até 3 saques diários e com limite no máximo de R$500,00 por saque!")
    while True:
        erro = 0
        if quantidade > 3:
            print("\nÉ permitido realizar apenas 3 saques diários.")
            erro = 1
            break

        valor_saque_string = input("Digite o valor a ser sacado: ")
        valor_saque = float(valor_saque_string.replace(",", "."))

        if saldo < valor_saque:
            print(f"Saldo insuficiente para este valor do saque. - {saldo}" )
            erro = 1
        
        if valor_saque > 500:
            print("É permitido sacar no máximo R$500,00 por vez.")
            erro = 1
        
        if erro == 0:
            extrato.append(f"{operacao} de R$ {valor_saque}")
            saldo -= valor_saque  
            quantidade += 1
            print("Valor sacado com sucesso!")
        
        continuacao = input("Deseja continuar sacando? (Sim ou Não) ")
        if continuacao.upper() == "SIM" or continuacao.upper() == "S":
            continue
        elif continuacao.upper() == "NAO" or continuacao.upper() == "N" or continuacao.upper() == "NÃO":
            break
        else:
            print("Opção inválida, por favor, digite uma opção válida!")
        
    return saldo, quantidade

def deposito(operacao, saldo):
    print("\n >>>>>", operacao)
    while True:
        valor_deposito_string = input("Digite o valor do depósito: ")
        valor_deposito = float(valor_deposito_string.replace(",", "."))
        if valor_deposito <= 0:
            print("Valor de depósito precisa ser maior que 0 (zero), por favor digite um valor válido!")
        else:
            break
        
    extrato.append(f"{operacao} de R$ {valor_deposito}")
    saldo += valor_deposito
    print("Valor depositado com sucesso!")
    return saldo

def extrato_conta(operacao, extrato, saldo):
    print("\n >>>>>", operacao)
    contador = 1
    for transacao in extrato:
        print(f"{contador} - {transacao}")
        contador += 1
    print(f"Saldo: R$ {saldo}")

def cadastro_cliente(operacao, lista_clientes, codigo):
    print("\n >>>>>", operacao)
    codigo += 1
    print(">>> Dados Pessoais")
    nome = input("Nome completo: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")

    #validacao CPF
    cpf_string = input("CPF: ")
    cpf = ''.join(filter(str.isdigit, cpf_string))
    for cliente in lista_clientes:
        if cliente['cpf'] == cpf:
            print("CPF já cadastrado.")

    print(">>> Dados Endereço")
    logradouro = input("Logradouro: ")
    numero = input("Numero: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")

    #valida estado
    while True:
        estado = input("Siga Estado: ")
        if len(estado) != 2:
            print("Formato inválido para a sigla do estado. Por favor, digite um estado válido!")
            continue
        else:
            break

    endereco = logradouro + ", " + numero + " - " + bairro + " - " + cidade + "/" + estado.upper()

    lista_clientes.append({
        'codigo': codigo,
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Cliente cadastrado com sucesso!")
    return codigo

def listar_clientes(operacao, lista_clientes):
    print("\n >>>>>", operacao)
    for cliente in lista_clientes:
        for coluna, valor in cliente.items():
            print(f"{coluna.capitalize()}: {valor}")
        print("")

extrato = []
clientes = []
saldo_total = 0.0
quantidade_saque = 1
status = ""
codigo_cliente = 0

while True:
    while True:
        print (menu_principal())
        numoperacao = input("Digite o número da operação que deseja: ")

        if numoperacao == "1":
            descoperacao = 'Saque'
            saldo_total, quantidade_saque = saque(descoperacao, saldo_total, quantidade_saque)
        elif numoperacao == "2":
            descoperacao = 'Depósito'
            saldo_total = deposito(descoperacao, saldo_total)
        elif numoperacao == "3":
            descoperacao = 'Extrato'
            extrato_conta(descoperacao, extrato, saldo_total)
        elif numoperacao == "4":
            descoperacao = 'Cadastro'
            codigo_cliente = cadastro_cliente(descoperacao, clientes, codigo_cliente)
        elif numoperacao == "5":
            descoperacao = 'Lista de Clientes'
            listar_clientes(descoperacao, clientes)
        elif numoperacao == "0":
            descoperacao = 'Sair'
            break
        else:
            print("Numero de Operação inválido, por favor escolha uma opção válida!")

    if numoperacao == "0":
        print("Volte Sempre... Tchau!")
        break