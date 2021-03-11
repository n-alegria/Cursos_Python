# -*- coding: utf-8 -*-
'''
Un archivo es una secuencia de datos almacenados en un medio persistente que estan disponibles para ser utilizados por un programa.
Todos los archivos tienen un nombre y una ubicacion dentro del sistema de archivos del sistema operativo.
Un programa no puede manipular los datos de un archivo directamente.
Para hacerlo, debe abrir el archivo y asignarlo a una variable, que llamaremos el archivo logico.

--> Proceso:
* Se debera importar la libreria io
creacion - apertura - manipulacion - cierre

Si el archivo no esta previemete creado, se crea al abrirse, esto quiere decir que el proceso 'creacion y apertura'
pueden ser una sola etapa.
Cuando el archivo se crea y se abre, se debe especificar para que se abre:
lectura, escritura, agregar contenido al final, lectura + escritura

mi archivo = open("archivo", "r")  {debe existir}
mi archivo = open("archivo", "w")  {si no existe, se crea con la apertura}
mi archivo = open("archivo", "a")  {si no existe, se crea con la apertura}
mi archivo = open("archivo", "r+") {si el archivo no esta creado, da error}

--> Modo de abir un archivo
-> Por el tipo de archivo:
*  't' se trata de un archivo de texto.
*  'b' permite escritura en modo binario.
*  'U' define saltos de linea universales para el modo de lectura.

-> Por el tipo de acceso
*  'r' es modo lectura.
*  'w' es modo escritura. En caso de existir el archivo, este sera sobreescrito.
*  'a' es un modo de escritura. En caso de existir el archivo, comienza a escribir al final del mismo.
*  'x' es un modo de escritura para crear un nuevo archivo. En caso de que el archivo exista se emitira un error tipo 'FilesExistsError'.
*  'r+' es un modo de escritura/lectura, tambien puede ser 'w+'.

---> Siempre que se abra un archivo hay que cerrarlo.
archivo.close()
'''

'''
--> Crear un archivo
Hay dos formas de crar un archivo, la 'tradicional' como se uso anteriormente y la profesional con la clausula 'with'

with open("archivo.txt", "w+") as mi_archivo:
    mi_archivo.write("Hola mundo")
    mi_archivo.read()
    mi_archivo.close()

Si el archivo ya esta creado, con open() solo se lo agrega a la variable logica pasandole la ruta de acceso
en nuestra computadora como paraetro y desde alli se lo manipula.

with open(r"C:\User\Desktop\archivo.txt", "w+") as mi_archivo:
    mi_archivo.write("Agregando contenido..)
    mi_arhcivo.close()
'''

'''
--> Metodos de manipulacion
*  .write() -> escribe desde la primera linea del archivo, si este ya tiene contenido, lo que se pase como parametro lo sobreescribe.
Importante, si el archivo se abre en 'a', cuando se utiliza el metodo write() este agrega contenido al final del archivo y agrega 
ese contenido tantas veces como se inicie el programa.

*  .read() -> lee el contenido del archivo, pero no lo imprime, para poder iprimirlo hay que almacenarlo en una variable e imprimirla.

*  .seek() -> ubica el cursor en el indice que se le pase por parametro.

*  .readlines() -> convierte el contenido del archivo en una lista, el separador de cada elemento es el salto de linea, entonces cada elemento es una linea del archivo.

*  .readline() -> lee la primera linea del archivo y como limite os caracteres que se pasen por parametro.

*  .writelines() -> escribe el archivo hasta el final y agrega el contenido del parametro.

*  .writable() -> devuelve True si el archivo esta abierto en modo escritura.

*  .readable() -> devuelve True si el archivo esta abierto en modo lectura.

*  .seekable() -> devuelve True si es posible desplazarse dentro del archivo.

*  .tell() -> devuelve la posicion en la que se encuentra el puntero dentro del archivo.

*  .close() -> cierra el archivo.
'''

