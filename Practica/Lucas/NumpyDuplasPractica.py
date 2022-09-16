
import numpy as np

# 1. Crear una matriz 3x3 con valores del 0 al 8

# arr = np.arange(0,9).reshape(3,3)

# print(arr)


#2. Crear una matriz de identidad de 3x3

# arr = np.identity(3)

# print(arr)

# 3. Utilizar numpy para geneara un numero aleatorio entre 0 y 1

# numero = np.random.random()

# print(numero)

# 4. Utilizar numpy para generar un arreglo de 
# 25 numeros aleatorioas con una  distribucion normal

# arreglo = np.random.normal(0,2,25)

# print(arreglo)

#5. Crear la siguiente matriz

# matriz = np.arange(0.01,1.01,0.01).reshape(10,10)

# print(matriz)

#6 6. Crear un arreglo de 20 valores lineales entre 0 y 1

# matriz=np.arange(0,1.001,0.05263158)
# print(matriz)


#7. Generar pares de apellidos y nombres y devolver sus índices. 
# (primero por apellido, luego por nombre).

# apellido =    ('Gramajo',    'Rusas', 'Gramajo')
# nombres = ('Lucas', 'Abril', 'Agustin')
# print (np.lexsort((apellido, nombres)))