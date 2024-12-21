usercadastrado = 'admin'
senhaCadastrada = '1234'
user = input('Digite o usuário: ')
senha = input('Digite a senha: ')
if user != usercadastrado:
    while True:
        print('Usuário inválido.')
        user = input('Digite o usuário: ')
        senha = input('Digite a senha: ')
        if user == usercadastrado:
            break
if senha != senhaCadastrada:
    while True:
        print('Senha inválida.')
        senha = input('Digite a senha: ')
        if senha == senhaCadastrada:
            break
print('Seja vem vindo {user}!')