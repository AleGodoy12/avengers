#1 - Escriba un programa que permita crear una lista de palabras. 
# Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. 
# Por último, el programa tiene que escribir la lista.



# num = int(input("Número de palabras:"))
# lista1 = []
# for i in range(1,num+1):
#     lista1.append(input("Palabra:"))
        
# print(lista1)



#2 - Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# pida una palabra y diga cuántas veces aparece esa palabra en la lista.


# palabra = input("Escriba una palabra")

# listadepalabras = ["Hola", "como", "como", "estas", "todo", "bien"]

# for i in listadepalabras:
#     lista = listadepalabras.count(palabra)

# print(lista)

#3.- Escriba un programa que permita crear una lista de palabras 
# y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

# num1 = int(input("Escriba cuantas palabras quiere tener su lista"))

# i = 0

# lista1 = []


# while i < num1:
#     palabra1 = input("Escriba las  palabras, para crear una lista de palabras")
#     lista1.append(palabra1)
#     i += 1


# palabra2 = input("Escriba la palabra a reemplazar")

# indice = lista1.index(palabra2)

# palabra3 = input("Escriba la nueva palabra")

# lista1.insert (indice, palabra3)
# lista1.remove (palabra2)

# print(lista1)




#Escriba un programa que permita crear una lista de palabras y que, 
# a continuación, pida una palabra y elimine esa palabra de la lista.

# num1 = int(input("Escriba cuantas palabras quiere tener su lista"))

# i = 0

# lista1 = []


# while i < num1:
#     palabra1 = input("Escriba las  palabras, para crear una lista de palabras")
#     lista1.append(palabra1)
#     i += 1

# palabra2 = input("Escriba la palabra que quiera eliminar ")


# lista1.remove(palabra2)

# print(lista1)

#5- Escriba un programa que permita crear dos listas de palabras y que, a continuación, 
# elimine de la primera lista los nombres de la segunda lista

# listadepalabras = ["Hola", "como", "como", "estas", "todo", "bien"]

# listvacia= []

# print(listadepalabras)

# palabra1= input("Ingrese las palabras que quiere eliminar de la lista")

# listadepalabras.remove(palabra1)
# listvacia.append(palabra1)
# print(listadepalabras)

# palabra2= input("¿Desea eliminar otra palabra?")

# if (palabra2 == "Si"):
#     palabra3= input("Ingrese las palabras que quiere eliminar de la lista")
#     listadepalabras.remove(palabra3)
#     listvacia.append(palabra3)
#     print(listadepalabras)
#     print(listvacia)
# else:
#     "Fin del codigo"
#     print(listvacia)


#6- Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# cree una segunda lista igual a la primera, 
# pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

listadepalabras = ["Hola", "como", "como", "estas", "todo", "bien"]

listadepalabras.reverse()

print(listadepalabras)