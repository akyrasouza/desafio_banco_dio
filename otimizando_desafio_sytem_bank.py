menu = """
==== Banco DigitalPy ======
||                     ||
|| [d] Depositar       ||
|| [s] Sacar           ||
|| [e] Extrato         ||
|| [nu] Novo usuário   ||
|| [nc] Nova Conta     ||
|| [lc] Listar Conta   ||
|| [q] Sair            ||
=========================
==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3
AGENCIA = "0001"

#Função Depósito
def depositar(saldo,valor,extrato,/):  
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
       print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato
#Função Saque 
def sacar(*,saldo,valor,extrato,limite,numero_saques, limite_saques):
   
    excedeu_saldo = valor > saldo
    saldo_total = saldo + limite
    excedeu_saldo_total = valor > saldo_total
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo_total:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        if excedeu_saldo:
            altera_limite = valor - saldo
            saldo = 0
            limite -= altera_limite
            extrato += f"Saque utilizando limite \tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
            
        else:
            saldo -= valor
            extrato += f"Saque \tR$ {valor:.2f}\n"
            numero_saques += 1
           
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato,limite

#Função Extrato
def exibir_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(f"Limite disponível: R${limite:.2f}")
    print("==========================================")

#Função Cadastrar Usuaário
def cadastrar_usuario(usuario):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dia-mês-ano): ")
    endereco = input("Informe o endereço(Rua, n° - bairro - cidade/sigla estafo): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})

    print("=== Usuários cadastrado com sucesso! ===")

#Função Filtrar Usuário
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#Função Cadastrar Conta
def cadastrar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o CPF do usuário:  ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta cadastrada com sucesso! ===")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@") 

#Função Listar Contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            Conta-Corrente: \t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

#Opções
while True:

    opcao = input(menu)

    if opcao == "d":
        valor= float(input("Informe o valor do depósito: "))
        saldo,extrato = depositar(saldo,valor, extrato)
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo,extrato,limite= sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
       exibir_extrato(saldo,extrato=extrato)

    elif opcao == "nu":
        cadastrar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)
    
        if conta:
            contas.append(conta)
    
    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        print("Operação Finalizada! \nObrigada por usar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

   