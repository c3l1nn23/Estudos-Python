from random import randint
computador = randint(1,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
numero = int(input('Qual é o seu palpite? '))
while numero != computador:
    if numero > computador:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
    numero = int(input('Qual é o seu palpite? '))
print(f'Parabéns! Você acertou. O número é {computador}')