# -*- coding: utf-8 -*-
"""
Ejercicio 3: Pedir al usuario que ingrese por teclado 2 números, 
si el primero es menor que el segundo imprimir la resta entre 
el segundo y el primero, si el primero es mayor que el segundo
imprimir la suma de ambos, y si son iguales imprimir su producto. 
"""

num_1 = int(input('Ingrese el primer numero: '))
num_2 = int(input('Ingrese el segundo numero: '))

if num_1 < num_2:
    print(f'Resta: {num_2 - num_1}')
elif num_1 > num_2:
    print(f'Suma: {num_1 + num_2}')
else:
    print(f'Producto: {num_1 * num_2}')