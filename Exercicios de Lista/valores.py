lista = []
while True:
    n = (int(input("Digite um número: ")))
    if n in lista:
        print("Número já digitado")
    else:
        lista.append(n)
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print(f"Os números digitados foram: {sorted(lista)}")