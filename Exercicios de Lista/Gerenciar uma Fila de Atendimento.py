#1. Gerenciar uma Fila de Atendimento
#Objetivo: Simule uma fila de atendimento onde novos clientes são 
#adicionados ao final da lista e os clientes atendidos são removidos 
#do início da lista.
novo_Cliente = 0
fila = []

while True:
    print ('1 - ADICIONAR CLIENTE NA LISTA')
    print ('2 - REMOVER CLIENTE DA LISTA')
    print ('3 - FINALIZAR')
    
    escolha = input("Escolha o numero da opção desejada : \n")
    if escolha == '1':
          novo_Cliente = input('Qual o nome do cliente ? \n')
          fila.append (novo_Cliente)
          print (f'O cliente foi {novo_Cliente} colocado na lista :) \n')
    elif escolha == '2':
        if fila:
            cliente_atendido = fila.pop(0)
            print(f"Cliente '{cliente_atendido}' atendido e removido da fila.")
        else:
            print("Não há clientes na fila para atender.")
    elif escolha == '3':
        print("Fim")
        break
    
    else:
        print ("Opção Invalida")
        break
        
print (f"Fila final {fila}")
