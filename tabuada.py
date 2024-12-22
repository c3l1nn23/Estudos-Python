numero = 0
while True:  
    numero = int(input("Digite um número para ver a tabuada: "))
    if numero <= 0:
        print("FIM")
        break
    for c in range(1, 11):
        print(f"{numero} x {c} = {numero * c}")