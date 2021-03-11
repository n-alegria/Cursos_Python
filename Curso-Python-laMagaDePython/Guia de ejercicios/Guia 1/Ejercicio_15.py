'''
Ejercicio 15: 
Crear un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos 
de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura>
es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso.
'''

diccionario = {
    'Matemáticas' : 6,
    'Física' : 4,
    'Química' : 5
}
total_creditos = 0

print()
for i, k in diccionario.items():
    print(f'{i} tiene {k} créditos')

for i in diccionario.values():
    total_creditos += i

print(f'\nEl total de creditos del curso es: {total_creditos}')