#1. Solicitar al usuario que ingrese su dirección email. 
#Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
#Una dirección se considerará válida si contiene el símbolo "@"

email= str(input("Ingrese su dirección de email: "))
simbolo= "@"
                                                         
def validar(correo):
    emailValido= False
    for i in correo:
        if i == simbolo:
            return "Email valido"
    return "No valido"
print(validar(email))

#2. Solicitar números al usuario hasta que ingrese el cero. 
#Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)

def sumaDigitos(numero):
    suma= 0
    while numero != 0:
        digito= numero %10
        suma= suma + digito
    return suma
    
num= int(input("Ingrese números: "))
while num != 0:
    print("Suma:",sumaDigitos(num))
    num= int(input("Ingrese números: "))



#3. Solicitar números al usuario hasta que ingrese el cero. 
#Por cada uno, mostrar la suma de sus dígitos. 
#Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
#Reutilizar la misma función realizada en el ejercicio 2.

def sumaDigitos(numero):
    suma=0
    while numero != 0:
        digito=numero %10
        suma=suma + digito
    return suma

 
sumatoria=0
num= int(input("Ingrese números: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    sumatoria=sumatoria + num
    num= int(input("Ingrese números: "))
print("Sumatoria:", sumatoria)
print("Dígitos:", sumaDigitos(sumatoria))