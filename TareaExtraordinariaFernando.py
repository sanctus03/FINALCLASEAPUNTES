# Import librería json para trabajar con ficheros
import json
import os

# Definición de la clase Automóvil
class Automovil:

    # Constructor
    # Objeto self -> siempre se indica para poder guardar los datos en objeto que estamos creando
    def __init__(self, marca, modelo, combustible, potencia, traccion, cambio):

        # Asignar a cada atributo de la clase Automóvil el parámetro correspondiente
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.potencia = potencia
        self.traccion = traccion
        self.cambio = cambio

    # Método str para imprimir los datos del objeto Automovil
    def __str__(self):

        # Variable a la que iremos contatenando los datos del automóvil
        datos = ""

        # Concateno los datos del Automóvil.
        # += es lo mismo que = datos +.
        # \n = enter
        datos += "Marca: " + self.marca + "\n"
        datos += "Modelo: " + self.modelo + "\n"
        datos += "Combustible: " + self.combustible + "\n"
        datos += "Potencia: " + self.potencia + "\n"
        datos += "Tracción: " + self.traccion + "\n"
        datos += "Cambio: " + self.cambio + "\n"

        # Devolver la cadena de texto con los datos del automovil
        return datos


# Definición de la clase que gestiona la aplicación
class Aplicacion:

    # Constructor
    def __init__(self):

        # Cuando iniciamos la aplicación, creamos una lista de automóviles vacía
        self.dicAuto = {}

    # Función que muestra el menú de opciones y devuelve la opción seleccionada por el usuario
    def menu(self):

        # Mostramos las opciones disponibles
        print("1. Nuevo automóvil. ")
        print("2. Buscar por marca y modelo")
        print("3. Listado de automóviles ordenados por marca")
        print("4. Salir")

        # Pedir la opción seleccionada
        opcion = int(input("Introduzca la opción seleccionada: "))

        # Devolver la opción
        return opcion

    # Función que guarda los datos de una lista de automoviles en un fichero de texto
    def guardarDatos(self):

        # Abrimos el fichero automovil.json en modo escritura
        # Si el fichero no existe, crea uno nuevo
        # Si el fichero existe, se sobreescribe
        # w de write
        fichero = open("automovil.json", "w")

        # Utilizamos la función json.dump() para volcar todo el diccionario en un objeto json
        # Le pasamos el diccionario a convertir a json como primer parámetro
        # Le pasamos a la función lambda (función predefinida para convertir tipos)
        # El objeto deque tipo es para que se sepa de qué tipo tiene que convertirlo
        json_object = json.dumps(self.dicAuto, default=lambda obj: obj.__dict__)

        # Escribimos el objeto json en el fichero
        fichero.write(json_object)

    # Función que lee los datos del fichero de texto y los guarda en un diccionario de automoviles
    def leerDatos(self):

        # Abrimos el fichero automovil.json en modo lectura
        # El fichero debe existir previamente
        # r de read
        if (os.path.exists("automovil.json")):

            # El fichero debe existir previamente
            fichero = open("automovil.json", "r")

            # Comprobar que el fichero no está vacío
            if (os.path.getsize("automovil.json") > 0):

                # Guardamos el contenido del fichero en un diccionario mendiante la funcion json.load
                self.dicAuto = json.load(fichero)

        else:

            # Crear un fichero vacio
            fichero = open("automovil.json", "w")

    # OPCIÓN 1
    # Función que añade un nuevo automóvil al diccionario
    def nuevoAutomovil(self):

        # Pedir los datos del nuevo automóvil por teclado
        marca = input("Introduzca marca: ")
        modelo = input("Introduzca modelo: ")
        combustible = input("Introduzca combustible (Gasolina, Diésel, Eléctrico): ")
        potencia = input("Introduzca potencia: ")
        traccion = input("Introduzca tracción: ")
        cambio = input("Introduzca cambio (Automático, Manual): ")

        # Crear un objeto Automóvil y le pasamos todos los valores anteriores
        auto = Automovil(marca, modelo, combustible, potencia, traccion, cambio)

        # Creamos la clave del diccionario con la marca y el modelo concatenado
        clave = auto.marca + "-" + auto.modelo

        # Añadir el automóvil al diccionario
        self.dicAuto[clave] = {"marca": auto.marca,
                               "modelo": auto.modelo,
                               "combustible": auto.combustible,
                               "potencia": auto.potencia,
                               "traccion": auto.traccion,
                               "cambio": auto.cambio}

    # OPCION 2
    # Funcion que busca por marca y modelo
    def buscarMarcaModelo(self):

        # Pedir la marca y el modelo para buscar el automovil
        marca = input("Introduzca marca: ")
        modelo = input("Introduzca modelo: ")

        print("-----------------------------")

        # Bucle que recorre el diccionario principal
        for clave, valores in self.dicAuto.items():

            # Si dentro del diccionario de valores la clave marca y la clave modelo son iguales
            # a las que nos ha indicado el usuario
            if valores["marca"] == marca and valores["modelo"] == modelo:

                # Mostramos los datos
                print("Marca: ", valores["marca"])
                print("Modelo: ", valores["modelo"])
                print("Combustible: ", valores["combustible"])
                print("Potencia: ", valores["potencia"])
                print("Traccion: ", valores["traccion"])
                print("Cambio: ", valores["cambio"])
                print("-----------------------------")

    # OPCIÓN 3
    # Función que muestra el listado de automoviles ordenados por marca
    def mostrarListadoMarca(self):

        print("-----------------------------")

        # Bucle para cada clave y valor en un diccionario ordenado
        for clave, valores in sorted(self.dicAuto.items()):

            # Imprimir cada posicion de la lista
            print("Marca: ", valores["marca"])
            print("Modelo: ", valores["modelo"])
            print("Combustible: ", valores["combustible"])
            print("Potencia: ", valores["potencia"])
            print("Traccion: ", valores["traccion"])
            print("Cambio: ", valores["cambio"])
            print("-----------------------------")

    # Función de ejecución de la aplicación
    def ejecucion(self):

        # Leer los datos del fichero de automoviles
        self.leerDatos()

        # Creamos la variable opción y le asignamos un valor por defecto inicial
        opcion = 0

        # Bucle que ejecuta el menú mientras que la opción sea distinta de 4
        while opcion != 4:
            opcion = self.menu()

            # Dependiendo de la opción seleccionada por el usuario ejecute la opción correspondiente
            if opcion == 1:
                print("NUEVO AUTOMOVIL")
                self.nuevoAutomovil()
            elif opcion == 2:
                print("BUSQUEDA POR MARCA Y MODELO")
                self.buscarMarcaModelo()
            elif opcion == 3:
                print("LISTADO POR MARCA")
                self.mostrarListadoMarca()
            elif opcion == 4:
                print("SALIR")
                self.guardarDatos()
            else:
                print("Opción incorrecta")

# PROGRAMA PRINCIPAL
app = Aplicacion()
app.ejecucion()
