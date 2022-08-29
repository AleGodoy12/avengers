#1. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono 
# (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que 
# no quiere insertar mas. No se podrán meter nombres repetidos.

dicc= {}

while True:
    clave= input("Ingrese un nombre: ")
    if clave == "x":
        break
    valor= int(input("Ingrese un número de telefono: "))
    if clave not in dicc:
        dicc[clave] = valor
    else:
        print("No se puede repetir el nombre")
print(dicc)

#2. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 
# 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un 
# mensaje de error. El programa termina cuando el usuario introduce un cero.

meses= ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
mes= 1
while mes != 0:
    mes= int(input("Ingrese un numero para saber el mes: "))
    if (mes >=1 and mes <=12):
        print(meses[mes-1])       # -1 para que me coincida el numero con el mes pq empieza de 0
    elif mes == 0:
            break
    else:
        print("Error")
        
#3. Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

tuplas= (4, 3, 5, 9, 7, 3, 3, 5, 7, 1,)
numero= int(input("Ingrese un numero para saber cuantas veces se repite: "))
print ("Hay", tuplas.count(numero),"numeros repetidos")

#4. Crea un programa e inserte los valores del 50 al 100 en una lista
lis= list(range(50,101))

print (lis)

#5. Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

materias= ("Matemáticas", "Física", "Química", "Historia", "Lengua")

print (materias)



