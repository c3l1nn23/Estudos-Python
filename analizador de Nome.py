nome = str(input("Qual seu nome ? "))
print ("Analizando seu nome...")
nomeMaior = nome.upper()
nomeMenor = nome.lower()
separanome = nome.split()
qntPnome = len(separanome)
nomeSEspaco = nome.replace(" ","")
qntNomeTodo = len(nomeSEspaco)
print (f"""Seu nome em maiusculo fica : {nomeMaior}
       Seu nome em minusculo fica : {nomeMenor}
       Seu nome todo tem {qntNomeTodo}
       Seu Primeiro nome tem {qntPnome} letras""")
print (separanome)