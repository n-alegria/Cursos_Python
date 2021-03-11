"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su ID,
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
donde preferente tendrá el valor True si se trata de un cliente preferente.
El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
(5) Listar clientes preferentes, (6) Terminar.

En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el ID del cliente y eliminar sus datos de la base de datos.
Preguntar por el ID del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su ID y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su ID y nombre.
Terminar el programa.
"""

clientes = {}
opcion = ''

while opcion != '6':
    print('''
    1) Añadir cliente.
    2) Eliminar cliente.
    3) Mostrar cliente.
    4) Listar todos los clientes.
    5) Listar clientes preferentes.
    6) Terminar.
    '''
    )
    opcion = input('Ingrese una opcion: ')
    if opcion == '1':
        print('\n Alta cliente. \n')
        id = input('Ingrese ID del cliente: ')
        nombre = input('Ingrese nombre del cliente: ')
        direccion = input('Ingrese direccion dle cliente: ')
        telefono = input('Ingrese el telefono del cliente: ')
        correo = input('Ingrese el correo del cliente: ')
        preferente = input('Es cliente preferente? [S/N]: ').upper()
        cliente = {'nombre' : nombre, 'direccion' : direccion, 'telefono' : telefono, 'correo' : correo, 'preferente' : preferente == 'S'}
        clientes[id] = cliente
    if opcion == '2':
        print('\n Baja cliente. \n')
        id = input('Ingrese el id del cliente: ')
        if id in clientes:
            del clientes[id]
        else:
            print(f'No existe cliente con el id: {id}')
    if opcion == '3':
        print('\n Mostrar cliente. \n')
        id = input('Ingrese el id del cliente: ')
        if id in clientes:
            print(f'ID: {id}')
            for key, value in clientes[id].items():
                print(f'{key.title()} : {value}')
        else:
            print(f'No existe cliente con el id: {id}')
    if opcion == '4':
        print('\n Listar todos los clientes. \n')
        for key, value in clientes.items():
            print(key, value["nombre"])
    if opcion == '5':
        print('\n Listar clientes preferentes. \n')
        for key, value in clientes.items():
            if value['preferente']:
                print(key, value["nombre"])
  