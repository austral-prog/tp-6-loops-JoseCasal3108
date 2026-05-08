# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """

    lst = []

    for lista in matrix:
        for indice in lista:
            lst.append(indice)

    return lst


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    
    lst = []

    for fila in matrix:
        contador = 0
        for elemento in fila:
            contador += elemento

        lst.append(contador)

    return lst



def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """


    lst = []
    for fila in range(len(matrix[0])):
        contador = 0

        for i in range(len(matrix)):
            contador = contador + matrix[i][fila]

        lst.append(contador)

    return lst

