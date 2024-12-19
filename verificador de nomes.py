nome = str(input("Qual seu nome ? ")) .lower().title()
verificar = ( "Silva" in nome)
separanome = nome.split()
ultimonome = separanome[-1]
print (f"Seu nome tem Silva ? {verificar}")
print (separanome[0])
print (ultimonome)