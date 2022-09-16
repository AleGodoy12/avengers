alumnos = [{'nombre': 'Esteban', 'altura': 170, 'grado': 5, 'curso': 'A'},
{'nombre': 'Abril', 'altura': 150, 'grado': 5, 'curso': 'C'}, {'nombre': 'Candela', 'altura': 160, 'grado': 5, 'curso': 'C'}]

def datos():
    nombre = input("Ingresa nombre del alumno: ").capitalize()
    altura = int(input("Ingresa altura del alumno: "))
    grado = int(input("Ingresa grado del alumno de 1 a 5: "))
    curso = input("Ingrese el curso del alumno A, B o C: ").capitalize()

    alumnos.append({"nombre": nombre, "altura": altura, "grado": grado, "curso": curso})

    operacion = input("Desea ingresar datos de un alumno [y/n]: ")
    if operacion == "y":     
        datos()
    elif operacion == "n":
        print("Operación terminada")

def posicionNombre(lista):
    posicion = 1
    for x in lista:
        print("Alumno:", x["nombre"], ", posicion en fila:", str(posicion))
        posicion += 1

def cantidadAlumnos(lista):
    cursoA, cursoB, cursoC = 0, 0, 0
    for x in lista:
        if x["curso"] == "A":
            cursoA += 1
        elif x["curso"] == "B":
            cursoB += 1
        elif x["curso"] == "C":
            cursoC += 1
    return cursoA, cursoB, cursoC

def altura_segun_grado(lista, grado):
    posicion = 1
    mayor = 0
    posicionMayor, posicionMenor = 0, 0  
    menor = alumnos[0]["altura"]
    for x in lista:
        if x["grado"] == grado:
            if x["altura"] > mayor:
                mayor = x["altura"]
                posicionMayor = posicion
            if x["altura"] < menor:
                menor = x["altura"]
                posicionMenor = posicion
        posicion += 1
    return mayor, posicionMayor, menor, posicionMenor

def promedioAltura(lista):
    suma = 0
    for x in lista:
        suma += x["altura"]
    promedio = suma / len(alumnos)
    return promedio

datos()

posicionNombre(alumnos)

cursoA, cursoB, cursoC = cantidadAlumnos(alumnos)

mayor, posicionMayor, menor, posicionMenor = altura_segun_grado(alumnos, 5)

promedio = promedioAltura(alumnos)

print(f"Del curso A hay: {cursoA} alumnos. Del curso B hay: {cursoB} alumnos. Del curso C hay: {cursoC} alumnos")

print(f"El alumno mas alto del curso mide: {mayor}, posicion: {posicionMayor} y el alumno mas bajo mide: {menor}, posicion: {posicionMenor}")

print(f"La altura promedio es: {promedio}")
