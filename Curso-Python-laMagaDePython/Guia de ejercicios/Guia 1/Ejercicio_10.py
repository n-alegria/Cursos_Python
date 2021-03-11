'''
Ejercicio 10: Escribir un programa que almacene todas las letras del abecedario y 
luego elimine las vocales y nos devuelva una lista sin las vocales, sin modificar la original.
'''

abecedario = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
vocales = ['a', 'e', 'i', 'o', 'u']
lista_sin_vocales = list(abecedario)


for i in abecedario:
    for k in vocales:
        if i == k:
            lista_sin_vocales.remove(i)

print(lista_sin_vocales)