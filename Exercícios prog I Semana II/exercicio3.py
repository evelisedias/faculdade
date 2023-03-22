print("\n--------------INICIO DA EXECUÇÃO-------------------")

ano = int (input("Digite um ano qualquer: "))

if ano % 4 == 0:
    print("O ano informado", ano, "é um ano bissexto!")
else:
    print("O ano", ano, "é um ano comum.")

print("\n--------------FIM DA EXECUÇÃO-------------------")