
def separador():
    print("\n----------------------------------------------------------\n")

# Convencion de variables
print("Python utiliza Snake_Case, debo utilizar underscore entre los nombres")
print("Ejemplo: edad_promedio")
separador()

# Comentarios

print("Para utilizar comentarios de una sola línea utilizo #")
print('Para utilizar comentarios multilínea utilizo """" Comentario """ ')
print()
separador()

# Tipos de datos
print("Tipos de datos\n")
"""
Primitivos: 
Numeros --->
* int: todo aquel que sea estero, es decir, no tiene parte decimal
* float: todo aquel que tiene al menos un numero despues de la coma, incluido el cero
* complex: todo aquel que tenga parte imaginaria

String --->
* se los llama cadenas de caracteres o cadenas de texto
* se condireta string a todo conjunto de caracteres que este dentro de un entrecomillado,
puede doble o simple, pero siempre respetando el tipo de apertura y cierre

Booleanos --->
* todo aque que represente un valor de verdad: True o False
* el valor debe estar en mayuscula, de lo contrario dara error en ejecucion

Colecciones: 
Listas --->
* conjunto ordenado y mutable de elementos a los cuales se accede mediante un index que empieza por cero
* puede estar compuesta por distintos tipos de elementos

Tuplas --->
* conjunto ordenado e inmutable de elementos a los cuales se accede mediante un index que empieza por cero
* puede estar compuesta por distintos tipos de elementos
* ocupan menos memoria que una lista

Diccionarios --->
* conjunto no ordenado y mutable de elementos clave-valor (tambien llamado matriz asociativa) a los cuales se accede mediante claves
* con mutable se refiere a que los valores pueden cambiar e incluso repetirse
* las claves permanecen iguales, solo pueden eliminarse, y no pueden repetirse
* las claves pueden ser strings o int
"""
ejemplo_int = 3
ejemplo_float = 6.2
ejemplo_comp = 1+1j
ejemplo_string = "Hola Mundo" # Puedo utilizar comillas simples
ejemplo_lista = [1, 2, "Buenas tardes", 12.2, (0, 0)]
ejemplo_tupla = (1, 2, "Hello Word")
ejemplo_diccionario = {
    "nombre" : "Lautaro",
    "apellido" : "Alegria",
    "edad" : 28,
    "ocupacion" : "programador"
}
print(f"Lista: {ejemplo_int}")
print(f"Float: {ejemplo_float}")
print(f"Compusto: {ejemplo_comp}")
print(f"String: {ejemplo_string}")
print(f"Lista: {ejemplo_lista}")
print(f"Tupla: {ejemplo_tupla}")
print(f"Diccionario: {ejemplo_diccionario}")
separador()
