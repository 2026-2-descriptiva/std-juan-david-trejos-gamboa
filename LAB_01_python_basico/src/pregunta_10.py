"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    from collections import defaultdict

    data = []

    with open('./files/input/data.csv', 'r') as file:
        
        for line in file:
            newLine = line.strip().split('\t')
            col1_value = newLine[0]
            elements_col4 = len(newLine[-2].split(','))
            elements_col5 = len(newLine[-1].split(','))

            data.append((col1_value, elements_col4, elements_col5))

    return data


print(pregunta_10())