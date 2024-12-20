anoNasc = int(input('Digite o ano de nascimento: '))
idade = 2024 - anoNasc
if idade <= 9 :
    print(f'Você tem {idade} anos, sua categoria é MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos, sua categoria é INFANTIL.')
elif idade <= 19:
    print(f'Você tem {idade} anos, sua categoria é JUNIOR.')
elif idade <= 25:
    print(f'Você tem {idade} anos, sua categoria é SÊNIOR.')