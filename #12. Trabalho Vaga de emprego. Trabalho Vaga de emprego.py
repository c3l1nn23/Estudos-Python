#12. Trabalho Vaga de emprego
idade = int(input("Qual sua idade? "))
nasc = input("Qual sua nacionalidade? ")
experiencia = float(input("Quantos anos de experiência? (Apenas números): "))
if idade <= 0 :
    print ("Coloque uma idade correta ")
elif idade >= 18 and experiencia >= 2:
    if nasc == "Brasileira" or "BR" or "Brasileiro" or "br":
        print("Você está elegível")
else: 
    print("Você não está elegível")