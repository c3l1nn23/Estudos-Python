frase = input("Digite a frase : ").strip().lower()
letrasA = frase.count('a')
primeirAA = frase.find('a')
ultimAA = frase.rfind('a')
print (f"""A Letra A aparece {letrasA}x
       A primeira letra A aparece na posição {primeirAA}
       A ultima letra A aparece na posição {ultimAA}""")