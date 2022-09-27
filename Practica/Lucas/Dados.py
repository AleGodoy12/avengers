import numpy as np

#Creacion del juego en una funcion
def tirarDados():
    num=np.random.randint(1,7,2) 
    print("Usted ha sacado", num[0],"y",num[1]) 
    resultado=num[0]+num[1] 

    if resultado>4:                                   #Si el resultado es mayor, puede intentar denuevo
        print("Obtuvo:",resultado)
        opcion=input("Desea volver a tirar? [si/no]")
        if opcion == "si":
            tirarDados()
        else:
            print("Espero que haya disfrutado el juego!") 
            return
    elif resultado==4:                                    #Si el resultado es 4 ha ganado
        print("Felicidades! Obtuvo 4. Usted ha ganado :D") 
        return
    elif resultado<4:                                     #Si el resultado es menor ha perdido
        print("Lo lamento! Obtuvo ",resultado,". Usted ha perdido :c")
        return
#Ejecucion del juego
tirarDados()


 




















#Se llama a una librería para utilizar su funcion "random" mas adelante
# Obtiene 2 numeros aleatoriamente (random) y siendo enteros (radint) del 1 al 6
#Muestra los dados obtenidos

    #Distintas opciones de acuerdo a el resultado de la suma

   #Si el resultado es mayor, puede intentar denuevo