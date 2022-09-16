
lista = []
def agregaralumno():
    nombre= input("ingrese el nombre del alumno: ")
    grado = int(input("ingrese el grado del alumno: "))
    altura = float(input("ingrese la altura del alumno: "))
    curso = input("ingrese el curso del alumno(A B o C): ").capitalize()
    datos = (nombre,grado,altura,curso)
    lista.append(datos)
# confirmacion = input("desea seguir agregando alumnos? y/n")
    # while True:
    confirmacion = input("desea seguir agregando alumnos? y/n")
    if confirmacion == "y":
        agregaralumno()
    else:
         print("Alumnos agregados")
         print (lista)

agregaralumno()

# def cantAlumnos():
#     pregunta = input("De que curso quiere saber la cantidad de Alumnos? ")
#     pregunta2 = int(input("De que grado quiere saber la cantidad de alumnos? "))
#     x = 0
#     for alumno in lista:
#         if pregunta == alumno[3] and pregunta2 == alumno[1]:
#             x += 1

#     print("En el curso", pregunta, pregunta2, "Hay", x, "Alumnos")

# cantAlumnos()

def altalumnos():
    for alumno in lista:
        if alumno[1] == 5:
            print(max(alumno))
            print(min(alumno))

altalumnos()
    
