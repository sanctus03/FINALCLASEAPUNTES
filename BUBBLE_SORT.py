def bubbleSort (array):
    length = len(array) -1

    #bucle para las pasadas
    for i in range (0, length):
        #bucle para las comparaciones e intercambios
        for j in range (0, length):
            if array [j] > array [j + 1]:
                aux = array [j]
                array [j] = array [j + 1]
                array [j + 1] = aux
    return array
scores = [70, 90, 0, 80, 60, 85]

print("Antes de ordenar: ")
print(scores)
print("Despues de ordenar: ")
print(bubbleSort(scores))
bubbleSort(scores)