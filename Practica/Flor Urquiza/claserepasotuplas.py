## -Agregar pasajeros a la lista de viajeros.
lista = []
def agregarpasajeros(nombre,dni,destino,lista):
    datos = (nombre,dni,destino)
    lista.append(datos)
nombre= input("ingrese su nombre: ")
dni = int(input("ingrese su dni: "))
destino = input("ingrese su destino: ")
agregarpasajeros(nombre,dni,destino,lista)
while True:
        opcion = input("desea seguir agregando pasajeros? [S/N]")
        if opcion == "S":
            nombre= input("ingrese su nombre: ")
            dni = int(input("ingrese su dni: "))
            destino = input("ingrese su destino: ")
            agregarpasajeros(nombre,dni,destino,lista)
        if opcion == "N":
            print("finalizaste la operacion")
            break
#tuple2 = tuple(lista)
#print(tuple2)

# ## -Agregar ciudades a la lista de ciudades.
lista_Ciudades = []
def agregarciudades():
    nueva_ciudad = input("ingrese una nueva ciudad: ")
    lista_Ciudades.append(nueva_ciudad)
    confirmacion = input("quiere agregar una nueva ciudad  [S/N]:")
    while confirmacion == "S":
        nueva_ciudad = input("ingrese una nueva ciudad: ")
        lista_Ciudades.append(nueva_ciudad)
        confirmacion = input("quiere agregar una nueva ciudad  [S/N]: ")
    return lista_Ciudades
variable = agregarciudades()
print(variable)


## -Dado el DNI de un pasajero, ver a qué ciudad viaja.

def buscarCiudad(lista, dni):
    
    for viaje in lista:
        if viaje[1] == dni:                 #nombre,dni,destino,lista(POSICIONES)
            return viaje[2]
    return ""
print (buscarCiudad(lista, dni))
buscarCiudad(lista,dni)


## -Dado un país, mostrar cuántos pasajeros viajan a ese país.

#def pasajerosCiudad ():
  #  for destino in pasajeros: