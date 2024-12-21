n = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
for  c in range(1, 11):
    print(f"{n} -> ", end="", )
    n = n + razao
print("FIM")