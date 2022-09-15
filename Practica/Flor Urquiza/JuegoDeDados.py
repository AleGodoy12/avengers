import random # Importamos un archivo que contiene las funciones que nos ayuda a generar números aleatorios.
    
# Genera dos números aleatorios entre 1 y 6, los suma y retorna el resultado.
def lanzarDados():
    dadoUno = random.randint(1, 6) 
    dadoDos = random.randint(1, 6)
    sumaDados = dadoUno + dadoDos
    print(f"\nValor dado 1: {dadoUno}")
    print(f"Valor dado 2: {dadoDos}")
    print(f"La suma de los dados es: {sumaDados}")
    return sumaDados

# Hicimos otra funcion que se encarga de empezar el juego.
def juegoDeDados(): 
    # Guardo en la variable "respuesta" la opción elegida por el usuario.
    respuesta = input("\n==================\n [JUEGO DE DADOS]\n==================\n[1] Lanzar dados\n[2] Salir\nOpción: ") 
    while respuesta == "1": # El bucle se va a repetir mientras el usuario ingrese [1], es decir, que quiere seguir lanzando los dados. [Revisión]        
        resultadoDados = lanzarDados() 
        if resultadoDados == 4:
            print ("\n¡¡¡Ganaste el juego!!!")
        elif resultadoDados < 4:
            print ("\n¡Perdiste! Juego terminado.\n")
            break
        else:
            print ("\n¡Te pasaste de 4! Inténtalo de nuevo.")
        respuesta = input("\n  ¿Seguir jugando? \n[1] Lanzar los dados \n[2] Salir \nOpción: ")

juegoDeDados()