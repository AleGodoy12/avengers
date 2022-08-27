#1.  Realiza una función que indique si un número pasado por parámetro es par o impar.

def numerosParOImpar ():
    numero= int(input("Ingrese un numero: "))
    if numero%2 ==0 :
        print ("Es Par")
    else :
        print ("Es Impar")
numerosParOImpar()

#2. Crea una función que dados dos números mostrará todos los números que hay entre ellos.
def numerosEntre():
    for i in range(5, 10):
        print(i)
numerosEntre()
#3. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es.
#  Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
dni= int(input("ingrese dni"))
def validarDni(dni):
    if len(dni)==7 or len(dni)==8:
        print("es valido")
        return True
    else:
        print("no es valido")
    return False
validarDni(dni)
#4. Escribir una función que, dado un string, retorne la longitud de la última palabra.
# Se considera que las palabras están separadas por uno o más espacios.
# También podría haber espacios al principio o al final del string pasado por parámetro
def ultima(array):
    lista=array.split()
    n=len(lista[-1])
    return n
string= input("ingtrese oracion")
print(ultima(string))
#5. Realiza una función que sume dos números pasados por parámetros
def suma(n1, n2):
    return (n1 +n2)
n1= int(input("ingrese numero"))
n2= int(input("ingrese segudno numero"))
print("la suma es:" + str(suma(n1, n2)))