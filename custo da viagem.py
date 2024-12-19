#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#cobrando R$0,50 por Km para viagens de até 200Km e 
#R$0,45 parta viagens mais longas.
tarifa = 0
distancia = float(input("Qual a distancia da viagem ? "))
if distancia < 201:
    tarifa = distancia*0.50
else:
    tarifa = distancia*0.45
print (f"A passagem ficara R${tarifa:.2f}")