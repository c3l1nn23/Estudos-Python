#14. Criar uma lista de alunos, ir adicionando os nomes a essa lista e quando o usuário digitar “fim” ele encerra e mostra a lista de alunos.
nome_A = 0
contador = 1
lista = []
while True:
    nome_A = str(input(f"Qual o nome do {contador}º aluno ? 'Fim' para encerrar \n"))
    if nome_A == "Fim":
        print ("Fim")
        break
    lista.append (nome_A)
    contador = contador + 1
print (f"{lista}")
