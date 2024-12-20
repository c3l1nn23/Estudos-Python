from random import randint
computador = randint(1,3)
escolha = input("""Escolha entre
                1 - Pedra
                2 - Papel
                3 - Tesoura
                """)
if escolha == '1':
    if computador == 1:
        print('Empate')
    elif computador == 2:
        print('Computador venceu')
    elif computador == 3:
        print('Jogador venceu')
elif escolha == '2':
    if computador == 1:
        print('Jogador venceu')
    elif computador == 2:
        print('Empate')
    elif computador == 3:
        print('Computador venceu')
elif escolha == '3':
    if computador == 1:
        print('Computador venceu')
    elif computador == 2:
        print('Jogador venceu')
    elif computador == 3:
        print('Empate')
