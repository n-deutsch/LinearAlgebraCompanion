from util import *


# driver function for matrixSubtraction()
def subtract(m_a, m_b):
    matrix_a = copyMatrix(m_a)
    matrix_b = copyMatrix(m_b)

    solution = matrixSubtraction(matrix_a, matrix_b)
    return solution
# end subtract()


# returns the difference between two matrices
def matrixSubtraction(matrix_a, matrix_b):
    if not checkEqualDimensions(matrix_a, matrix_b):
        return []

    solution = []

    for i in range(len(matrix_a)):
        row_a = matrix_a[i]
        row_b = matrix_b[i]

        solution_row = []
        for j in range(len(row_a)):
            difference = row_a[j] - row_b[j]
            solution_row.append(difference)
        solution.append(solution_row)

    return solution
# end matrixSubtraction()


