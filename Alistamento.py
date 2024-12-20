anoNasc = int(input('Digite o ano de nascimento: '))
idade = 2024 - anoNasc
if idade < 18:
    print(f'Você tem {idade} anos, ainda não pode se alistar.')
    print(f'Faltam {18 - idade} anos para você se alistar.')
    print (f'Seu alistamento será em {2024 + (18 - idade)}')