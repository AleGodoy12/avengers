# Listas

# 1. Genera una lista con los valores del 1 al 100 en una lista.


""" lista = []

for i in range (1, 101):

    lista.append(i)

print (lista) """



# 2. Crea un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50


""" numero = int ( input ("Escribe un número: "))

lista = []

multiplicador = 10

for i in range (1, multiplicador + 1 ):

    resultado = numero * i 

    lista.append(resultado)

print ("El resultado de la multiplicación del número ", numero, " = ",  lista) """


# 3. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.


""" numero = int (input ("Escribe un número: "))

numeroLimite = 0

lista = []

while numero != numeroLimite :

    lista.append ( numero)

    numero = int (input ("Escribe un número: "))


lista.sort()

print(lista)  """



# 4. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor.

numero = int (input ("Escribe un número: "))

lista = []

numeroLimite = 0

while numero != numeroLimite: 

    lista.append(numero)

    numero = int (input ("Escribe un número: "))

lista.sort (reverse = True)     # De MAYOR a MENOR

print(lista)

    