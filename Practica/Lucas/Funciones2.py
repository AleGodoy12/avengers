# 1.  Realiza una función que indique si un número pasado por parámetro es par o impar.

# def paroimpar (numero):
#     if ( numero %  2 == 0):
#         return("Es par!")
#     else:
#         return("No es par")    
    
# print(paroimpar(5))

# 2. Crea una función que dados dos números mostrará todos los números que hay entre ellos

# def entrenumeros (numero1, numero2):
#     for i in (range(numero1+1, numero2)):
#         print(i)


# print(entrenumeros(1,10))


    # i = 0
    # while numero1 != numero2:
    #     if (numero1 < numero2):
    #         numero1 += 1
    #         # return(numero1)
    #     else:
    #         numero1 -= 1
    # return(numero1)

#ero de DNI, reto
# 3. Escribir una función que, dado un númrne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
# def dni (numerodni):
#     # str(numerodni)
#     if (len(str(numerodni)) == 8 or len(str(numerodni)) == 7):
#         return ("True")
#     else:
#         return("False")

# print(dni(44521489))


# 4. Escribir una función que, dado un string, retorne la longitud de la última palabra. 
# Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro

# def longitud (palabra):
#     str(palabra)

# 5.Realiza una función que sume dos números pasados por parámetros

def hola (num1,num2):
    sumita = num1 + num2
    return(sumita)

print(hola(10,20))
