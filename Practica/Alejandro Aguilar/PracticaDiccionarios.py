# # Practica diccionarios - Evaluacion 30-8

# 1. Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios
# de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos
# mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no 
# existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta

# 2. Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. 
# El programa nos dará el siguiente menú:

# #### Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# #### Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# #### Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# #### Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario. 

diario = {}
while True:
    print("1. Añadir/modificar .")
    print("2. Buscar. ")
    print("3. Borrar. ")
    print("4. Listar. ")
    print("5. Salir. ")
    
    menu = int(input("Opción a ejecutar: "))
    
    if number == 1:
        nombre = input("Ingrese el nombre: ")
        
    
    break
print(diario)




# 3. Generar un diccionario con los nombres y numeros de camisera de la seleccion argentina

# jugadores = {"Lionel Messi" : "10",
#              "Angel Di Maria" : "11",
#              "Gonzalo Montiel" : "4"}

# print(jugadores)


# 4. Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente.
# Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.



# materias = {"Laura" : "Matematica",
#             "Federico" : "Geografia",
#             "Nicolas" : "Lengua"}
# print("La lista de docentes con sus respectivas materias es:", materias)
# materias["Matemática"] = "Esteban"
# materias["Geografia"] = "Lucia"
# print("La lista actualizada al dia de la fecha es: " , materias)