print("if izquierda ; else derecha")
x = input("Respuesta: ")
if x == "izquierda":
    x = input("Respuesta: ")
    if x == "izquierda":
        print("Perro")
elif x == "arriba":
    x = input("Respuesta: ")
    if x == "izquierda":
        print("Tigre")
elif x == "abajo":
    x = input("Respuesta: ")
    if x == "izquierda":
        print("Leon")
else:
    x = input("Respuesta: ")
    if x == "izquierda":
        print("Gato")
    elif x == "abajo":
        x = input("Respuesta: ")
        if x == "izquierda":
            print("Camello")
    else:
        x = input("Respuesta: ")
        if x == "izquierda":
            print("Serpiente")
        else:
            print("Conejo")