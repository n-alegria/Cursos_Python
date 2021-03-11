# -*- coding: utf-8 -*-
"""
Ejercicio 10:
Utilizar el método range() para recorrer el iterable e imprimir 
solo los números impares entre 1 y 40 inclusive.
"""

for i in range (1, 41):
    if i % 2 != 0:
        print(i)

# Otra forma:

lista_impares = [i for i in range(1, 41) if i % 2 != 0]
print(lista_impares)