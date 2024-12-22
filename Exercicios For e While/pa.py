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