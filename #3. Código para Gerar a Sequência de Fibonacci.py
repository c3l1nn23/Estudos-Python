#3. Código para Gerar a Sequência de Fibonacci
n = int(input("Quantos termos deseja ver da Sequência de Fibonacci : "))
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

result = fibonacci(n)
print(result)