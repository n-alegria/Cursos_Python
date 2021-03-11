''' --> Entrada y salida de datos <-- '''

# Salida de datos
'''
print()
* es una funcion predefinida de Python (built-in function)
* su tarea es imprimir por consola, terminal o interprete aquello que le pasemos por parametro
* se puede pasar como parametro: un dato, una variable o una funcion
'''

# Entrada de datos
'''
input()
* es una funcion predefinida de Python (built-in function)
* su tarea es imprimir por consola, terminal o interprete aquello que se le pida al usuario que ingrese por parametro
* dentro de los parentesis se puede poner un string que indique al usuario que es lo que espera que se ingrese
* todo lo que se ingresa por teclado es un STRING, por mas que sea un numero, para poder tratarlo diferente hay que convertirlo
'''

# type
'''
Con el metodo type() puedo saber que tipo de dato estoy usando
'''

# Manejo de datos
'''
Todo lo que ingrese por input() es un STRING por lo cual debo castearlo, hay dos formas:
* directamente en el input() --> int(input("Ingrese un numero: "))
* modificar la variable --> numero = int(numero)
'''

''' --> Operadores <-- '''
'''
* Un operador es un simbolo que se aplica a uno o varios operandos en una expresion o instruccion con el fin de obtener cierto resultado.

--> Aritmeticos
* Simbolos que se utilizan para realizar operaciones aritmeticas y manipular datos de tipo int, float y complex, 
a excepcion de + que se utiliza tambien para concatenar strings.

    +  = suma
    -  = resta / negacion
    *  = producto
    ** = potencia
    /  = division
    // = division entera
    %  = modulo

-> De asignacion
* Simbolos que se utilizan para asignar un valor a una variable.

    =   --> asigna el valor de la derecha a la variable de la izquierda
    +=  --> suma a la variable de la izquierda el valor de la derecha
    -=  --> resta a la varible de la izquierda el valor de la derecha
    *=  --> multiplica a la variable de la izquierda por el valor de la derecha
    /=  --> divide a la variable de la izquierda por el valor de la derecha
    **= --> eleva a la variable de la izquierda a la potencia de la derecha
    //= --> divide de manera entera a la varaible de la izquierda por el valor de la derecha
    %=  --> devuelve el resto de la division entre la variable de la izquierda y la derecha

-> Relacionales
* Aquellos operadores que, como su nombre lo indica, devuelven un valor booleano segun la relacion que haya entre los operandos. 
--> Todos daran como resutado True si efectivamente cumplen su tarea, de lo contrario daran como resultado False.

    ==  --> Compara que dos valores sean exactamente iguales
    !=  --> Compara si dos valores son distintos
    <   --> Evalua si el valor de la izquiera es menor que el valor de la derecha
    >   --> Evalua si el valor de la izquiera es mayor que el valor de la derecha
    <=  --> Evalua si el valor de la izquiera es menor o igual que el valor de la derecha
    >=  --> Evalua si el valor de la izquiera es mayor o igual que el valor de la derecha

-> Logicos
* Aquellos que devuelven un resultado booleano si se cumple la funcion operador. Se aplican sobre valores booleanos.add()

    and --> evalua si todos los operandos involucrados son True
    or  --> evalua si al menos uno de los operandos involucrados es True
    not --> cambia el valor del operando involucrado

-> A nivel de bit
* Las computadoras reciben informacion y la procesan en binario (unos y ceros), cada uno y cada cero que forme parte de un numero o de una palabra es un bit.
Por ejemplo, el numero binario 1000 (8 en decimal), ocupa 4 bits y 1 byte. Un byte son 8 bits, y siempre se completa el octeto con ceros a la izquierda.
'''
