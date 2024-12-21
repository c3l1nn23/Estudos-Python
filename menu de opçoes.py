n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
print('Escolha uma opção:\n1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Novos números\n5 - Sair\n')
opcao = int(input('Digite a opção escolhida: '))
while opcao != 5:
    if opcao == 1:
        print(f'A soma de {n1} + {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'O produto de {n1} x {n2} é {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f'O maior número é {n2}')
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        n1 = float(input('Digite o 1º número: '))
        n2 = float(input('Digite o 2º número: '))
    print('Escolha uma opção:\n1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Novos números\n5 - Sair\n')
    opcao = int(input('Digite a opção escolhida: '))