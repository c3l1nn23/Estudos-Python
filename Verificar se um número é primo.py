#Verificador de numero primo
numero = int(input("Digite um numero : "))
x = 0 
for i in range(1,numero + 1):
    if numero % i == 0:
        x = x + 1
if x == 2 :
    print (f"{numero} é primo")
else:
    print (f"{numero} não é primo")
        
