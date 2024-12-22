from random import randint
computador = randint(0, 11)
escolhapc = ""
escolha = ""
escolha = input("Escolha uma opção: [P]ar ou [I]mpar: ").strip().upper()
if escolha in ["P", "I"]:
    numero = int(input("Digite um número: "))
    soma = numero + computador
    if escolha == "P":
        escolhapc = "I"
    else:
        escolhapc = "P"
    if soma % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"
    escolha = escolha.replace("P", "Par").replace("I", "Impar")
    escolhapc = escolhapc.replace("P", "Par").replace("I", "Impar")
    if escolha == resultado:
        print(f"Você escolheu {escolha} e o computador escolheu {escolhapc}. A soma deu {soma}. Você venceu!")
    else:
        print(f"Você escolheu {escolha} e o computador escolheu {escolhapc}. A soma deu {soma}. Você perdeu!")