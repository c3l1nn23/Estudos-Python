#13. Digitar numeros para serem somados e quando o usuário  digitar ‘0’ o programa fecha e da o resultado da soma de todos os numeros digitados.
soma = 0
contador = 1
while True:
    numero = float(input(f"Qual o {contador} numero ? Digite '0' para encerrar"))
    if numero == 0:
        print ("Fim")
        break
    soma = soma + numero
    contador = contador + 1
print (f"{soma}")
