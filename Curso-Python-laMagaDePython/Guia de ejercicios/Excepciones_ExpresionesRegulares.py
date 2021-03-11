# -*- coding: utf-8 -*-
import re, sys

# EXCEPCIONES
'''
Una excepcion es un error que ocurre durante la ejecicion de un programa pero
que no esta en la sintaxis del codigo.
Para evitar que se produzcan errores se utiliza la sentencia 'try-except'
'''

def dividir(a, b):
    try:
        return a / b
    except  ZeroDivisionError:
        return f'No se puede dividir por cero. Operacion Fallida'

print(dividir(8,0))

'''
Aplicando 'try-except', lo que hacemos es indicar que, si está todo ok se efectua el calculo,
y si aparece el ZeroDivisionError se devuelve el string de aviso.
Al ejecutar la funcion dividir(), se intentara realziar excepto que el parametro 'b' sea 0
y devolvera ese mensaje.

Tambien se puede utilizar a sentencia 'finally' que no es obligatoria, pero siempre que este
se ejecutara, haya o no error.

# Lanzar una excepcion
Tambien puedo lanzar excepciones utilizando 'raise'
'''
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError('No valido', 'Chau')
    else:
        return a / b

try:
    print(dividir(8,0))
except Exception:
    e = sys.exc_info()[1]
    print(e.args)

# EXPRESIONES REGULARES

'''
Una expresion regular es una secuencia de caracteres que forma un patron que sirve
para realiar busquedas y filtrar datos.

Para poder utilizar las regex, hay que importar la libreria re:

import re

La sintaxis es: re.metodo(patron, variable)
'''

texto = 'Mi nombre  es lautaro y tengo 28 años'
buscar = 'nombre'

if re.search(buscar, texto):
    print(f'La cadena contiene {buscar} entre sus caracteres')
else:
    print(f'La cadena no contiene {buscar} entre sus caracteres')

texto_encontrado = re.search(buscar, texto)
print(texto_encontrado.start()) # Me devolvera la posicion del primer caracter de la cadena donde se encuentra
print(texto_encontrado.end()) # Me devolvera la posicion del caracter siguiente al ultimo de donde se encuentra
print(texto_encontrado.span()) # Devuelve una tupla de dos numeros, el primero es start() y el segundo end()

cadena = 'Me gusta la programacion, estudie programacion, trabajo en programacion'
buscar = 'programacion'

print(re.findall(buscar, cadena)) # Devolvera una lista con la cantidad de veces que aparece el patron en la cadena
print(len(re.findall(buscar, cadena))) # Devolvera la cantidad de veces que aparece el patron en la cadena


# METACARTERES

'''
Se conoce como metacaracteres a aquellos que, dependiendo del contecto, tienen un significado especial
para las expresiones regulares.
Algunos autores los llaman 'caracteres comodin'

Tipos:
-> Anclas
-> Clases de caracteres
-> Rangos
-> Universal
-> Cuantificadores
'''

'''
[ ANCLAS ]

Indican que lo que queremos encontrar se encuentra al principio o al final de la cadena.
Combinandolas, podemos buscar algo que represente a una cadena entera.

-> ^patron: coincide con cualquier cadena que comience con patron.
-> patron$: coincide con cualquier cadena que termine con patron.

[ CLASES DE CARACTERES ]
Se utilizan cuando se quiere buscar un caracter dentro de varias posibles opciones.
Una clase se delimita entre corchetes y lista posibles opciones para el caracter que representa.

-> [abc]: coincide con a, b o c
-> [387ab]: coincide con 3, 8, 7, a o b
-> niñ[oa]s: coincide con niños o niñas
-> Para evitar errores, en caso de que queramos crear una clase de caracteres que contenga un corchete,
debemos escribir una barra (\) delante, para que el motor de expresiones regulares lo considere un
caracter normal: la clase [ab\[] coincide con a, b y [. ]

[ RANGOS ]
Si queremos encontrar un numero, podemos usar una clase como [0123456789], o podemos utilizar un rango.
Un rango es una clase de caracteres abreviada que se crea escribiendo el primer caracter del rango,
un guion y el ultimo caracter del rango. Multiples rangos pueden definirse en la misma clase de caracteres.
-> [a-c]: equivale a [abc]
-> [0-9]: equivale a [0123456789]
-> [a-d5-8]: equivale a [abcd5678]
-> Es importante aclarar que si se quiere buscar un guion debe colocarse al principio o final de a clase
[a4-] [-a4] [a\-4]

[ * RANGOS NEGADOS ]
Asi como podemos listar los caracteres posibles en cierta posicion de la cadena, tambien podemos listar
caracteres que no deben aparecer.
-> [^abc]: coincide con cualquier caracter distinto de a, b y c

[ UNIVERSAL ]
Coincide con cualquier caracter '.'

[ CUANTIFICADORES ]
Son caracteres que multiplican el patron que les precede.
-> **?**: coincide con cero o una ocurrencia del patron. Dicho de otra forma, hace que el patron
sea opcional.
-> **+**: coincide con una o mas ocurrencias del patron.
-> *****: coincide con exactamente x  ocurrencias del patron.
-> **{x, y}**: coincide con al menos x y no mas de y ocurrencias. Si se omite x, el minomo es cero,
y si se omite y, no hay maximos. Esto permite especificar a los otros como casos particulares: ? es {0,1},
+ es {1,} y * es {,} o {0,}.

'''