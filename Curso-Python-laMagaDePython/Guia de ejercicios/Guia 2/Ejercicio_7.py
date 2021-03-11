# -*- coding: utf-8 -*-
"""
Ejercicio 7:
Crear un diccionario con 5 estudiantes y sus respectivas notas. 
Imprimir por pantalla los alumnos que aprobaron y su nota 
(no en forma de diccionario, si no con nombre : nota). 
Tener en cuenta que para aprobar el alumno debe sacarse una nota
mayor o igual a 7 y menor o igual a 10.
"""

diccionario = {
    'Juan' : 8,
    'Carlos' : 1,
    'Santiago' : 3,
    'Ana' : 10,
    'Sabrina' : 7
    }

for nombre, nota in diccionario.items():
    if nota > 6:
        print(f'{nombre} : {nota}')

