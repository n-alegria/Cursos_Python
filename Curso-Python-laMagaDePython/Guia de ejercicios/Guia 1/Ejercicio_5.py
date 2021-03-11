# Ejercicio 5: Crear un programa que pida al usuario ingresar 2 números por teclado y devuelva por pantalla 
# la suma de ellos en un renglón, la resta en otro, el producto en otros y la división en otro.

numero_uno = int(input("Ingrese el primer numero: "))
numero_dos = int(input("Ingrese el segundo numero: "))

print(f"\nSuma: {numero_uno + numero_dos}")
print(f"Resta: {numero_uno - numero_dos}")
print(f"Multiplicacion: {numero_uno * numero_dos}")
print(f"Division: {numero_uno / numero_dos}")