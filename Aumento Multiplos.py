#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Qual o seu salário? "))

if salario > 1250:
    aumento = (salario * 10) / 100  # Aumento de 10%
else:
    aumento = (salario * 15) / 100  # Aumento de 15% para salários menores ou iguais a 1250

salario_atualizado = salario + aumento
print(f"Seu salário atualizado é R${salario_atualizado:.2f}")