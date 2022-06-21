import json


Lista = []
while True:
    marca = input("marca del vehiculo: ")
    if marca == "fin":
        break
    modelo = input("modelo del vehiculo: ")

    Diccionario = {}
    Diccionario["marca: "] = marca
    Diccionario["modelo: "] = modelo
    Lista. append(Diccionario)
print("Listado: \n ", Lista)

json.dump(json.dumps(Lista), open("Lista.txt", "w"))