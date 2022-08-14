#1. Crea una tupla con los meses del año, 
# pide números al usuario, 
# si el numero esta entre 1 y la longitud máxima de la tupla, 
# muestra el contenido de esa posición sino muestra un mensaje de error.
#El programa termina cuando el usuario introduce un cero.

meses= ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
mes= 1

while mes != 0:
    mes= int(input("Ingrese un numero del 1 al 12: "))
    if (mes >=1 and mes <=12):
        print(meses[mes-1])       # -1 para que me coincida el numero con el mes pq empieza de 0
    else:
        print("Error!")

#2. Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

tuplas= (4, 3, 5, 9, 7, 3, 3, 5, 7, 1,)
numero= int(input("Ingrese números: "))

contador= 0 
for i in tuplas:
    if numero == i:
        contador += 1
print("Hay", contador ,"numeros repetidos")

    

#3. Crea una tupla con valores ya predefinidos del 1 al 10, 
# pide un índice por teclado y muestra los valores de la tupla.

tupla1= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
indice= int(input("Ingrese un índice: "))
print(tupla1[indice])


