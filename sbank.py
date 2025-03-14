menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[s] Sair

=> """

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
            extrato += f"Valor para depósito: R$ {valor:.2f}\n"

        else:
            print("###### O valor informado é inválido.######")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("####### Saldo suficiente.#######")

        elif excedeu_limite:
            print("###### Limite diário excedidod.######")

        elif excedeu_saques:
            print("###### Número saques excedido.######")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("##### O valor informado é inválido.####")

    elif opcao == "e":
        print("\n_*_*_*_*_*_EXTRATO_*_*_*_*_*_")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")