"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    from collections import defaultdict

    data = defaultdict(int)

    with open('./files/input/data.csv', 'r') as file:
        
        for line in file:
            newLine = line.strip().split('\t')
            letter = newLine[0]
            elements_col5 = newLine[-1].split(',')
            numbers = [int(element.split(':')[-1]) for element in elements_col5]
            total_numbers = sum(numbers)

            data[letter] += total_numbers
    
    return dict(sorted(data.items()))


print(pregunta_12())