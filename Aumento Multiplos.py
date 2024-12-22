
salario = float(input("Qual o seu salário? "))

if salario > 1250:
    aumento = (salario * 10) / 100  
else:
    aumento = (salario * 15) / 100 

salario_atualizado = salario + aumento
print(f"Seu salário atualizado é R${salario_atualizado:.2f}")