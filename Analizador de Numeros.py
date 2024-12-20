numero = int(input("Digite um numero : "))


def converter_numero (numero):
     binario = bin(numero)[2:]
     hexadecimal = hex(numero)[2:]
     octal = oct(numero)[2:]
     return binario, hexadecimal, octal
binario, hexadecimal, octal = converter_numero(numero)
def analisar_numero (numero):
    unidade = numero//1 %10
    dezena = numero//10 %10
    centena = numero//100 %10
    milhar = numero//1000 %10
    return unidade, dezena, centena, milhar
unidade, dezena, centena, milhar = analisar_numero(numero)
print (f""" Unidades : {unidade}
        Dezenas : {dezena}
        Centenas : {centena}
        Milhar : {milhar}""")
print (f"O numero Convertido em Binario é {binario}")
print (f"O numero Convertido em Hexadecimal é {hexadecimal}")
print (f"O numero Convertido em Octal é {octal}")