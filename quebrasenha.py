from random import randint
senhaC = [2,3,0,1]
senha = []
while senha != senhaC:
    senha = [randint(0,9)for _ in range (4)]
    print(senha)
    if senha == senhaC:
        print("Senha quebrada")
        print (senha)
        break