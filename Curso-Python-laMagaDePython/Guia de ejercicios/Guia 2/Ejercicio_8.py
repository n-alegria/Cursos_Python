# -*- coding: utf-8 -*-
"""
Ejercicio 8:
Pedirle al usuario que ingrese por teclado 3 números binarios de 8 bits,
para cada uno imprimir su siguiente (número + 1) pero en sistema decimal. 
Recuerden que los números binarios están compuestos por 1 y 0. 
"""

decimal = 0
for i in range(3):
    binario = input("Ingrese un numero binario: ")
    for bit in binario:
        decimal += decimal + int(bit)
    print(decimal + 1)
    decimal = 0