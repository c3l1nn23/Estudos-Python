contador = 1
fem = 0
masc = 0
soma_idade = 0
masc_velho = 0
nome_masc_velho = ''
fem_M20 = 0

for c in range(0, 4):
    nome = input(f'Digite o {contador}ª nome: ').capitalize()
    idade = int(input(f'Digite a idade do(a) {nome}: '))
    sexo = input(f'Digite o sexo do(a) {nome} (m/f): ').lower().strip()

    while sexo not in ['m', 'f']:
        print('Entrada inválida. Digite "m" para masculino ou "f" para feminino.')
        sexo = input(f'Digite o sexo do(a) {nome}: ').lower().strip()

    p_letra = sexo[0]
    contador += 1

    if idade > masc_velho and p_letra == 'm':
        masc_velho = idade
        nome_masc_velho = nome
    
    if idade < 20 and p_letra == 'f':
        fem_M20 += 1

    if p_letra == 'f':
        fem += 1
    elif p_letra == 'm':
        masc += 1

    soma_idade += idade

media = soma_idade / 4

if masc > 0:
    print(f'O homem mais velho é {nome_masc_velho}')
else:
    print('Não há homens no grupo.')

print(f'A quantidade de mulheres abaixo de 20 é: {fem_M20}')
print(f'A média de idade do grupo é: {media:.2f}')
