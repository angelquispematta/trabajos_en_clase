nombres = ["Ana", "Sonia", "Helena"]
nombres2 = ["Miguel", "Carlos", "Juan"]
nombresfinales = [nombres, nombres2]
print("Imprimiendo valor [1] [2]", nombresfinales[1][2])
print("Lista completa:", nombresfinales)
for i in range(len(nombresfinales)):
    print("\n")
    if i == 0:
        print("####NOMBRES FEMENINOS####")
    elif i == 1:
        print("####NOMBRES MASCULINOS####")
    for j in range(len(nombresfinales[i])):
        print(nombresfinales [i][j], end=",")
