'''
Ejercicio 16:
Crear un programa que cree un diccionario vacío y lo vaya llenado con información 
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''

informacion_persona = {}
rta = 's'

while rta == 's':
    key = input('Ingrese tipo de dato: ')
    value = input(f'{key}: ')
    informacion_persona[key] = value
    print(informacion_persona)
    rta = input("¿Desea introducir más información? Presione s por sí y n por no: ").lower()
