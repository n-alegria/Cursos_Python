# -*- coding: utf-8 -*-
"""
Ejercicio 4: Ingresar 6 números por teclado, 
preferentemente enteros, ordenarlos de manera 
creciente e imprimirlos por pantalla.
"""

lista = []
while len(lista) < 6:
    lista.append(int(input('Ingrese un numero: ')))
    
lista.sort()
print(lista)

