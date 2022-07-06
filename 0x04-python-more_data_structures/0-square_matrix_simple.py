#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square_cells(array):
        result = []
        for c in array:
            result.append(c ** 2)
        return result
    return list(map(square_cells, matrix))
