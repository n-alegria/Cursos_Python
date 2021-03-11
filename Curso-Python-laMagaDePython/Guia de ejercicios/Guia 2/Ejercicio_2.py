# -*- coding: utf-8 -*-
"""
Ejercicio 2: Crear una lista con 10 números enteros cualquiera. 
Indicar cuál es el número mayor y cuál es el número menor. 
Si al menos hay 3 números mayores a 100, imprimir esos números, 
si no, imprimir los números menores a 50 que formen parte de la lista.
"""

lista = [20, 500, 150, 5, 9, 10, 80, 6, 2000, 40]
lista.sort()

menor = lista[0]
mayor = lista[-1]
acumulador = 0

for numero in lista:
    if(numero >= 100):
        acumulador += 1

if acumulador >= 3:
    for numero in lista:
        if numero >= 100:
            print(numero)
else:
    for numero in lista:
        if numero <= 50:
            print(numero)