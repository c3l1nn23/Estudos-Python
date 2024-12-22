contador = 0
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        contador = contador + 1        
print(f"A soma de todos os {contador} valores solicitados é {soma}.")
    