# Ejercicios practicos Evaluacion 16-8

# 1.  Realiza una función que indique si un número pasado por parámetro es par o impar.
numer = int(input ("Ingrese un numero: "))
def esPar(numer):
    if  ((numer %2)== 0):
        print ("Es par")
    else: 
        print ("Es Impar")
    # return (numero % 2 == 0)
esPar()


def esPar(numero):
    return (numero % 2 ==0)
print(esPar(6   ))



# # 2. Crea una función que dados dos números mostrará todos los números que hay entre ellos


def nEntre(num1, num2):
     
    if (num1 > num2):
 
        number = num1
        num1 = num2
        num2 = number
 
    for i in range(num1+1,num2):
        print(i)
 
nEntre(1,20)



# 3. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.


def vDNI(dni):
   cantidad=0
   while dni!=0:
       cantidad=cantidad+1
       dni=dni//10
   return cantidad==7 or cantidad==8
print(vDNI(39874512))


# 4. Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios.
# También podría haber espacios al principio o al final del string pasado por parámetro


def ultPalabra(frase):
   if len(frase)==0:
       return 0
   cantidad=0
   for i in range(len(frase)):
       if frase[i]!=' ':
           cantidad+=1
       else:
           if i<len(frase)-1 and frase[i+1]!=' ':
               cantidad=0
   return cantidad
print(ultPalabra("hola diagonal"))


# 5. Realiza una función que sume dos números pasados por parámetros
 
def sumas(numero1, numero2):
    return numero1 + numero2
 
resultado = sumas(5, 10)
 
print(resultado)
