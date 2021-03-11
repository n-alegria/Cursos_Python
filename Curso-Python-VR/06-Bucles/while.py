"""
# WHILE -> estructura de control que itera o repite la ejecucion de una 
           serie de instrucciones tantas veces como sea necesario,
           hasta que deje de cumplirse la condicion.

while 'condicion':
    bloque de instrucciones
    actualizacion de contador
"""

contador = 1
while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)