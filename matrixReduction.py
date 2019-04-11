from util import *


# driver function for matrixReduction()
def reduce(m):
    matrix = copyMatrix(m)
    solution = matrixReduction(matrix)
    return solution
# end reduce()


# returns input matrix in reduced echelon form
def matrixReduction(matrix):
    numRows = len(matrix)

    # don't process if it's empty
    if numRows <= 0:
        return matrix

    # every row has the same length because it's a matrix
    numColumns = len(matrix[0])
    numReductions = numColumns - 1

    submatrixRow = 0

    # iterate through every column c except the last one
    for submatrixColumn in range(0, numReductions):
        # find a row with some nonzero entry at index 'c'
        row = matrix[submatrixRow]

        # ensure row[c] is nonzero
        if row[submatrixColumn] == 0:
            # find some row that doesn't have a zero in column 'c'
            for r in range(submatrixRow, numRows):
                tempRow = matrix[r]
                if tempRow[submatrixColumn] != 0:
                    # swap rows
                    matrix[r] = matrix[submatrixRow]
                    matrix[submatrixRow] = tempRow
                    row = matrix[submatrixRow]
                    break

        # is row[c] STILL zero?? ignore this column 'c'
        if row[submatrixColumn] == 0:
            continue
        # now we have a nonzero entry at row[c]

        # grab the value in column c
        factor = row[submatrixColumn]
        for i in range(submatrixColumn, numColumns):
            # divide every entry by the leading number so r[c] has value of "1"
            row[i] = row[i] / factor

        # leading entry is now one, zero out all rows below this one at "c"
        for i in range(0, numRows):
            # skip the current row
            if i == submatrixRow:
                continue

            # row subtraction and multiplication
            rowSubtraction = matrix[i]
            factor = rowSubtraction[submatrixColumn]
            for j in range(submatrixColumn, numColumns):
                rowSubtraction[j] = rowSubtraction[j] - (factor * row[j])

        # shrink submatrix
        submatrixRow = submatrixRow + 1  # shrink submatrix
        # end master loop!

    # round to three decimal places
    matrix = roundDecimals(matrix, 3)

    return matrix
# end rowReduce()
