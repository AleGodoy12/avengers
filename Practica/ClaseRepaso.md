# Ejericios Lista nivel Avengers💥🚀

## A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
## B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
## C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
## D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
## E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

## 1. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
## -Agregar pasajeros a la lista de viajeros.
## -Agregar ciudades a la lista de ciudades.
## -Dado el DNI de un pasajero, ver a qué ciudad viaja.
## -Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
## -Dado el DNI de un pasajero, ver a qué país viaja.
## -Dado un país, mostrar cuántos pasajeros viajan a ese país.
## -Salir del programa.




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





