# Ejercicio 7: Crear un programa que calcule el sueldo bruto de una persona que trabaja 
# de lunes a viernes 8 hs y su pago por hora es de 400 pesos. Devolver el sueldo por pantalla.

dias_trabajados = 5
horas_dia = 8
precio_hora = 400
semanas = 4

sueldo = dias_trabajados * horas_dia * precio_hora * semanas

print(f"Sueldo bruto: ${sueldo}")