# def suma(a, b):
#     suma = a + b
#     resta = a-b
#     return suma, resta # Si retorno 2 elementos me los decuelve en una tupla

# variable = suma(4, 3)
# tipo = type(variable[0])
# numA = int(variable[0])
# numB = int(variable[1])
# print(variable)
# print(numA)
# print(numB)
# print(numA + numB)
# print(tipo)

# def resta(a=2, b=5):
#     return a-b

# print(resta(b=8))

'''
Los parametros por defectos van despues de los parametros normales.
'''

lista = [1, 2, 3, 4, 5]
print(lista)
lista.__delitem__(2)
print(lista)
print(lista.__getitem__(2))
print(lista.pop(0))
print(lista.remove(1))