contador = 0
soma = 0
maior = None
menor = None

def pedir_continuacao():
    while True:
        escolha = input("Quer continuar? [S/N] ").strip().upper()
        if escolha in ["S", "N"]:
            return escolha
        else:
            print("Opção inválida! Por favor, digite 'S' para continuar ou 'N' para sair.")

while True:
    numero = int(input("Digite um número: "))
    contador += 1
    soma += numero

    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

    escolha = pedir_continuacao()
    if escolha == "N":
        break

if contador > 0:
    media = soma / contador
    print(f"Você digitou {contador} números e a média entre eles foi {media:.2f}")
    print(f"O maior valor foi {maior} e o menor valor foi {menor}")
else:
    print("Nenhum número foi digitado.")
print("FIM")