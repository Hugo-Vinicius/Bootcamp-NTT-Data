menu = """

[d] Depositar
[s] Saque
[e] Extrato
[b] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        
        else:
             print("Valor inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
           print("Saldo insuficiente.")
        
        elif excedeu_limite:
            print("O valor excede o limite.")
        
        elif excedeu_saque:
            print("Limite máximo de saques permitido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Valor inválido.")

    elif opcao == "e":
        print("Extrato")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "b":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")