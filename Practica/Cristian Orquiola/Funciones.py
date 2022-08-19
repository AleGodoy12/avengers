# Funciones

#1. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"

# usuario= input("ingrese su direccion email: ")

# condi = "@"
# def x(correo):
#     valido = False
#     for i in correo:      #for = recorrer # i = iterar "recorre"
#         if i ==condi:  # i = iterar "recorre elemento x elemnto"  
#          return"su email es valido"
      
#     return"su email no es valido"
# print(x(usuario))        


#2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)
 # el ciclo for recorrelos elementos hasta terminar, el ciclo while recorre el elemento hasta encontrar la condicion y dowhile recorre si se cumple la condicion

def suma(a):

   numeros= int(input("ingrese numeros para sumar, al ingresar el numero cero terminamos: "))
   num = 0 

   while numeros != "0":    
      for i in numeros:
       numeros += int(numeros)
      print(num)
      num = 0
      numeros= int(input("ingrese numeros para sumar, al ingresar el numero cero terminamos: "))
      print("fin")
suma()      
      
    
   


#3. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.


