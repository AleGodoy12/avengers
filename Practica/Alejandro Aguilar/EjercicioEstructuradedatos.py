# Ejercicios Listas, tuplas y diccionarios

# 1. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar).
# Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.

palabras= {}

while True:
    clave= input("Ingrese su nombre: ")
    if clave == "x":
        break
    valor= int(input("Ingrese su número de telefono: "))
    if clave not in palabras:
        palabras[clave] = valor
    else:
        print("No se puede repetir el nombre")        
print(palabras)


# 2. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima
# de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando
# el usuario introduce un cero.

meses= ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
mes= 1

while mes != 0:
    mes= int(input("Ingrese un numero del 1 al 12: "))
    if (mes >=1 and mes <=12):
        print(meses[mes-1])       # -1 para que me coincida el numero con el mes pq empieza de 0
    else:
        print("Error!")

# 3. Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

tupl= (6, 4, 3, 7, 2, 4, 9, 1, 7, 4,)
numero= int(input("Ingrese números: "))

contador= 0 
for i in tupl:
    if numero == i:
        contador += 1
print("Hay", contador ,"numeros repetidos")



# 4. Crea un programa e inserte los valores del 50 al 100 en una lista


listita= list(range(50,101))
print (listita)

# 5. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
# Historia y Lengua) en una lista y la muestre por pantalla.


materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for asignatura in materias:
    print("Yo estudio " +asignatura)