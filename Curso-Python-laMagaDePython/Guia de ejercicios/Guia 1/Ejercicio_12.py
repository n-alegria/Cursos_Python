# Ejercicio 12: Crear un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

vector_uno = [1, 2, 3]
vector_dos = [-1, 0, 2]
producto_escalar = 0

for i in range(len(vector_uno)):
    producto = vector_uno[i] * vector_dos[i]
    producto_escalar += producto

print(f"Producto esclar: {producto_escalar}")
