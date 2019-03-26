from util import *

# returns the sum of two matricies
def add(matrix_a, matrix_b):
    if not check_equal_dimensions(matrix_a, matrix_b):
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
#end add()