print ('='*10)
print ('Loja Polar')
precoCompras = float(input('Digite o valor total das compras: R$'))
formaPagamento = int(input('Digite a forma de pagamento: \n1 - À vista dinheiro/cheque \n2 - À vista no cartão \n3 - Em até 2x no cartão \n4 - 3x ou mais no cartão\n'))
if formaPagamento == 1:
    precoFinal = precoCompras - (precoCompras * 10 / 100)
    print(f'O valor final das compras é R${precoFinal:.2f}')
elif formaPagamento == 2:
    precoFinal = precoCompras - (precoCompras * 5 / 100)
    print(f'O valor final das compras é R${precoFinal:.2f}')
elif formaPagamento == 3:
    precoFinal = precoCompras
    print(f'O valor final das compras é R${precoFinal:.2f}')
elif formaPagamento == 4:
    precoFinal = precoCompras + (precoCompras * 20 / 100)
    print(f'O valor final das compras é R${precoFinal:.2f}')
else:
    print('Forma de pagamento inválida.')
print ('='*10)