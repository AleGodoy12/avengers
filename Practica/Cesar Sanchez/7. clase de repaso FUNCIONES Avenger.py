# Ejericios Lista nivel Avengers💥🚀

## A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.

listaNumeros = []


numero = int (input ("Ingrese los números, si ingresa el número 0 finaliza la lista : "))

def solicitarNumeros (numero): 

    numerofinalizar = 0

    while numero != numerofinalizar:

        listaNumeros.append(numero)

        numero = int (input("Ingrese los números, si ingresa el número 0 finaliza la lista : "))

    return listaNumeros


print(solicitarNumeros(numero))

## B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

numeroNuevo = int (input ("Ingrese un número y si está repetido lo eliminaremos: "))

def numeroAEliminar (numeroNuevo):

    if numeroNuevo in listaNumeros :    # Si mi número está en la lista ...

        listaNumeros.remove(numeroNuevo)            # Elimino el número repetido 

        print("El número ", numeroNuevo ," se encuentra repetido.Su nueva lista es: ",listaNumeros)

    else :

        print (f'No es posible eliminar el número {numeroNuevo} porque no se encuntra en su lista')

numeroAEliminar (numeroNuevo)



## C) Recorrer la lista para imprimir la sumatoria de todos los elementos.

print (f'La lista es: ', listaNumeros)

def sumatoriaElementos (listaNumeros):

    sumatoria = 0

    for i in listaNumeros :           # Recorro los elementos de la lista  

        sumatoria += i                # Sumo los elementos de la lista

    print (f'La sumatoria de los elementos de la lista es: {sumatoria}')

sumatoriaElementos(listaNumeros)

## D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

otroNumero = int (input ("Ingrese otro número y así crear una lista con números menores al ingresado: "))

listaNueva = []

def numerosMenores (listaNumeros, otroNumero):     # Ingreso con 2 parametros 

    for elementoListaNumeros in listaNumeros:      # Recorro los elementos de la lista creada al inicio (ListaNumeros)

        if elementoListaNumeros < otroNumero:        # Mientras los elementos de la lista (listaNumeros) sean MENORES que el número ingresado (otroNumero) 

            listaNueva.append(elementoListaNumeros)      # Agrego los elementos de mi (listaNumeros) a mi (listaNueva)

            # break            # Finzalizo el ciclo 

    print(f'La lista con los números menores a {otroNumero} es  {listaNueva}') 

numerosMenores (listaNumeros, otroNumero)



## E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]


listaFinal = []

def elementosTupla (listaNueva):

    for i in listaNueva:    # Recorro los elementos de mi lista

    # Tengo que generar una tupla de la forma (n, lista.count(n)) 
    
        if (i , listaNueva.count(i)) not in listaFinal:        # Evaluo si la tupla se encuentra o no en mi lista (listaFinal). Si no se encuemtra le agrego a mi lista 

            listaFinal.append((i, listaNueva.count(i)))

        print (f'Mi lista nueva con la tupla queda {listaNueva}')

elementosTupla(listaNueva)


