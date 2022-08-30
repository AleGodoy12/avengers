# Evaluacion Estructura de datos.

### Se presentan 3 consignas, una por cada estructura de datos donde se busca ademas de la resolucion efectiva, un codigo lo mas escalable y limpio posible.

#### Al finalizar, avisar en hilo por el canal de slack, asi me acerco y de forma aleatoria me explican una de las resoluciones de los ejercicios realizados. 

# 1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. 
# Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.

materias = {"Laura" : "Matematica",
            "Federico" : "Geografia",
            "Nicolas" : "Lengua"}
print("La lista de docentes con sus respectivas materias es:", materias)
materias["Matemática"] = "Esteban"
materias["Geografia"] = "Lucia"
print("La lista actualizada al dia de la fecha es: " , materias)

# 2. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos
# de insertar. Por último, muestra los números ordenados de mayor a menor


lista = []
digitos = int(input("Ingresa un numero: "))


while digitos !=0 :
    lista.append (digitos)
    digitos = int(input("Ingresa un numero: "))

lista.sort()
print (lista)


# 3. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud 
# máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina
# cuando el usuario introduce un cero

meses = ("Enero", "Febrero", "Marzo", 
        "Abril", "Mayo", "Junio", 
        "Julio", "Agosto", "Septiembre", 
        "Octubre", "Noviembre", "Diciembre")
number = 1
while number != 0:
    number = int(input("Ingresa un número [0 para salir]: "))
    if number == 0: 
        break
    if(number >= 1 and number <= len(meses)):
        print(f'Mes: {meses[number-1]}')
    else: 
        print("¡Error! El número esta fuera de rango [entre 1 y 12]")