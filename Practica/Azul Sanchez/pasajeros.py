## -Agregar pasajeros a la lista de viajeros.
lista = []
def agregarpasajeros(nombre,dni,destino,lista):
    datos = (nombre,dni,destino)
    lista.append(datos)
nombre= input("ingrese su nombre")
dni = int(input("ingrese su dni"))
destino = input("ingrese su destino")
agregarpasajeros(nombre,dni,destino,lista)
while True:
        opcion = input("desea seguir agregando pasajeros? [S/N]")
        if opcion == "S":
            nombre= input("ingrese su nombre")
            dni = int(input("ingrese su dni"))
            destino = input("ingrese su destino")
            agregarpasajeros(nombre,dni,destino,lista)
        if opcion == "N":
            print("finalizaste la operacion")
            break
# tuple2 = tuple(lista)
# print(tuple2)

# ## -Agregar ciudades a la lista de ciudades.
lista_Ciudades = []
def agregarciudades():
    nueva_ciudad = input("ingrese una nueva ciudad")
    lista_Ciudades.append(nueva_ciudad)
    confirmacion = input("quiere agregar una nueva ciudad  [S/N]")
    while confirmacion == "S":
        nueva_ciudad = input("ingrese una nueva ciudad")
        lista_Ciudades.append(nueva_ciudad)
        confirmacion = input("quiere agregar una nueva ciudad  [S/N]")
    return lista_Ciudades
# variable = tuple(agregarciudades())
# print(variable)


## -Dado el DNI de un pasajero, ver a qué ciudad viaja.

def buscarCiudad(lista, dni):
    
    for viaje in lista:
        if viaje[1] == dni:                 #nombre,dni,destino,lista(POSICIONES)
            return viaje[2]
    return ""
print(buscarCiudad(lista, dni))


## -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.

def cantidadPasajeros(pasajeros, lista_Ciudades):
    contador=0
    for destino in pasajeros:
        if destino[2]== lista_Ciudades:
            contador+=1
    return contador


## -Dado el DNI de un pasajero, ver a qué país viaja.

