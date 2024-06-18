#7. Adicionar Elementos a uma Lista com append:
item = 0
lista = []
while True:
    item = str(input(f"Qual o item deseja adicionar na lista ? Digite 'Parar' para parar o codigo \n" "Apenas Letras : \n"))
    if item == "Parar":
        print ("Fim da lista")
        break
    lista.append (item)
print (f"{lista}")