class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola soy un',self.tipo,'mi sonido es:',self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Gato con valores agregados.')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("extendiendo funcionalidad de perro con super()")


# Tenemos que instanciar primero para que la propiedad "tipo" exista
gato = Gato('fluffy', 'maullido')
gato.saludo()
perro = Perro('Kira', 'ladrido')
perro.saludo()
