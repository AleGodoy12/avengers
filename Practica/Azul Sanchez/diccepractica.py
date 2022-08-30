#1.Vamos a crear un programa en python donde vamos a declarar un diccionario 
#para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido 
# y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. 
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta

#2.Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:

#### Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
#### Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
#### Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
#### Listar: Nos muestra todos los contactos de la agenda.
#Implementar el programa con un diccionario. 



#3. Generar un diccionario con los nombres y numeros de camisera de la seleccion argentina

seleccion= {"Guzman": "1", "Mercado":"2", "Tagliafico":"3", "Ansaldi":"4", "Biglia":"5", "Fazio":"6", "Benega":"7", "Acuña":"8", "Higuaín":"9", "Messi":"10", "Di María":"11", "Armani":"12", "Meza":"13", "Mascherano":"14", "Lanzini":"15", "Rojo":"16", "Otamendi":"17", "Salvio":"18", "Aguero":"19", "Lo Selso":"20", "Dybala":"21", "Pavon":"22", "Caballero":"23"}

#4.Generar un diccionario con los nombres de las materias del secundario y el nombre de cada docente. 
# Cambiar el nombre de dos docentes y mostrar por pantalla con esta modificacion.

materias= {"matemática":"maria", "lengua":"jose", "ingles":"marta", "sociales":"lorena"}
docentes= {"lengua":["roberto"], "sociales":["manuel"]}
materias.update(docentes)
print(materias)