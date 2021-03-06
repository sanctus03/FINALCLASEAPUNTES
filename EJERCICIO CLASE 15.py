#   partiendo del ejercicio 9 al final del modulo principal antes de escribir los datos de la lista de objetos ordenar la lista por el atributo
#   "marca" utilizando el metodo de la burbuja

class Car:
    """class represent and manage cars"""

    num_cars = 0

    def __init__(self, marca, modelo, combustible, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.pos_x = 0
        self.pos_y = 0

    def move_to(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move_incr(self, x, y):
        self.pos_x += x
        self.pos_y += y

    def get_pos(self):
        return self.pos_x, self.pos_y