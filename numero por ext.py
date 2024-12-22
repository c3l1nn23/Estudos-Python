numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input('Digite um número entre 0 e 20: '))
if escolha < 0 or escolha > 20:
    print('Tente novamente. ', end='')
else:
    print(f'Você digitou o número {numeros[escolha]}')