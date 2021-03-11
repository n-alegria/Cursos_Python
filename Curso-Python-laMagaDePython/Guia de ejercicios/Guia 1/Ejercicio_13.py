'''
Ejercicio 13: Crear un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa 
y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''

diccionario = {
    'Euro' : '€', 
    'Dollar':'$', 
    'Yen':'¥'
}

divisa = input("Ingrese una divisa: ")

if divisa in diccionario: # El for en los diccionarios itera sobre los valores no sobre las claves
    print(f'\n{diccionario[divisa]}')
else:
    print("No esta la divisa en el diccionario")