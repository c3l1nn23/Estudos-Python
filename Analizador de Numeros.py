numero = int(input("Digite um numero : "))
print ("Analizando o numero ...")
unidade = numero//1 %10
dezena = numero//10 %10
centena = numero//100 %10
milhar = numero//1000 %10
print (f""" Unidades : {unidade}
        Dezenas : {dezena}
        Centenas : {centena}
        Milhar : {milhar}""")