lista = []
conta = input("Digite a expressão matemática: ")
for simb in conta:
    if simb == "(":
        lista.append("(")
    elif simb == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("Expressão válida.")
else:
    print("Expressão inválida.")