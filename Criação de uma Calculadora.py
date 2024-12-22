def calculadora_simples():
    print("Bem-vindo à Calculadora Simples!")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Escolha a operação:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    operacao = int(input("Digite a operação (1-4): "))

    if operacao == 1:
        print(f"Resultado: {n1} + {n2} = {n1 + n2}")
    elif operacao == 2:
        print(f"Resultado: {n1} - {n2} = {n1 - n2}")
    elif operacao == 3:
        print(f"Resultado: {n1} * {n2} = {n1 * n2}")
    elif operacao == 4:
        if n2 != 0:
            print(f"Resultado: {n1} / {n2} = {n1 / n2}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida.")
