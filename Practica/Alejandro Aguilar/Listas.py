# Listas

# 1. Genera una lista con los valores del 1 al 100 en una lista.

lista = []
numero = 0
while numero <=100 : # Mientras que 100 sea mayor 
    
    lista.append (numero) #Agrega un valor al final de la lista
    numero +=1  # Suma 1 a la variable numero
print (lista)

# 2. Crea un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. 
# Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

lista = []
number = int(input("Ingresa un numero: "))

aumento = 1

while aumento <=10 :
    resultado = number * aumento
    lista.append (resultado)
    aumento +=1
    
print (lista)

# 3. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese un 0 dejaremos
# de insertar. Por último, muestra los números ordenados de menor a mayor.

lista = []
digitos = int(input("Ingresa un numero: "))


while digitos !=0 :
    lista.append (digitos)
    digitos = int(input("Ingresa un numero: "))

lista.sort() #Sort ordena de menor a mayor por defecto 
print (lista)


# 4. Crea un programa que pida al usuario números, genera en una lista, cuando el usuario ingrese
# un 0 dejaremos de insertar. Por último, muestra los números ordenados de mayor a menor.

lista = []
digitos = int(input("Ingresa un numero: "))


while digitos !=0 :
    lista.append (digitos)
    digitos = int(input("Ingresa un numero: "))

lista.sort(reverse = True) #Sort ordena de mayor a menor
print (lista)