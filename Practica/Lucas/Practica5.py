# def agregarpasajero():
#     nombre = input("ingrese el nombre del pasajero: ")
#     pasajeros= []
#     confirmacion = ()
#     while nombre != confirmacion :
#         dniuser= int(input("ingrese su DNI: "))
#         destinouser= input("ingrese su destino: ")
#         confirmacion = input("confirme su nombre : ")
#         pasajeros.append((confirmacion,dniuser,destinouser))
#         return pasajeros
# agregarpasajero()


# def agregarciudades():
#     ciudades = []
#     nuevaciudad = input("Ingrese la ciudad que quiere agregar")
#     ciudades.append(nuevaciudad)
#     while ciudades != nuevaciudad:
#         confirmacion = input("¿Quiere agregar una nueva ciudad? Escriba Si o No")
#         if (confirmacion == "Si"):
#             nuevaciudad = input("Ingrese la ciudad que quiere agregar")
#             ciudades.append(nuevaciudad)
#             print(ciudades)
#         else:
#             print(ciudades)
#     return ciudades

# agregarciudades()
            
# def agregarciudades():
#     ciudades = []
#     nuevaciudad = input("Ingrese la ciudad que quiere agregar")
#     ciudades.append(nuevaciudad)
#     confirmacion = input("¿Quiere agregar una nueva ciudad? Escriba Si o No")
#     while confirmacion == "Si":
#             nuevaciudad = input("Ingrese la ciudad que quiere agregar")
#             ciudades.append(nuevaciudad)
#             confirmacion = input("¿Quiere agregar una nueva ciudad? Escriba Si o No")
#     return ciudades

# agregarciudades()

# listaejemplo = ["Manuel Juarez", 19823451, "Liverpool"]
# def buscarciudad():
#     for i in listaejemplo:
#         print(i)





























# -Agregar pasajeros a la lista de viajeros.
from re import X


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
tuple2 = tuple(lista)
print(tuple2)

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
variable = tuple(agregarciudades())
print(variable)


## -Dado el DNI de un pasajero, ver a qué ciudad viaja.

def buscarCiudad(nombre, dniuser):
    
    for viaje in nombre:
        if viaje == dniuser:
            return viaje
    return nombre, dniuser
variable2 = tuple(buscarCiudad())
print(variable2)    


    
def cantidadpasajeros(lista, lista_Ciudades):
    
    x = 0

    for destino[2] in lista:

        if destino[2] == lista_Ciudades[0]:

            x += 1
    return x

cantidadpasajeros




    
