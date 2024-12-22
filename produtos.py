p_maisDeMil = 0
menor_preco = 0
nome_menor_preco = ""
while True:
    nome_P = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        nome_menor_preco = nome_P
        nome_menor_preco = nome_P
    if preco > 1000:
        p_maisDeMil += 1
    continuar = input("Deseja continuar? [S/N] ").upper()
    if continuar == "N":
        break
print(f"Total de produtos que custam mais de R$1000: {p_maisDeMil}")
print(f"Produto mais barato: {nome_menor_preco} custando R${menor_preco:.2f}")