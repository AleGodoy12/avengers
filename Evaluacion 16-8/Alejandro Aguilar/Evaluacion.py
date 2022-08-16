# Evaluacion 16-8

# 1. Crea una función que dados dos números mostrará todos los números que hay entre ellos


def nEntre(num1, num2):
     
    if (num1 > num2):
 
        number = num1
        num1 = num2
        num2 = number
 
    for i in range(num1+1,num2):
        print(i)
 
nEntre(1,20)

# # 2. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# # Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.


def vDNI(dni):
   cantidad=0
   while dni!=0:
       cantidad=cantidad+1
       dni=dni//10
   return cantidad==7 or cantidad==8
print(vDNI(39874512))


# 3. Crea una funcion que retorne tu nombre y color favorito.

def nombre():
    name = "Alejandro"
    color = "amarillo" 
    return name, color

nameCol = nombre()
print(nameCol)
