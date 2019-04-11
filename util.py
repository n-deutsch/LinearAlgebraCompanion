# copyMatrix() converts a matrix containing tkinter.Entry to a matrix of floats
def copyMatrix(m):
    numRows = len(m)

    # is there at least one row??
    if numRows <= 0:
        return [] # something went wrong

    numColumns = len(m[0])
    matrix = []

    for i in range(numRows):
        r = m[i]
        row = []
        for j in range(0, numColumns):
            val = r[j].get()

            try:
                val = float(val)
            except ValueError:
                val = 0

            row.append(val)
        matrix.append(row)

    return matrix
# end copyMatrix


# returns FALSE if matrix1, matrix2 have different dimensions, or different values
def assertEqual(matrix1, matrix2):
    numRows = len(matrix1)

    # unequal number of rows?
    if numRows != len(matrix2):
        return False

    # empty matrix?
    if numRows <= 0:
        return True

    numColumns = len(matrix1[0])

    # unequal number of columnms?
    if numColumns != len(matrix2[0]):
        return False

    # compare matrix row by row
    for r in range(0,numRows):
        r1 = matrix1[r]
        r2 = matrix2[r]
        for c in range(0,numColumns):
            if r1[c] != r2[c]:
                return False
    return True
# end assertEqual()


# round all values to 3 decimal places, otherwise we get lots of 0.0000000001 values
def roundDecimals(matrix, numDecimalPlaces):
    numRows = len(matrix)

    if numRows > 0:
        numColumns = len(matrix[0])
    else:
        numColumns = 0

    for r in matrix:
        for c in range(0, numColumns):
            r[c] = round(r[c], numDecimalPlaces)

    return matrix
# end roundDecimals()


# returns TRUE if a has the same # of columns and rows as b
def checkEqualDimensions(matrix_a, matrix_b):
    # get A's dimensions
    rows_a = len(matrix_a)
    if rows_a > 0:
        cols_a = len(matrix_a[0])
    else:
        cols_a = 0

    # get B's dimensions
    rows_b = len(matrix_b)
    if rows_b > 0:
        cols_b = len(matrix_b[0])
    else:
        cols_b = 0

    if rows_a != rows_b:
        return False
    if cols_a != cols_b:
        return False

    return True
# end check_equal_dimensions()



