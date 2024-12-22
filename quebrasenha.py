from random import randint
senhaC = [2,3,0,1,0,7]
senha = []
while senha != senhaC:
    senha = [randint(0,9)for _ in range (6)]
    print(senha)
    if senha == senhaC:
        print("Senha quebrada")
        print (senha)
        break