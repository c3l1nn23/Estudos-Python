from unidecode import unidecode
import random
import string

def remover_acentos(palavra):
    return unidecode(palavra)

#---------------------------------------------------------------------------------------------------

def gerar_senha(palavras, tamanho):
    def gerar_caracteres_extras(tamanho):
        caracteres_especiais = "!@#$%^&*"
        return ''.join(random.choices(caracteres_especiais, k=tamanho))

    def substituir_vogais(palavra):
        mapa_vogais = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'u': '@'}
        for vogal, numero in mapa_vogais.items():
            palavra = palavra.replace(vogal, numero)
            palavra = palavra.replace(vogal.upper(), numero)
        return palavra

    def substituir_numeros_por_caracteres(palavra):
        mapa_numeros = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%'}
        for numero, caractere in mapa_numeros.items():
            palavra = palavra.replace(numero, caractere)
        return palavra

    def letras_maiusculas(palavra):
        if palavra.islower():
            palavra = palavra[0].upper() + palavra[1:]
        return palavra

    def c_ç(palavra):
        return palavra.replace('c', 'ç')

    if tamanho < 12:
        raise ValueError("O tamanho mínimo recomendado para uma senha segura é 12 caracteres.")

    senha = ''.join(random.choices(''.join(palavras), k=tamanho))
    senha = substituir_vogais(senha)
    senha = substituir_numeros_por_caracteres(senha)
    senha = c_ç(senha)
    
    if 'c' not in senha:
        senha += 'Ç'
    
    if len(senha) < tamanho:
        senha += gerar_caracteres_extras(tamanho - len(senha))
    
    senha = letras_maiusculas(senha)
    
    if 'ç' in senha or 'Ç' in senha:
        senha = senha.replace('ç', 'Ç')
    
    return senha

palavras = input('Digite as palavras que deseja usar para gerar a senha: ').lower().split()
tamanho = int(input('Digite o tamanho da senha: '))

senha_gerada = gerar_senha(palavras, tamanho)
print(f'Sua senha segura é: {senha_gerada}')

#---------------------------------------------------------------------------------------------------
def calculadora_simples():
    print("Bem-vindo à Calculadora Simples!")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Escolha a operação:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    operacao = int(input("Digite a operação (1-4): "))

    if operacao == 1:
        print(f"Resultado: {n1} + {n2} = {n1 + n2}")
    elif operacao == 2:
        print(f"Resultado: {n1} - {n2} = {n1 - n2}")
    elif operacao == 3:
        print(f"Resultado: {n1} * {n2} = {n1 * n2}")
    elif operacao == 4:
        if n2 != 0:
            print(f"Resultado: {n1} / {n2} = {n1 / n2}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida.")
