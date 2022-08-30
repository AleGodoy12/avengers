#1. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. 
# Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.

# materias = {"Geografia": "Andrea", "Matematica": "Jorge", "Historia": "Julian"}

# print(materias)
# elimdoce = input("Escriba de que materia desea eliminar su docente")
# newdoce = input("Escriba el nombre del nuevo docente")

# materias[elimdoce] = newdoce
# print(materias)
# elimdoce1 = input("Escriba de que materia desea eliminar su docente")
# newdoce1 = input("Escriba el nombre del nuevo docente")

# materias[elimdoce1] = newdoce1

# print(materias)



#2. Crea un programa que pida al usuario números, genera en una lista, 
# cuando el usuario ingrese un 0 dejaremos de insertar.
#  Por último, muestra los números ordenados de mayor a menor

def numeritos():
    lista = []
    num = int(input("Declare un numero"))
    confirmacion = 0
    while num != confirmacion:
        lista.append(num)
        num = int(input("Declare un numero, presione 0 para detener"))
    
    lista.sort(reverse=True)
    print(lista)

numeritos()
    



#3. Crea una tupla con los meses del año, pide números al usuario, 
# si el numero esta entre 1 y la longitud máxima de la tupla, 
# muestra el contenido de esa posición sino muestra un mensaje de error. 
# El programa termina cuando el usuario introduce un cero

# tupla= ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
# mes= 1

# while mes != 0:
#     mes= int(input("Coloque un numero 1 al 12: "))
#     if (mes >=1 and mes <=12):
#         print(tupla[mes-1])     
#     else:
#         print("Error,Numero no encontrado en los meses")



# def numeritos():
#     lista = []
#     num = int(input("Declare un numero"))
#     lista.append(num)
#     while num != "0:
#         if (num == 0):
#             break
#         else:
#             num = int(input("Declare un numero, presione 0 para detener"))
#             lista.append(num)
#     lista.sort(reverse=True)
#     print(lista)

# numeritos()