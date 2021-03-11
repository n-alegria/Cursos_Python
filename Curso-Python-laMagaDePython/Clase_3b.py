''' --> Estructuras de control de flujo --> '''
'''
* El flujo del programa sigue la logica Top-Down.
* La mayoria de las veces que creamos y codeamos un programa, necesitamos chequear ciertas condiciones y ver que camino seguir y/o cuantas veces.
Para esto, se utilizan las estructuras de control de flujo.
--> Se dividen en dos grupos: Condicionales e Iterativas

--> Condicionales <--
* Permiten comprobar condiciones y hacer que el programa se comporte de una forma u otra, 
que ejecute un fragmento de codigo u otro, dependiendo del valor de verdad de esa condicion.

-> Sentencia if
* Es la forma mas simple de crear una estructura de flujo condicional, if, en español "si", seguido de
la o las condiciones a evaluar, y luego dos puntos. En caso de que la o las condiciones resulte/n 
falsa/s, el programa seguira a la proxima instruccion, dejando sin efecto el codigo dentro del if.

if condicion:
    bloque de codigo...

-> Sentencia if-else
* Muchas veces, si la condicion es false, no vamos a quere que el programa continue a la siguiente
instruccion sino que ejecute in codigo particular. Para eso existe la sentencia if-else, en español
si-si no. Si la condicion es verdadera se ejecuta el codigo luego del if, si es false, se ejecuta el
codigo luego del else.

if condicion:
    bloque de codigo...
else:
    bloque de codigo...

-> Sentencia if-elif
* En otros lenguajes elif seria else if, es decir, es para crear un else (si la condicion es falsa)
y agregarle una condicion a ese else. Luego puede ir un else al final o no.

if condicion_uno:
    bloque de codigo...
elif condicion_dos:
    bloque de codigo...
else:
    bloque de codigo...

-> Sentencias if anidadas if-if-if
* Estas sentencias se utilizan cuando, luego de comprobar si una condicion es True, se desea comprobar
otra u tras condicion/es. Es decir, cada subcondicion depende de la verdad de la anterior para ser comprobada o no.

if condicion:
    bloque de codigo...
    if condicion_anidada:
        bloque de codigo...
        if condicion_anidada2:
            bloque de codigo...
        else:
            bloque de codigo...

--> Iterativas <--
* Las estructuras de control de flujo iteraticas permiten ejecutar un mismo fragmento de codigo un cierto numero de veces,
mientras se cumpla una determinada condicion. Estas estructuras son a menuda llamadas bucles.

-> Bucle while
* El bucle while, en español mientras, ejecuta un fragmento de codigo mientras cierta condicion permanece verdadera.

while condicion:
    bloque de codigo...

-> Bucle for
* A diferencia de otro lenguajes de programacion, en Python for se utiliza para recorrer objetos iterables.
Un objeto iterable es aquel que puede ser recorrido elemento a elemento, por ejemplo una lista, una tupla, un diccionario.

for elemento in objeto:
    bloque de codigo...

-> Sentencias pass, break, continue

* pass: devuelve NULL al leer el interior de un bucle, como si estuviera vacio (que puede estarlo). Se suele utilizar cuando 
se esta creando una funcion pero aun no se determino su tarea, o una clase y aun no tiene atributos y metodos propios.

* break: termina el bucle actual y salta a la siguiente instruccion del programa.

* continue: salta a la siguiente iteracion del bucle, ignorando el actual.
'''