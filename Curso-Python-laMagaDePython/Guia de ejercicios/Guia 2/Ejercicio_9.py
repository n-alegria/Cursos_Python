# -*- coding: utf-8 -*-
import operator

"""
Ejercicio 9: 
Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito. 
Evaluar si puede realizar una compra de $2500, si puede indicar cuánto
saldo le queda luego de efectuarla. Si no puede, indicar cuánto dinero
le falta para poder realizarla.
"""

compra = 2500
monto_disponible = int(input('Ingrese saldo de su tarjeta: '))

if monto_disponible >= compra:
    print(f'Saldo restante: ${operator.neg((compra - monto_disponible))}')
else:
    print(f'Le faltan: ${compra - monto_disponible}')