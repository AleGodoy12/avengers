#1. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
# y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

meses= {"01":"enero", "02":"febrero","03":"marzo", "04": "abril", "05":"mayo","06": "junio","07": "julio", "08": "agosto", "09": "septiembre", "10": "octubre","11": "noviembre","12":"diciembre"}

dia= int(input("Ingrese el dia: "))
mes= (input("ingrese el mes: "))
año= int(input("ingrese el año: "))

print("La fecha es: ", dia ," de ", meses.get(mes), " del ", año )




#2. Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par :<traducción> separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. 
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.

#dicc= {}
#palabras= input("Ingrese las palabras en español e ingles separado por dos puntos y cada par por comas")

#for i in palabras:


#3. Declare un diccionario y manipule sus datos utilizando los metodos: pop, update, get, copy y zip.

dicc= {"nombre": "azul", "edad": "22", "animales": "perro", "comida": "pastel de papa", "color":"rosa" }

dicc.pop("color")
print("Se borra el color", dicc)

mascotas= {"animales":["gato"]}
dicc.update(mascotas)
print("Se modifica perro por gato", dicc)

print("Buscamos la edad:", dicc.get("edad"))

copia= dicc.copy()
print("Se hace copia de dicc", copia)

clave= ["nombre", "edad", "color"]
valor= ["azul", 22, "rosa"]
dicc1= zip(clave, valor)
    
for dato, info in zip(clave, valor):
    print(dato, ":", info,)

