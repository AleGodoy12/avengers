# A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. 
# Finalizar al ingresar el número 0, el cual no debe guardarse.

listaNumeros = []
def ingresoN () :
    numerosIngresados = int(input("Escriba un numero: "))
    numCorte= 0
    while numCorte != numerosIngresados :
        listaNumeros.append(numerosIngresados)
        numerosIngresados = int(input("Escriba un numero: "))
    print (listaNumeros)
ingresoN()
        #Me salio a la primera vez el codigo, soy felizzzz 
        
# B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista,
# eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

def eliminarN () :
    eliminar= int(input("Escriba el numero que desee eliminar: "))
    if eliminar in listaNumeros:
        listaNumeros.remove((eliminar))
    else: 
         print("No es posible eliminarlo")
    
    print (listaNumeros)

eliminarN()
    
## C) Recorrer la lista para imprimir la sumatoria de todos los elementos.

def sumarLista():
    sumarLista= sum(listaNumeros)
    print ("La suma total de la lista es:")
    print (sumarLista)
    
sumarLista()

## D) Solicitar al usuario otro número y crear una lista con los elementos de
# la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

numeroNuevo = int (input ("Ingrese un numero nuevo: "))
listaNueva = []

def numerosMenores (listaNumeros, numeroNuevo):     
    for elementoListaNumeros in listaNumeros:      
        if elementoListaNumeros < numeroNuevo:  
            listaNueva.append(elementoListaNumeros)    

    print(f'La lista con los números menores a {numeroNuevo} es  {numeroNuevo}') 

numerosMenores (listaNumeros, numeroNuevo)
