# Ejercicio 9: Crear un programa que pregunte al usuario 5 números enteros y devuelva una lista con ellos.

contador = 0
lista_numerica = []
while contador < 5:
    numero = int(input("Ingrese un numero: "))
    lista_numerica.append(numero)
    contador += 1

print(f'\n{lista_numerica}')
