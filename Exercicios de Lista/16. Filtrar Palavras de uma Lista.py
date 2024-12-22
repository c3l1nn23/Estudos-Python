#16. Filtrar Palavras de uma Lista

nomes = ['Miguel' , 'Sophia', 'Davi', 'Alice', 'Artur', 'Julia', 'Pedro', 'Isabela', 'Manuela', 'Laura', 'Raphael', 'Nicolas', 'Maria', 'Pietra', 'Marcelo']


letra = str(input("Qual a letra desejada ? "))
letra = letra.upper()
if letra:
    filtrar = list(filter(lambda nome: nome.startswith(letra), nomes))
    print (filtrar)
else:
    print ("Digite uma letra para funcionar")
