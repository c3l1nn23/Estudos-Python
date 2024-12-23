lista = []
pares = []
impares = []
while True:
    n = int(input("Digite um numero: "))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = input("Deseja continuar? S/N  ").upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        print("Numero adicionado")


print(f"A lista digitada foi {lista}")
print(f"Os numeros pares são {pares}")
print(f"Os numeros impares são {impares}")