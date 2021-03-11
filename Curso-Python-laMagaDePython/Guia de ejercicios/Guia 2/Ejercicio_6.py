# -*- coding: utf-8 -*-
"""
Ejercicio 6:
Escribir un programa que seleccione una operación de cuatro operaciones 
numéricas disponibles, una vez seleccionada la operación, introducir
dos números y ejecutar la operación. 
"""

operandos = ['+', '-', '*', '/']
ingreso = input('Ingrese un operando: ')
if ingreso in operandos:
    num_1 = int(input('Ingrese el primer numero: '))
    num_2 = int(input('Ingrese el segundo numero: '))
    if ingreso == '+':
        print(num_1 + num_2)
    elif ingreso == '-':
        print(num_1 - num_2)
    elif ingreso == '*':
        print(num_1 * num_2)
    else:
        print(num_1 / num_2)
else:
    print('El operando no esta disponible')