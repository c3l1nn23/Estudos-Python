from utils import remover_acentos
palavra = input("Digite uma palavra: ").lower().strip()
palavra = remover_acentos(palavra)
palavra = palavra.lower().strip()
palavras = palavra.split()
junto = "".join(palavras)
print ("Desconsiderando acentos, espaços e etc ...")
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")