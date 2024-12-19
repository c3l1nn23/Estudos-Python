#8. Pedir 10 números para o usuário e no final retornar a soma dos 10 números.
soma = 0
contador = 1
while contador <= 10:
    numero = float(input(f"Qual o {contador} numero ? - 10 Numeros para finalizar a sequencia : "))
    soma = soma + numero
    contador = contador + 1
print (f"{soma}")
