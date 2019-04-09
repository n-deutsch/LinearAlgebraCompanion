from util import *


def add(m_a, m_b):
    matrix_a = copyMatrix(m_a)
    matrix_b = copyMatrix(m_b)

    solution = matrixAddition(matrix_a, matrix_b)
    return solution
# end add()


# returns the sum of two matricies
def matrixAddition(matrix_a, matrix_b):
    if not checkEqualDimensions(matrix_a, matrix_b):
        return []

    solution = []

    for i in range(len(matrix_a)):
        row_a = matrix_a[i]
        row_b = matrix_b[i]

        solution_row = []
        for j in range(len(row_a)):
            # named 's_sum' since 'sum' is reserved
            s_sum = row_a[j] + row_b[j]
            solution_row.append(s_sum)
        solution.append(solution_row)

    return solution
#end matrixAddition()