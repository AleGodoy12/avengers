def  sumadigitos (a) :                     # defino funcion (a) puede val
    digitos =[int (x) for x in str(a)]     #va a leer el elemento
    acumulador = 0                         #declaro el acumulador ene su posicion
    for i in digitos:
        acumulador+=i
    return acumulador
sumatoria= 0
numero = int(input("Ingrese un numero: "))
while numero !=0:                             # cero como string
    print ("Suma:",sumadigitos(numero))
    sumatoria=sumatoria+numero
    numero = int(input("Ingrese un numero: "))
print("Sumatoria:", sumatoria)
print("Suma de dígitos:", sumadigitos(sumatoria))
print ("Bucle finalizado")