class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Hi! my name is: ", self.nombre, self.apellido)

#Inheritance:

class Admin(Usuario):
    def superSaludo(self):
        print('Hi! My name is:', self.nombre, 'and Im an admin')

# usuario = Usuario("Jorge", "Nunez")
# usuario.saludo()
admin = Admin('adminJorge', 'adminNunez')
admin.saludo()
admin.superSaludo()
