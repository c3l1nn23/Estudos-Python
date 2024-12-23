
def menu():

    print("==========================================")
    print("  Seja bem-vindo à Calculadora Científica  ")
    print("==========================================")
    print("Selecione uma opção:")
    print("1. Calculadora Simples (Soma, Subtração, Multiplicação e Divisão) :")
    print ("2. Gerar Sequência de Fibonacci :")
    print ("3. Converter o numero para ( Binário, Hexadecimal e Octal) :")
    print ("4. Fatorar um numero :")
    print ("5. Verificar se um numero é perfeito :")
    print ("6. Verificar a tabuada de um numero :")
    print ("7. Verificar se um numero é primo :")
    print ("8. Verificar aprovação de emprestimo :")
    print ("9. Verificar se um numero é par ou impar :")
    print ("10. Fazer uma Progreção Aritimedica :")
    print ("0 . Sair")
    print ('=====================================================================')
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
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence
def converter_numero(numero):
    binario = bin(numero)[2:]
    hexadecimal = hex(numero)[2:]
    octal = oct(numero)[2:]
    return binario, hexadecimal, octal
def fatorar_numero(numero):
    if numero < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    fatorial = 1
    for c in range(numero, 0, -1):
        fatorial *= c
    return fatorial
def numero_perfeito():
    n = int(input("Digite o numero: "))
    soma = 0
    
    for divisor in range(1,n):
        if n % divisor == 0:
            soma += divisor 
    if n == soma:
        print(f"O numero {n} é perfeito")
    else: 
        print(f"O numero {n} nao é perfeito\n")
def tabuada():
    numero = 0 
    numero = int(input("Digite um número para ver a tabuada: "))  
    for c in range(1, 11):
        print(f"{numero} x {c} = {numero * c}")
def numero_primo():
    numero = int(input("Digite um numero : "))
    x = 0 
    for i in range(1,numero + 1):
        if numero % i == 0:
            x = x + 1
    if x == 2 :
        print (f"{numero} é primo")
    else:
        print (f"{numero} não é primo")
def emprestimo(valor_casa, salario, anos):
    valor_casa = float(input("Digite o valor do item: R$ "))
    salario = float(input("Digite o salário do comprador: R$ "))
    anos = int(input("Em quantos anos deseja pagar? "))

    meses = anos * 12
    prestacao_mensal = valor_casa / meses

    limite = salario * 0.30

    print(f"\nPara pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será de R${prestacao_mensal:.2f}.")
    if prestacao_mensal <= limite:
        print("Empréstimo APROVADO!")
    else:
        print("Empréstimo NEGADO! A prestação excede 30% do salário.")
def progressao_aritimetica():
    n = int(input("Digite o primeiro termo da PA: "))
    razao = int(input("Digite a razão da PA: "))
    for c in range(1, 11):
        print(n, end=" ")
        n += razao
        while c == 10:
            print("PAUSA")
            c = int(input("Quantos termos você quer mostrar a mais? "))
            if c == 0:
                break
            else:
                for i in range(1, c+1):
                    print(n, end=" ")
                    n += razao
    print("FIM")
escolha = 0
while True:
    menu()
    escolha = int(input("Digite a opção desejada : "))
    if escolha == 0:
        print("Obrigado por usar a Calculadora Científica!")
        break
    elif escolha == 1:
        calculadora_simples()
        input("Pressione Enter para voltar ao menu...")
    elif escolha == 2:
        n = int(input("Quantos termos deseja ver da Sequência de Fibonacci : "))
        result = fibonacci(n)
        print(result)
        input("Pressione Enter para voltar ao menu...")
    elif escolha == 3:
        numero = int(input("Digite um número inteiro: "))
        binario, hexadecimal, octal = converter_numero(numero)

        print(f"Binário: {binario}")
        print(f"Hexadecimal: {hexadecimal}")
        print(f"Octal: {octal}")
        input("Pressione Enter para voltar ao menu...")
    elif escolha == 4:
        numero = int(input("Digite um número inteiro: "))
        fatorar_numero(numero)
        print(f"O fatorial de {numero} é {fatorar_numero(numero)}")
        input("Pressione Enter para voltar ao menu...")
    elif escolha == 5:
        numero_perfeito()
        input("Pressione Enter para voltar ao menu...")
    elif escolha == 6:
        tabuada()
        input("Pressione Enter para voltar ao menu...")
    elif escolha == 7:
        numero_primo()
        input("Pressione Enter para voltar ao menu...")
    elif escolha == 8:
        emprestimo()
        input("Pressione Enter para voltar ao menu...")
    elif escolha == 9:
        numero = int(input("Digite um numero : "))
        if numero % 2 == 0:
            print(f"{numero} é par")
        else:
            print(f"{numero} é impar")
        input("Pressione Enter para voltar ao menu...")
    elif escolha == 10:
        progressao_aritimetica()
        input("Pressione Enter para voltar ao menu...")
    elif escolha < 0 or escolha > 10:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para voltar ao menu...")
    else:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para voltar ao menu...")