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

