contador = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input("Digite um número (999 para parar) : "))
    if numero != 999:
      contador += 1
      soma += numero
else:
    print("Você digitou {} números e a soma entre eles foi {}".format(contador, soma))