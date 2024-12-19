import random
contador = 1
alunos = []  # Inicializa a lista para armazenar os nomes

while True:
    nome = input(f"Qual o nome do {contador}º aluno (digite 0 para sair): ")
    if nome == "0":
        print("Fim")
        break
    alunos.append(nome)
    contador += 1  
random.shuffle(alunos)
print(f"A ordem da lista é {alunos}")