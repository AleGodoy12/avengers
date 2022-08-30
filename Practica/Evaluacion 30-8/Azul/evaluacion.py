#1.Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente.
#  Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.

materias= {"matemática":"maria", "lengua":"jose", "ingles":"marta", "sociales":"lorena"}
print(materias)
docentes= {"lengua":["roberto"], "sociales":["manuel"]}
materias.update(docentes)
print("Se reemplazaron los nombre de las materias de lengua y sociales", materias)

#2.Crea un programa que pida al usuario números, genera en una lista, 
# cuando el usuario ingrese un 0 dejaremos de insertar. 
# Por último, muestra los números ordenados de mayor a menor

lista= []
numero= int(input("Ingrese un número: "))
cond= 0

while numero != cond :
    lista.append(numero)
    numero = int(input("Ingrese un número: "))    
lista.sort()
lista.reverse()
print(lista)

#3.Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 
# y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. 
# El programa termina cuando el usuario introduce un cero

meses= ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
mes= 1

while mes != 0:
    mes= int(input("Ingrese un numero del 1 al 12: "))
    if (mes >=1 and mes <=12):
        print(meses[mes-1])      
    else:
        print("Error!")