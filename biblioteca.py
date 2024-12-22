titulo = []
autor = []
ano_de_publicacao = []
genero = []

print('Bem-vindo ao Sistema de Cadastro de Livros!')

def escolha_menu():
    while True:
        try:
            escolha = int(input("""Escolha uma opção:
1 - Cadastrar Livro
2 - Listar Livros
3 - Buscar Livros
4 - Excluir Livro
5 - Sair do Sistema \n"""))
            if escolha in [1, 2, 3, 4, 5]:
                return escolha
            else:
                print("Opção inválida. Por favor, insira um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

escolha = escolha_menu()

while escolha != 5:
    if escolha == 1:
        Titulo = input('Digite o título do livro: ').strip().upper()
        titulo.append(Titulo)
        Autor = input('Digite o autor do livro: ').strip().upper()
        autor.append(Autor)

        while True:
            try:
                Ano_de_publicacao = int(input('Digite o ano de publicação do livro: '))
                break
            except ValueError:
                print("Por favor, insira um ano válido.")

        ano_de_publicacao.append(Ano_de_publicacao)
        Genero = input('Digite o gênero do livro: ').strip().upper()
        genero.append(Genero)

        print('Livro cadastrado com sucesso!')
        escolha = escolha_menu()

    elif escolha == 2:
        print('Listando livros...')
        for i in range(len(titulo)):
            print(f'Título: {titulo[i]}')
            print(f'Autor: {autor[i]}')
            print(f'Ano de publicação: {ano_de_publicacao[i]}')
            print(f'Gênero: {genero[i]}')
            print('-' * 20)
        escolha = escolha_menu()

    elif escolha == 3:
        busca = input('Digite o título do livro que deseja buscar: ').upper().strip()
        if busca in titulo:
            print(f'O livro "{busca}" está cadastrado! Na posição {titulo.index(busca)}')
        else:
            print(f'O livro "{busca}" não está cadastrado!')
        escolha = escolha_menu()

    elif escolha == 4:
        excluir = input('Digite o título do livro que deseja excluir: ').upper().strip()
        if excluir in titulo:
            print(f'O livro "{excluir}" foi excluído!')
            posicao = titulo.index(excluir)
            titulo.pop(posicao)
            autor.pop(posicao)
            ano_de_publicacao.pop(posicao)
            genero.pop(posicao)
        else:
            print(f'O livro "{excluir}" não está cadastrado!')
        escolha = escolha_menu()
