#1 Crea una función que dados dos números mostrará todos los números que hay entre ellos

# def entrenumeros (num1, num2):
#      for i in (range(num1+1, num2)):
#          print(i)

# print(entrenumeros(10,20))


#2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.


# def dni (numerodni):
#     # str(numerodni)
#     if (len(str(numerodni)) == 8 or len(str(numerodni)) == 7):
#         return ("True")
#     else:
#         return("False")

# print(dni(12345678))


#3

nomuser = input("Introduzca su nombre")

coloruser = input("Introduzca su color favorito")

def nombreycolor (nomuser, coloruser):

    # nomuser = input("Introduzca su nombre")

    # coloruser = input("Introduzca su color favorito")

    # print("Felicidades tu nombre es: ", nomuser,  " y tu color favorito es el ", coloruser)
    return nomuser, coloruser

print("Felicidades tu nombre es: ", nomuser,  " y tu color favorito es el ", coloruser)
 



