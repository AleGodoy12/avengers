 # Evaluacion Estructura de datos.

### Se presentan 3 consignas, una por cada estructura de datos donde se busca ademas de la resolucion efectiva, un codigo lo mas escalable y limpio posible.

#### Al finalizar, avisar en hilo por el canal de slack, asi me acerco y de forma aleatoria me explican una de las resoluciones de los ejercicios realizados. 

# 1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.

from turtle import update


materia_docente = {"matematicas": "juan", "fisica": "pedro","ingles": "natalia", "phyton": "alex" }
  
materia_docente.update{"matematicas"}=="cristian"



 
# 2. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor

# usuario= int(input("ingrese numeros, para finalizar ingrese el numero 0 (cero): "))
# num = 0
# lista1 = []
# while usuario != num:
#     lista1.append (usuario)
  
#     usuario= int(input("ingrese numeros, para finalizar ingrese el numero 0 (cero): "))
# lista1.sort(reverse=True)
# print(lista1)

# 3. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero -->
año = ("enero", "febrero","marzo", "abril", "mayo","junio","julio","agosto","septiembre","octubre", "noviembre", "diciembre")
mes=1
while año != 0:
    if(mes <=1 and mes <=12 ):
      print(año [mes - 1] ) 
    else:
        print("error.")  




