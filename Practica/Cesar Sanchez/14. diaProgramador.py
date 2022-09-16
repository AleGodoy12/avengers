
# En una secundaria, los alumnos que estuvieron presentes, se han formado en una fila por orden de llegada. 

# Con el objeto de llevar registros sobre el crecimiento de los adolescentes, el profesor necesita realizar ciertos cálculos sobre las alturas de los alumnos.

# En la secundaria hay 5 años, de primero a quinto (de 1 a 5), y de cada grado hay tres cursos (‘A’,’B’ y ‘C’).

# De cada alumno/a se conoce la siguiente información:

# ● Nombre (valor cadena).

# ● Altura en cm (valor entero).

# ● Grado (valor entero de 1 a 5).

# ● Curso al que pertenece (valor: ‘A’, ‘B’ o ‘C’).

lista = []

def agregaralumno():

    nombre= input("ingrese el nombre del alumno: ")

    grado = int(input("ingrese el grado del alumno de 1 a 5: "))

    altura = float(input("ingrese la altura del alumno en cm: "))

    curso = input("ingrese el curso del alumno (A B o C): ").capitalize()

    datos = (nombre,grado,altura,curso)

    lista.append(datos)

# confirmacion = input("desea seguir agregando alumnos? y/n")

    confirmacion = input("desea agregar alumnos? y/n: ").lower()


    if confirmacion == "y":

        agregaralumno()       # Llamo a mi función agregar alumno 

    else:
        print("Alumnos agregados son: ", lista)

        # confirmacion = input("desea agregar alumnos? y/n: ").lower()


agregaralumno()


# Para ayudar a al profesor, se te pide que desarrolles una aplicación,que obtenga los siguientes resultados:

# a) Por cada alumno/a, informar su nombre y su posición en la fila. Al finalizar, informar:

def nombrePosicion ():

    posicion = 0 

    for i in lista :

        print (f'{posicion} : {i[0]}')

        posicion += 1


nombrePosicion()


# b)La cantidad de alumnos en la fila, de cada curso.


def posicionFila ():

    cursoA, cursoB, cursoC = 0, 0, 0

    for i in lista: 

        if i [3] == "A":

            cursoA += 1
        
        elif i [3] == "B":

            cursoB += 1

        elif i [3] == "C":

            cursoC += 1
    
    print(f'El curso A tene :{cursoA} alumnos ,el curso B tiene:{cursoB} alumnos y el curso C tiene:{cursoC} alumnos ')


posicionFila()

# c) La altura del alumno más alto y la del más bajo (se suponen únicos), indicando en ambos casos, su posición en la fila.

# Considerar sólo a los alumnos de quinto grado.





def alumnoAlto ():

    altura= []

    for i in lista:

        if i[1] == 5:

            altura.append(i[2])
    
    maximaAltura = max(altura)

    for i in lista: 

        if [1] == 5 and i [2] == maximaAltura:

            posicionAlturaMaxima= lista.index(i)

    print("el alumno mas alto del 5 año mide ", maximaAltura," y esta en la posicion ",posicionAlturaMaxima)          

    # print (f'El alumno mas alto del 5 mide {maximaAltura} y está en la posición {posicionAlturaMaxima}')
alumnoAlto()


def alumnoBajo ():

    altura = []

    for i in lista:

        if i[1] == 5:

            altura.append(i[2])
    
    minimaAltura = min(altura)

    for i in lista: 

        if [1] == 5 and i [2] == minimaAltura:

            posicionAlturaMinima= lista.index(i)

    # print ("el alumno mas alto del 5 año mide", maximaAltura,"y esta en la posicion",posicion)

    print("el alumno mas alto del 5 año mide ", minimaAltura," y esta en la posicion ",posicionAlturaMinima)       

    # print (f'El alumno mas alto del 5 mide {minimaAltura} y está en la posición {posicionAlturaMinima}')

alumnoBajo()

# d) El promedio de las alturas, considerando a los alumnos de todos los años.

# Se ingresan datos de alumnos hasta que el usuario lo determine


def promedioAltura ():

    acumulador = 0

    for i in lista:

        acumulador += i [2]

    promedioTotal = acumulador / len(lista)

    print (f'El promedio de altura de todos los alumnos es: {promedioTotal} ')

promedioAltura()








