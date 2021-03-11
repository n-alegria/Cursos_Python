# -*- coding: utf-8 -*-
"""
Ejercicio 5: Crear un diccionario con los meses del año de la forma { 1: "enero"}.
Desafío: lograr cambiar las claves.
Pista: si imprimen ítems del diccionario les crea una lista. Una vez que lo logren, 
imprimir el diccionario modificado.
"""

meses = {
    1 : 'Enero',
    2 : 'Febrero',
    3 : 'Marzo',
    4 : 'Abril',
    5 : 'Mayo',
    6 : 'Junio',
    7 : 'Julio',
    8 : 'Agosto',
    9 : 'Septiembre',
    10 : 'Octubre',
    11 : 'Noviembre',
    12 : 'Diciembre'
    }

lista_meses = list(meses.keys())
lista_numeros = list(meses.values())

meses.clear()

meses = dict(zip(lista_numeros, lista_meses))
print(meses)