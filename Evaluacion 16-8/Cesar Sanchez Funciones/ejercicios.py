# Evaluacion 16-8

# 1. Crea una función que dados dos números mostrará todos los números que hay entre ellos

""" numero1 = int (input ("Escribe el primer número: "))

numero2 = int (input ("Escribe el segundo número: "))

def numerosIntermedios (num1, num2):

    while num1 < num2- 1:

        num1 += 1

        print("Los números intermedios son: ", num1)


numerosIntermedios(numero1, numero2) """


# 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

""" numero = int (input ("Escrtibe el número de DNI: "))

def documento (dni):

    cantidad = 0

    while dni != 0 : 

        cantidad += 1

        dni = dni // 10

    return cantidad == 7 or cantidad == 8

print(documento( numero )) """




# 3. Crea una funcion que retorne tu nombre y color favorito.

""" tuNombre = str (input ("Escribe tu nombre: "))

colorFavorito = str ( input ("Escribe tu color favorito: "))

def nombre (nombre, color):

    c = print ("Tu nombre es", nombre, " y tu color favorito es ", color)

    return c

nombre(tuNombre, colorFavorito) """

