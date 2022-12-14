#  Funciones 馃悕

1. 驴Que son? - 驴Para que sirve?
2. Sintaxis
3. Ejemplo

![funciones](/imagenes/funciones.png)

### 驴Que son y para que sirven las funciones?

### Una fu nci贸n es una porci贸n o bloque de c贸digo reutilizable que se encarga de realizar una determinada tarea.
### Cualquier funci贸n tendr谩 un nombre, unos argumentos de entrada, un c贸digo a ejecutar y unos par谩metros de salida.
### Las funciones nos ayudan a generar un codigo mas limpio y escalable porque cumplen con dos principios claves: 
### 1. El principio de reusabilidad, que nos dice que si por ejemplo tenemos un fragmento de c贸digo usado en muchos sitios, la mejor soluci贸n ser铆a pasarlo a una funci贸n. Esto nos evitar铆a tener c贸digo repetido, y que modificarlo fuera m谩s f谩cil, ya que bastar铆a con cambiar la funci贸n una vez.
### 2. Principio de modularidad, que defiende que en vez de escribir largos trozos de c贸digo, es mejor crear m贸dulos o funciones que agrupen ciertos fragmentos de c贸digo en funcionalidades espec铆ficas, haciendo que el c贸digo resultante sea m谩s f谩cil de leer.


# Sintaxis

### Para declarar una funci贸n solo se debe poner la palabra "def" seguido del nombre de la funci贸n, para el ejemplo le hemos puesto "sumar", en los par茅ntesis deben ir los par谩metros, ya hablaremos de eso m谩s adelante, por 煤ltimo la palabra "pass" es el contenido de la funci贸n. Siempre tengan en cuenta la identaci贸n dentro de la funci贸n.
![ejemplo](/imagenes/funciones1.png)

## Para terminar con la funci贸n antes declara vamos a agregar el contenido.
![ejemplo](/imagenes/funciones2.png)

#### Con esto tenemos una funci贸n que suma 5 + 10, para llamar o activar a esta funci贸n, ponemos el nombre la funci贸n seguido de par茅ntesis.

## Par谩metros

### Si bien en el ejemplo anterior creamos una funci贸n que suma 5 + 10 eso no es suficiente, ahora vamos a enviarle par谩metros a esa funci贸n y sumar los datos que le enviemos.
![ejemplo](/imagenes/funciones3.png)

#### Con esto nuestra funci贸n sumar ahora recibe 2 par谩metros, si ejecutan esto el resultado debe ser 25. Veamos otras variaciones de parametros.

![ejemplo](/imagenes/funciones4.png)
#### En este caso el par谩metro number2 tiene un valor por defecto, esto quiere decir que cuando NO se le envie ese par谩metro a la funci贸n, por defecto number2 tomar谩 el valor de 20.

# Orden de los par谩metros

### Cuando enviamos par谩metros a una funci贸n, damos por hecho que el primer valor siempre va al primer par谩metro, el segundo valor con el segundo par谩metro, y as铆 con todo los que haya, pero esto es algo que podemos cambiar gracias a Python.
![ejemplo](/imagenes/funciones5.png)

#### Al momento de llamar a la funci贸n, expl铆citamente le estamos diciendo que par谩metro va a tomar que valor, para verificar esto, impriman number1 y number2 y ver谩n el valor que tienen. Ya saben que no es necesario seguir el orden de los par谩metros en la funci贸n, pueden enviar los par谩metros en el orden que deseen pero siempre poniendo expl铆citamente el nombre del par谩metro.

