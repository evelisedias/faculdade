print("------------- LISTA DE COMPRAS -----------------")
nProdutos = int (input("Quantos produtos deseja comprar? "))

minhaLista = []

for produtos in range (0, nProdutos):
    minhaLista.append (input("Digite o produto: "))
    
print ("\nSua lista de produtos é:", minhaLista)
print("\nBoas compras!")
   