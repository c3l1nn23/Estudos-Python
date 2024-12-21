contador = 1
peso = 0
maior_peso = 0
for i in range(1,6):
    peso = float(input(f"Digite o peso da {contador}ª pessoa: "))
    if peso > maior_peso:
        maior_peso = peso
        contador += 1
    elif peso < menor_peso:
        menor_peso = peso
        contador += 1
print(f"O maior peso é {maior_peso}")
print(f"O menor peso é {menor_peso}")
      