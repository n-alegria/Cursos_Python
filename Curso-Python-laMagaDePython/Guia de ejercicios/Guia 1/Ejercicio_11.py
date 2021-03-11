'''
Ejercicio 11: Crear una lista con varios números, luego ordenarlos de manera creciente y 
devolver por pantalla la lista ordenada y cuál es el menor y cuál el mayor.
'''

lista_numerica = [12, 32, 66, 10, 43]
lista_numerica.sort()
menor = min(lista_numerica)
mayor = max(lista_numerica)

# menor = lista_numerica[0]
# mayor = lista_numerica[-1]

print(f"Lista: {lista_numerica}")
print(f"Menor: {menor}")
print(f"Mayor: {mayor}")