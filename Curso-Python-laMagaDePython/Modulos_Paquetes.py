# -*- coding: utf-8 -*-
'''
Un modulo es un tipo de archivo .py o .pyc que contiene funciones, clases,
objetos, variables e incluso otros modulos para ser utilizados en otros
archivos de Python.
Se utiliza para que el codigo sea mas ordenado, limpio, legible y 
utilizable.
Para poder usar el contenido de un modulo es necesario importarlo en
el archivo en el queharemos uso del mismo.
'''
# Siempre se importan los modulo y paquetes al inicio

import math
import math as mt
from math import sqrt
from math import *

'''
Un paquete es un directorio o carpeta donde se almacenan diferentes modulos
que estan relacionados entre si.
Se crean con una carpeta que tenga si o si un archivo (file) llamado
__init__.py. Dentro de un paquete puede haber otros paquetes, es importante 
que cada paquete interno tenga su propio archivo __init__.py.
 
# Formas de importar

from paquete import funciones_mate
from paquete import *
from paquete.funciones_math import sumar, restar
from paquete.funciones_mate import *
from paquete import funciones_mate as fm
'''