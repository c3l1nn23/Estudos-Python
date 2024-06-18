#14. Criar uma lista de alunos, ir adicionando os nomes a essa lista e quando o usuário digitar “fim” ele encerra e mostra a lista de alunos.
nomeA = 0
contador = 1
lista = []
while True:
    nomeA = str(input(f"Qual o nome do {contador}º aluno ? 'Fim' para encerrar \n"))
    if nomeA == "Fim":
        print ("Fim")
        break
    lista.append (nomeA)
    contador = contador + 1
print (f"{lista}")