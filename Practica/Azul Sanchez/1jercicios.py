# #1. Solicitar al usuario que ingrese su dirección email. 
# #Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
# #Una dirección se considerará válida si contiene el símbolo "@"

# email= str(input("Ingrese su dirección de email: "))
# simbolo= "@"
                                                         
# def validar(correo):
#     for i in correo:
#         if i == simbolo:
#             return "Email valido"
#     return "No valido"
# print(validar(email))

# #2. Solicitar números al usuario hasta que ingrese el cero. 
# #Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)

# def  sumadigitos (a) :                     # defino funcion (a) puede val
#     digitos =[int (x) for x in str(a)]     #va a leer el elemento
#     acumulador = 0                         #declaro el acumulador ene su posicion
#     for i in digitos:
#         acumulador+=i
#     return acumulador
# numero = input("Ingrese un numero")
# while numero !="0":                        # cero como string
#     print (sumadigitos(numero))
#     numero = input("Ingrese un numero")
# print ("Bucle finalizado")



#3. Solicitar números al usuario hasta que ingrese el cero. 
#Por cada uno, mostrar la suma de sus dígitos. 
#Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
#Reutilizar la misma función realizada en el ejercicio 2.

def  sumadigitos (a) :                     # defino funcion (a) puede val
    digitos =[int (x) for x in str(a)]     #va a leer el elemento
    acumulador = 0                         #declaro el acumulador ene su posicion
    for i in digitos:
        acumulador+=i
    return acumulador

sumatoria= 0
numero = int(input("Ingrese un numero"))

while numero !=0:                             # cero como string
    print ("Suma:",sumadigitos(numero))
    sumatoria=sumatoria+numero
    numero = int(input("Ingrese un numero"))
print("Sumatoria:", sumatoria)
print("Suma de dígitos:", sumadigitos(sumatoria))  
  
print ("Bucle finalizado") 