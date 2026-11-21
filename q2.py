
saldo = 500.00
operacoes = 0

while True:
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Consultar saldo")
    print("2 - Realizar depósito")
    print("3 - Realizar saque")
    print("4 - Consultar quantidade de operações")
    print("5 - Encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 2:
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            operacoes += 1
            print("Depósito realizado!")
        else:
            print("Valor inválido!")

    elif opcao == 3:
        valor = float(input("Valor do saque: "))

        if valor > 0 and valor <= saldo:
            saldo -= valor
            operacoes += 1
            print("Saque realizado!")
        else:
            print("Operação recusada!")

    elif opcao == 4:
        print("Total de operações:", operacoes)

    elif opcao == 5:
        print("Caixa eletrônico encerrado!")
        break

    else:
        print("Opção inválida!")
