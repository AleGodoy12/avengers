# 2. Generar una matriz de 3 filas y 3 columnas
# Eliminar la primera fila y transformar en una matriz de 3x2

import numpy as np 

arr = np.arange(10,100,10)
newarr = arr.reshape(3,3)
nuevamatriz = np.delete(newarr,0,0)

nuevamatriz = nuevamatriz.reshape(3,2)
print(nuevamatriz)
