# Evaluacion Estructura de datos.

### Se presentan 3 consignas, una por cada estructura de datos donde se busca ademas de la resolucion efectiva, un codigo lo mas escalable y limpio posible.

#### Al finalizar, avisar en hilo por el canal de slack, asi me acerco y de forma aleatoria me explican una de las resoluciones de los ejercicios realizados. 

# 1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.

""" nombresMaterias = {"matematica": "juan", "quimica": "fabricio", "ingles": "esteban", "fisica": "cesar"}

print ("Materias con los nombres de los profesoes desactualizados ",nombresMaterias)

nombresMaterias ["matematica"] = "josé"

nombresMaterias ["ingles"] = "messi"

print("Las materias con los nombres de profesores en la actualidad son: ", nombresMaterias) """



# 2. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor


numeros = int (input("Ingrese los números: "))

lista = []

numeroFinalizador = 0

while numeros != numeroFinalizador:

    lista.append(numeros)

    numeros = int (input("Ingrese los números: "))


lista.sort(reverse=True)

print(f'La lista con los números son: {lista}')

# 3. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero

""" mesesAnio = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Noviembre", "Diciembre")

mesNumero = int (input("Ingrese un número del 1 al 12 y te diré que mes es: "))

posisicion = 1

while mesNumero != 0:

    if (mesNumero >= 1 and mesNumero <=12) :

        print(f'El número {mesNumero} pertenece al mes {mesesAnio[mesNumero-1]}')

    else:

        print(f'Error!')

    break """