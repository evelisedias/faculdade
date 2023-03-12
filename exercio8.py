#Entrada de dados

print ("--------------- GRAU A ----------------------")
print()
p = float (input ("Digite a nota da Atividade Prática: "))
t1 = float (input ("Digite a nota da Atividade Teórica: "))
print()

print ("--------------- GRAU B ----------------------")
print()
l = float (input ("Digite a nota do Laboratório: "))
t2 = float (input("Digite a nota do teste teórico: "))
e = float (input("Digite a nota do Trabalho Extraclasse: "))
print()
#Processamento de dados
A = (p * 0.45) + (t1 * 0.55)
B = (l * 0.60) + (t2 * 0.20) + (e * 0.20)
m = (A/2) + (B/3)

print ("--------------- RESULTADO ----------------------")
print()
print("Sua nota é:", A + B)
print ("Sua média é:",m)