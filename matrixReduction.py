from util import *

def reduce(m):
    matrix = copyMatrix(m)
    solution = rowReduce(matrix)
    return solution
#end reduce()

#converts a matrix to echelon form
def rowReduce(matrix):
    numRows = len(matrix)

    #don't process if it's empty
    if numRows <= 0:
        return matrix

    #every row has the same length because it's a matrix
    numColumns = len(matrix[0])
    numReductions = numColumns - 1

    startRow = 0

    #iterate through every column c except the last one
    for c in range (0, numReductions):
        #find a row with some nonzero entry at index 'c'
        row = matrix[startRow]

        #ensure row[c] is nonzero
        if row[c] == 0:
            #find some row that doesn't have a zero in column 'c'
            for r in range(startRow, numRows):
                tempRow = matrix[r]
                if tempRow[c] != 0:
                    matrix[r] = matrix[startRow]
                    matrix[startRow] = tempRow
                    row = matrix[startRow]
                    break

        #is row[c] STILL zero?? ignore this column 'c'
        if row[c] == 0:
            continue
        #now we have a nonzero entry at row[c]

        #grab the value in column c
        factor = row[c]
        for i in range(c,numColumns):
            #divide every entry by the leading number so r[c] has value of "1"
            row[i] = row[i] / factor

        #leading entry is now one, zero out all rows below this one at "c"
        for i in range(0, numRows):
            #skip the current row
            if i == startRow:
                continue

            rowSubtraction = matrix[i]
            factor = rowSubtraction[c]
            for j in range(c,numColumns):
                rowSubtraction[j] = rowSubtraction[j] - (factor * row[j])
        startRow = startRow + 1 #shrink submatrix!
        #master loop!

    #round all values to 3 decimal places, otherwise we get lots of 0.0000000001 values
    for r in range(0, numRows):
        row = matrix[r]
        for j in range(0, numColumns):
            row[j] = round(row[j],3)

    return matrix
#end rowReduce()

def testMatrixReduction():
    print("testing matrix reduction...")

    test1 = [
        [0,3,-6,6,4,-5],
        [3,-7,8,-5,8,9],
        [3,-9,12,-9,6,15]
    ]

    solution1 = [
        [1,0,-2,3,0,-24],
        [0,1,-2,2,0,-7],
        [0,0,0,0,1,4]
    ]

    test2 = [
        [1,2,1,1,7],
        [1,2,2,-1,12],
        [2,4,0,6,4]
    ]

    solution2 = [
        [1,2,0,3,2],
        [0,0,1,-2,5],
        [0,0,0,0,0]
    ]

    test1 = rowReduce(test1)
    output = assertEqual(test1, solution1)

    if output == False:
        print("test1 failed!")
        return False

    test2 = rowReduce(test2)
    output = assertEqual(test2, solution2)

    if output == False:
        print("test2 failed!")
        return False

    #print("Matrix reduction OK!")
    return True
#end testMatrixReduction