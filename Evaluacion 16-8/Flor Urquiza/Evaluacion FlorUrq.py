#1. Crea una función que dados dos números mostrará todos los números que hay entre ellos

def numeros():
    for i in range(0, 22):
        print(i)
numeros()

#2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es.
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def validacionDNI(dni):
    dni= (input("Ingrese DNI: "))
    if len(dni) >=7 or len(dni)==8:
        print("¡El DNI es válido!")
        return True
    else:
        print("DNI inválido")
    return False
validacionDNI(dni)

#3. Crea una funcion que retorne tu nombre y color favorito.
def nombreYcolor ():
    nombre= input("Ingrese su nombre: ")
    color= input("Ingrese su color favorito: ")
    return 'Su nombre es', nombre, 'y su color favorito es', color
nombreYcolor()

#Flor, venimos avanzando con mayor seguridad cada vez, la evaluacion y tu forma de resolver los ejercicios
#no es mas que una muestra de eso. Incluyes e integras los conocimientos y eso hace que cada vez que te enfrentas a una consigna
#sean menos las dudas y mas las ideas de como resolverlo.

#10/10