#Ejercicio 2
def agregarPasajeros(pasajeros):
    nombre=input("Nombre -x para cortar: ")
    while nombre!="x":
        dni=int(input("DNI: "))
        destino=input("Ciudad destino: ")
        pasajeros.append((nombre,dni,destino))
        nombre=input("Nombre -x para cortar: ")
    return pasajeros
