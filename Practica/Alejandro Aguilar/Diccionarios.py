# Diccionarios

# 1. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha
# en formato dd de <mes> de aaaa donde <mes> es el nombre del mes

# dias = input("Ingresa un dia: ")
# mes = input("Ingresa un mes: ")
# año = input("Ingresa un año: ")

# # fecha = dict (dia = dias ,
# #               mes = mes ,
# #               año = año)
# # print(fecha)

# meses = {"1": "Enero",
#               "2" : "Febrero",
#               "3" : "Marzo",
#               "4" : "Abril",
#               "5" : "Mayo",
#               "6" : "Junio",
#               "7" : "Julio",
#               "8" : "Agosto",
#               "9" : "Septiembre",
#               "10": "Octubre",
#               "11": "Noviembre",
#               "12": "Diciembre "}
# # print (meses)
# print ("dia" , dias, "del mes ", meses[mes], "del año", año)


# 2. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras
# en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español 
# y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla
# sin traducir.


# traduccion = {"Hola": "Hello",
#               "Dia" : "Today",
#               "Trabajo" : "Work" }
# palabras = input ("Ingrese una palabra en español: ")
# #print (traduccion[palabras])
 
# if palabras in traduccion: 
#     print (traduccion[palabras])
# else : 
#     print("No está en el diccionario.")
    
# 3. Declare un diccionario y manipule sus datos utilizando los metodos: pop, update, get, copy y zip.

meses = {"1": "Enero",
              "2" : "Febrero",
              "3" : "Marzo",
              "4" : "Abril",
              "5" : "Mayo",
              "6" : "Junio",
              "7" : "Julio",
              "8" : "Agosto",
              "9" : "Septiembre",
              "10": "Octubre",
              "11": "Noviembre",
              "12": "Diciembre "}

meses.pop ("12") # Elimina un elemento y te lo devuelve
print(meses)
copia = meses.copy() # Copiar todo el diccionario en una variable
print (copia)
meses.update ({17:"Mi dia de cumpleaños"}) # Agrega un elemento al diccionario
print(meses)
mesCumpleaños = meses.get ("9") #Recibe una clave y te devuelve el valor de esa clave
print(mesCumpleaños)


frutas = {"50": "manzanas", "99": "banana"  }
diccionariozip = zip(frutas, meses)
print(diccionariozip)




