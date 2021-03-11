'''
Ejercicio 14: Crear un programa que pregunte al usuario
su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje.
'''

diccionario = {}

diccionario['nombre'] = input("Ingrese su nombre: ")
diccionario['edad'] = int(input("Ingrese su edad: "))
diccionario['direccion'] = input("Ingrese su direccion: ")
diccionario['telefono'] = int(input("Ingrese su telefono: "))

print(f'{diccionario}\n')
for i, k in diccionario.items():
    print(f'{i}: {k}')
