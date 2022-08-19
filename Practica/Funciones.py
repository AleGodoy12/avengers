# Funciones

# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"
# correo = str(input("ingrese su email: "))
# def valido(x):
#     if ("@" in usuario ):
#         print("direccion de email",correo , " es valido")
#     else:
#         print("email", correo, "incorrecto")    
# valido(correo)
# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)

def  suma (a) : # defino funcion (a) puede val
    digitos =[int (x) for x in str(a)]   #va a leer el elemento == x for x in a
    acumu = 0   #declaro el acumulador ene su posicion
    for i in digitos:
        acumu+=i
    return acumu

numero = int(input("ingrese un numero para suma: "))
while numero !="0": 
    print (suma(numero))
    numero = int(input("ingrese un numero para sumar, al ingresar el numero cero finalizamos: " ))
print ("fin")
       


# 3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.