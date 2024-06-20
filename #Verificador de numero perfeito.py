#Verificador de numero perfeito
n = int(input("Digite o valor de n: "))
soma = 0
  
for divisor in range(1,n):
     if n % divisor == 0:
        soma += divisor 
if n == soma:
    print(f"O numero {n} é perfeito")
else: 
    print(f"O numero {n} nao é perfeito\n")