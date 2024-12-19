from random import randint
computador = randint (0,1)
print('-=-'*10)
print('Vou pensar em um numero ...')
print('-=-'*10)
numero = int (input("Qual numero pensei ? "))
if numero == computador:
    print (f"Parabens eu estava pensando no numero {numero}")
else:
    print (f"Você errou estava pensando no numero {computador}")