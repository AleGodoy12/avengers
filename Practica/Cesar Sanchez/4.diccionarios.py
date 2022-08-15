# Diccionarios

# 1. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes

""" dia = int (input ("Ingrese un día: "))
mes = int (input("Ingrese el número del mes : "))
anio = int (input("Ingrese año: "))

mesesAnio = { 1 : "enero", 2 : "febrero",3 : "marzo",4 :  "Abril", 5 : "Mayo", 6 : "Junio", 7 : "Julio", 8 : "Agosto", 9 : "Septiembre", 10 : "Octubre", 11 : "Noviembre", 12 : "Diciembre" }

print ("La fecha que ingreso es ", dia ,"/",mesesAnio[mes], "/",anio) """


# 2. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.


""" diccionario = { "hola" : "Hello", "buen día" : "good day", "¿cómo estás? ": "How are you" , "hasta luego": "Bye" }

palabra = str (input ("Escribe una palabra: ")).lower()

if palabra in diccionario :

    print ("La traducción de ", palabra, "es: ", diccionario[palabra])

else:
    print("La palabra ingresada no se encuentra en el diccionario") """



# 3. Declare un diccionario y manipule sus datos utilizando los metodos: pop, update, get, copy y zip.

""" diccionario = dict (zip("abcdefgh", [1, 2, 3, 4, 5, 6, 7, 8]))

print(diccionario) """

# pop         

""" diccionario.pop ("d")

print(diccionario) """

# update

""" diccionario.update({"i": 9})

print(diccionario) """

# get

""" clave = diccionario.get("b")

print (clave) """

# copy

""" copia = diccionario.copy()

print(copia) """

