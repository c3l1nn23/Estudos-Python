fatorial = 1
numero = int(input("Digite um número para calcular o fatorial: "))
for c in range(numero, 0, -1):
    fatorial = c * fatorial
print(fatorial)