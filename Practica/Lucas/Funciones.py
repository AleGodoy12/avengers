# 1.  Realiza una función que indique si un número pasado por parámetro es par o impar.

def paroimpar (numero):
    if ( numero %  2 == 0):
        return("Es par!")
    else:
        return("No es par")    
    
print(paroimpar(4))