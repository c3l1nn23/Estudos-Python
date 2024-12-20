numero = int(input("Digite um número: "))
binario = bin(numero)[2:]
hexadecimal = hex(numero)[2:]
octal = oct(numero)[2:]
print (f"O número {numero} em binário é {binario}")
print (f"O número {numero} em hexadecimal é {hexadecimal}")
print (f"O número {numero} em octal é {octal}")