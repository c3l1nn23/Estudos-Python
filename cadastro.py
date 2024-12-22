idadeS = 0
homens = 0
mulher20 = 0

while True:  
    idade = int(input("Digite a idade: "))
    if idade < 0:
        print("Idade inválida")
        input("Digite a idade: ")
    sexo = input("Digite o sexo [M] or [F] ").upper()
    if sexo not in ["M", "F"]:
        print("Sexo inválido")
        input("Digite o sexo [M] or [F] ").upper()
    if idade > 18:
        idadeS += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulher20 += 1
    if idade < 0:
        print("Idade inválida")
    escolha = input("Quer continuar? [S/N] ").strip().upper()
    if escolha not in ["S", "N"]:
        input("Opção inválida! Por favor, digite 'S' para continuar ou 'N' para sair: ")
    if escolha == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {idadeS}")
print(f"Total de homens cadastrados: {homens}")
print(f"Total de mulheres com menos de 20 anos: {mulher20}")