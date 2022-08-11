# Funciones

# 1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"



""" correo = str ( input("Escriba su dirección de correo: "))

def validar (direccion):

    if ("@" in direccion):           

        print ("El correo es válido")

    else:

          print ("El correo no es valido")

validar(correo) """





# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)


# TALIA


""" def sumadigitos(a):   #Defino una función (a)
   
    digitos =[int (x) for x in str(a)]   #va a leer el elemento                 Convierto el número en un String 
    
    acumulador = 0   #declaro el acumulador ene su posicion
   
    for i in digitos:

        acumulador+=i
   
    return acumulador

numero = input("ingrese un numero")

while numero !="0": # cero como string

    print (sumadigitos(numero))

    numero = input("ingrese un numero")

print ("bucle finalizado") """



# CESAR CON PRINT


""" def sumadigitos(a):   #Defino una función (a)
   
    digitos =[int (x) for x in str(a)]   #va a leer el elemento                 Convierto el número en un String 
    
    acumulador = 0   #declaro el acumulador ene su posicion
   
    for i in digitos:

        acumulador += i

   
    print ("La suma de dígitos del número",  numero, "es: ", acumulador )


numero = input("ingrese un numero: ")

while numero != "0": # cero como string

    sumadigitos(numero)

    numero = input("ingrese un numero: ")

print ("bucle finalizado") """



# CÉSAR 


""" def limite ( digito):

    a = digito

    suma = 0

    while digito != 0:

      suma += digito % 10             #Me da el residuo y le sumo a la variable suma 

      digito = digito // 10           #La división exacta

    print (f'La suma de los dígitos del número {a} es {suma}')



numero = int (input( "Ingrese un número: "))

while numero != 0 :

    limite (numero)

    numero = int (input( "Ingrese un número: ")) """






# 3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.


#CESAR RETURN

""" def  sumadigitos (a) :                     # defino funcion (a) puede val

    digitos =[int (x) for x in str(a)]     #va a leer el elemento

    acumulador = 0                         #declaro el acumulador ene su posicion

    for i in digitos:

        acumulador+=i

    return acumulador



numero = int(input("Ingrese un numero: "))

sumatoria= 0

while numero !=0:                             # cero como string

    print ("La sumatoria de dígitos es: ",sumadigitos(numero))

    sumatoria += numero

    numero = int(input("Ingrese un numero: "))

print("La suma de los números ingresados es: ", sumatoria)


print ("Bucle finalizado")  """








# CESAR PRINT

""" def  sumadigitos (a) :                     # defino funcion (a) puede val

    digitos =[int (x) for x in str(a)]     #va a leer el elemento

    acumulador = 0                         #declaro el acumulador ene su posicion

    for i in digitos:

        acumulador+=i

    print ("La suma de dígitos del número",  numero, "es: ", acumulador )



numero = int(input("Ingrese un numero: "))

sumatoria= 0

while numero !=0:                           

    sumadigitos(numero)              #LLamo a la fuunción

    sumatoria += numero

    numero = int(input("Ingrese un numero: "))

print("La suma de los números ingresados es: ", sumatoria)


print ("Bucle finalizado")  """


# CESAR

""" def limite ( digito):

    a = digito

    suma = 0

    while digito != 0:

      suma += digito % 10             #Me da el residuo y le sumo a la variable suma 

      digito = digito // 10           #La división exacta

    print (f'La suma de los dígitos del número {a} es {suma}')



numero = int (input( "Ingrese un número: "))

sumatoria = 0

while numero != 0 :

    limite (numero)

    sumatoria += numero

    numero = int (input( "Ingrese un número: "))

print (f'La suma total de los números ingresados son: {sumatoria}') """



