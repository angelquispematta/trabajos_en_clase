imp = []
total = []
for i in range(10):
    imp.append([])
    for j in range(3):
        imp[i].append(int(input("Ingresar el importe del producto" + str(i+1) + ", cliente" + str(j+1) + ": ")))
for i in range(3):
    suma = 0
    for j in range(10):
        suma = suma + imp[1][1]
    total.append(suma)
print("El importe de todos los productos son: ")
print(total)