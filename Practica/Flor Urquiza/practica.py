#1. Genera una lista con los valores del 1 al 100 en una lista.
def crearLista(n):
    listaNum = []
    for i in range(n):
        i +=1
        listaNum.append(i)
    return(listaNum)

print(crearLista(100)) 

#2. Crea un programa que pida un numero por teclado y guarde en una lista
# su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá
# : 5,10,15,20,25,30,35,40,45,50




#3. Crea un programa que pida al usuario números, genera en una lista, 
# cuando el usuario ingrese un 0 dejaremos de insertar. Por último, 
# muestra los números ordenados de menor a mayor.

def listaNumeros() :
    num= int(input("Escriba un numero: "))
    list [0]

    while num != 0 :
        list [0] += num
        num= int(input("Escriba un numero: "))
    
list [0]sort()