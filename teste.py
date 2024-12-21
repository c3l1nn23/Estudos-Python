numero = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
opr = input("Digite a operação desejada: ")
if opr == "+":
    print(f"A soma entre {numero} e {n2} é {numero + n2}.")
elif opr == "-":
    print(f"A subtração entre {numero} e {n2} é {numero - n2}.")
elif opr == "*":
    print(f"A multiplicação entre {numero} e {n2} é {numero * n2}.")
elif opr == "/":
    print(f"A divisão entre {numero} e {n2} é {numero / n2}.")
else:
    print("Operação inválida.")