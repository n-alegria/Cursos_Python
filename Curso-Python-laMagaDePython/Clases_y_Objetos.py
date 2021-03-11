# Todo en Python es un OBJETO

'''
    Una CLASE es un modelo o prototipo que define atributos y metodos comunes a todos 
los objetos de cierto grupo, un blueprint.
* Atributo: caracteristicas que tendran los objetos pertenecientes a la clase.
* Metodos: comportamientos que tendran los objetos pertenecientes a la clase.
'''
'''
    Un OBJETO es una entidad que agrupa un estado y una funcionalidad relacionadas.
El estado del objeto se define a traves de los atributos, mientras que la funcionalidad se
modela a traves de los metodos.
Cuando se crea un objeto, se dice que se instancia la clase a la que pertenece, y luego,
para accecer a sus atributos y metodos se utiliza la nomenclatura del punto.
'''

# EJEMPLO:

class Cancion: # En CamelCase

    def __init__(self, letra): # Constructor para indicar propiedades iniciales de la clase
        self.letra = letra # Con Self indico que es un atributo propio de la clase

    def cantar(self):
        for linea in self.letra: # Indico con self. que hago un llamado al atributo de la clase
            print(linea)

# Instancia la clase creando un objeto perteneciente a ella
musica_ligera = Cancion(['\nDe aquel amor, de musica ligera \nNada nos libra, nada mas queda\n'])

# Llamo al metodo perteneciente al objeto
musica_ligera.cantar()

'''
* El constructor __init__ : se ejecuta justo despues de crear un nuevo objeto a partir de la clase, proceso que se conoce con el nombre de instanciacion.
* Parametro self: el primer parametro de __init__ y del resto de metodos de la clase es siempre self, y sirve para referirse al objeto actual.
Este mecanismo es necesario para poder acceder a los atributos y metodos del objeto diferenciado, por ejemplo, una variable local mi_var de un atributo del objeto self.my_var.
* Para crear un objeto se escribe el nombre de la clase seguido de cualquier parametro que sea necesario entre paréntesis, excepto self. Estos parametros son los que se pasaran al metodo __init__.
'''

'''
4 pilares de la programacion orientada a objetos

--> Herencia
En un lenguaje orientado a objetos, cuando hacemos que una clase (subclase) 
herede de otra clase (superclase) estamos diciendo que la subclase contenga 
todos los atributos y metodos que tenia la superclase. 
Esta accion tambien se suele llamar a menudo "extender una clase".

* Python acepta herencia multiple, para esto hay que pasarle en la definicion 
de la clase 'class Derivada()' como parametros las clases de la cual va a heredar.
Siendo el orden de importancia de izquierda a derecha, si hay dos superclases
con atribuos o metodos iguales, se toma el el de la izquierda.
Como maximo 3 clases.

ej: class Derivada(ClassUno, ClassDos)
'''

# EJEMPLO:

class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.respira = True
        
    def descripcion(self):
        print(f'''La persona {self.nombre} {self.apellido} tiene el dni {self.dni}''')

lautaro = Persona('lautaro', 'fernandez', 36761509)
lautaro.descripcion()

class Empleado(Persona): # Indico dentro del parentesis de quien va a heredar
     # Debo declarar en los parametros los datos del padre mas los propios de la clase
    def __init__(self, nombre, apellido, dni, profesion, ocupacion):
        # El metodo super 'super().__init__(parametros)' indica que llamare al constructor del padre
        super().__init__(nombre, apellido, dni)
        # Luego declaro los nuevos parametros
        self.__profesion = profesion
        self.ocupacion = ocupacion
        
    def puesto(self):
        print(f'El empleado {self.nombre} {self.apellido} es {self.__profesion} y ocupa el puesto de {self.ocupacion}')

juan = Empleado('juan', 'perez', 121212, 'contador', 'gerente')
juan.descripcion() # Llama al metodo de la clase padre
juan.puesto() # Llama al metodo de la clase hija

'''
--> Encapsulacion
La encapsulacion se refiere a impedir el acceso a determinados metodos y 
atributos de los objetos estableciendo así que puede utilizarse desde fuera
de la clase.
En Python no existen modificadores de acceso, y lo que se suele hacer es que 
el acceso a una variable o funcion viee determinado por su nombre:
si el nombre comienza con dos guiones bajos (y no termina tambien con dos 
guiones bajos) se trata de una variable o funcion privada, en caso contrario
es publica.

'''
# Da error, no encuentra las variables
# juan.profesion = 'analista'
# juan.__profesion = 'analista'

'''
--> Polimorfismo
El polimorfismo se refiere a la habilidad de objetos de distintas clases de 
responder al mismo mensaje. Esto se puede conseguir a traves de la herencia:
un objeto de una clase derivada es al mismo tiempo un objeto de la clase padre,
de forma que alli donde se requiere un objeto de la clase padre tambien se
puede utilizar uno de la clase hija.
'''

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        
    def desplazarse(self):
        print(f'{self.nombre} se mueve en 4 patas')
        
class Pez:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    def desplazarse(self):
        print(f'{self.nombre} se desplaza nadando')


print()
canela = Perro('canela', 'de la calle')
romulo = Pez('romulo', 'pez espada')

canela.desplazarse()
romulo.desplazarse()

'''
La POO es un paradigma de programacion que busca representar entidades u 
objetos agrupando datos y metodos que puedan describir sus caracteristicas
y comportamientos.
En este paradigma, los conceptos del mundo real relevantes para nuestro problema
a resolver se modelan a traves de clases y objetos, y el programa
consistira en una serie de interacciones entre dichos objetos.
'''




