# Funciones

# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida 
# o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"

def direcmail (mail):
    if ("@" in mail):
        print ("Mail valido")
    else: 
        print ("Mail no valido")

mailuser = input(" Ingresa tu mail: ")
direcmail (mailuser)   



# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus
# dígitos
# (utilizando una función que realice dicha suma)

def sumaDigitos(numero):
    suma =0
    while numero!=0:
        digito = numero%10
        suma = suma+digito
        numero = numero//10
    return suma


num = int(input("Ingrese un numero : "))
while num!= 0:
    

    print("Suma:", sumaDigitos(num))
    num = int(input("Ingrese un numero : "))
    
print ("Bucle terminado")



# 3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos.
# Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar 
# la misma función realizada en el ejercicio 2.


def  sumadigitos (a) :                     # defino funcion (a) puede val
    digitos =[int (x) for x in str(a)]     #va a leer el elemento
    acumulador = 0                         #declaro el acumulador ene su posicion
    for i in digitos:
        acumulador+=i
    return acumulador
suma = 0
num = int(input("Ingrese un numero :"))
while num != 0:
    print (" Suma: " ,sumadigitos(num))
    suma = suma + num
    num = int(input(" Ingrese un numero "))
print("Sumatoria: " , suma)