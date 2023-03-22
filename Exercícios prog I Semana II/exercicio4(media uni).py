print('\n------------- Notas do semestre ----------------')
print('\n------------- Iniciando Execução ----------------')

grauA = int (input("Digite sua nota do Grau A: "))
grauB = int (input("Digite sua nota do Grau B: "))

media = (grauA * 0.3) + (grauB * 0.7)

if (grauA < 0) or (grauB <0):
    print("Nota digitada é inválida")

elif media >= 6:
    print("Você está aprovado! Boas Férias.")
else:
    print("Será necessário realizar o GrauC, boa sorte!")
print('\n------------- Fim da Execução ----------------')
