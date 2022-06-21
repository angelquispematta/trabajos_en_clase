lista = [1,2,3,4,5,6,7,5,1,24,5,63,3,3,4,5,6,6,4,2]
print("Lista sin eliminación de números repetidos")
print(lista)
conjunto = set(lista)
lista = list(conjunto)
print("Números sin repetición")
print(lista)