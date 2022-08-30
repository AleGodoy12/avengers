#1. Genera una lista con los valores del 1 al 100 en una lista.

lista= list(range(1, 101))
print(lista)

#2. Crea un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. 
#Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

numero= int(input("Ingrese un número: "))
lista= []

for i in range(1, 11):
    lista.append(i* numero)
print(lista)

#3. Crea un programa que pida al usuario números, 
#genera en una lista, cuando el usuario ingrese un 0 dejaremos de insertar. 
#Por último, muestra los números ordenados de menor a mayor.


def listaNumeros():
    num= int(input("Ingrese numeros: "))
    acumulador= 0
    lista= []
    while num != 0:
        lista.append(num)
        num= int(input("Ingrese numeros: "))
    lista.sort()
    return lista
listaNumeros()
        



#4. Crea un programa que pida al usuario números, genera en una lista, 
#cuando el usuario ingrese un 0 dejaremos de insertar. 
#Por último, muestra los números ordenados de mayor a menor.

def mayor():
    num= int(input("Ingrese numeros: "))
    lista= []
    while num != 0:
        lista.append(num)
        num= int(input("Ingrese numeros: "))
    lista.sort(reverse=True)
    print(lista)
mayor()