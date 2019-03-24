from util import *

def multiply(matrix_a, matrix_b):
    # ensure matrix_a has the same number of columns as matrix_b has rows
    if not check_dimensions(matrix_a, matrix_b):
        return []

    solution = []
    solution_row = []

    row_a = []
    row_b = []
    col_b = []

    num_rows_a = len(matrix_a)
    num_rows_b = len(matrix_b)
    num_cols_b = len(matrix_b[0])

    # master loop - iterate through each row of A
    for row_index_a in range(num_rows_a):
        row_a = matrix_a[row_index_a]
        solution_row = []
        # multiply row_a by each COLUMN in matrix b
        for col_index_b in range(num_cols_b):
            col_b = []
            for row_index_b in range(num_rows_b):
                row_b = matrix_b[row_index_b]
                b_factor = row_b[col_index_b]
                col_b.append(b_factor)
            # multiply selected row by the col_b we just assembled
            product = multiply_vectors(row_a, col_b)
            solution_row.append(product)
        solution.append(solution_row)
        # end master loop
    return solution
# end multiply()

# checkDimensions return TRUE if matrix A has the same number of columns as matrix B has rows
def check_dimensions(matrix_a, matrix_b):
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

# multiply_vectors exists to
def multiply_vectors(row_a, col_b):
    # rows should be the same length
    if len(row_a) != len(col_b):
        raise ValueError('Vector lengths are unequal')

    vector_len = len(row_a)

    output = 0
    for index in range(vector_len):
        output = output + row_a[index] * col_b[index]

    return output
# end multiply_vectors



