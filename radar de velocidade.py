#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input("Qual velocidade atual do carro ? "))
multa = 0
if velocidade > 80:
    velocidade = velocidade - 80
    multa = velocidade * 7
print (multa)