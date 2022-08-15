# Tuplas

# 1. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima
# de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.

# El programa termina cuando el usuario introduce un cero



meses = ("Enero", "Febrero", "Marzo", 
        "Abril", "Mayo", "Junio", 
        "Julio", "Agosto", "Septiembre", 
        "Octubre", "Noviembre", "Diciembre")
number = None
while number != 0:
    number = int(input("Ingresa un número [0 para salir]: "))
    if number == 0: 
        continue
    if(number >= 1 and number <= len(meses)):
        print(f'Mes: {meses[number-1]}')
    else: 
        print("¡Error! El número esta fuera de rango [entre 1 y 12]")



# # 2.  Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.

tupl = (1,2,2,3,3,3,5,5,5,6,7,7,8,8,9,9,9,9,10)
number = int(input("ingrese un numero: "))

if tupl[number]:
    print("El numero ingresado se repite: ", tupl.count(number), "veces")
else:
    print("El numero ingresado no se encuentra en la tupla")



# 3. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores
# de la tupla

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
indc = int(input("Ingrese un indice: "))
a = numbers[indc]
print("El indice es " + str(indc) + " y su valor es " + str(a))