contador = 1
maior_idade = 0
menor_idade = 0
ano = 2024
for i in range(1,7):
    nasc = int(input(f"Digite a data de nascimento da {contador}ª pessoa: "))
    idade = ano - nasc
    if idade >= 18:
        maior_idade += 1
        contador += 1
    else:
        menor_idade += 1
        contador += 1
print(f"{maior_idade} pessoas são maior de idade e {menor_idade} são menores de idade.")