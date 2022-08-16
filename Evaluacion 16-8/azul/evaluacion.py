#1. Crea una función que dados dos números mostrará todos los números que hay entre ellos

def numerosEntre():
    for i in range(5, 20):
        print(i)
numerosEntre()

#2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es.
#  Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

dni= (input("Ingrese su numero de dni"))
def validarDni(dni):
    if len(dni) == 7 or len(dni) == 8:            
        print("El Dni es válido")
        return True
    else:
        print("El Dni no es válido")
    return False

validarDni(dni)

#3. Crea una funcion que retorne tu nombre y color favorito.


nombre= "azul"
color= "rosa"
def datos(nombre, color):
    return nombre, color
print("mi nombre es: " ,nombre, "y mi color favorito es :", color)





