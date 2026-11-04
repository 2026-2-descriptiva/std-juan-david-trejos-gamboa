"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import defaultdict

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data = defaultdict()

    with open('./files/input/data.csv', 'r') as file:
        for line in file:
            newLine = line.strip().split('\t')
            firstColumn = newLine[0]
            if firstColumn not in data:
                data[firstColumn] = set()
                data[firstColumn].add(int(newLine[1]))
            else:
                data[firstColumn].add(int(newLine[1]))
    
    answer = []
    for key, value in data.items():
        answer.append(
            (key, max(value), min(value))
        )

    return sorted(answer)

print(pregunta_05())
            
            