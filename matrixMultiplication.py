from util import *

def multiply(matrix_a, matrix_b):
    # ensure matrix_a has the same number of columns as matrix_b has rows
    if not checkDimensions(matrix_a, matrix_b):
        return []


    # TODO: multiply two matricies...

    solution = []
    solution.append([1])
    return solution
# end multiply()

# checkDimensions return TRUE if matrix A has the same number of columns as matrix B has rows
def checkDimensions(matrix_a, matrix_b):
    # get number of columns in matrix a
    rows_a = len(matrix_a)
    if rows_a == 0:
        cols_a = 0
    else:
        cols_a = len(matrix_a[0])

    # get number of rows in matrix b
    rows_b = len(matrix_b)

    if cols_a == rows_b:
        return True
    return False
# end checkDimensions
