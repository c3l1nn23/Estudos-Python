soma = 0
contador = 1
numerosI = []
for n in range (0,6):
   numero = input (f"Digite o {contador}º número: ")
   if float(numero) % 2 != 0:
      numerosI.append(numero)
      contador = contador + 1
   if float(numero) % 2 == 0:
         soma = soma + float(numero)
         contador = contador + 1
if len(numerosI) != 0:
    print(f"Os números ímpares são: {numerosI}.")

print(f"A soma dos números pares é {soma}.")