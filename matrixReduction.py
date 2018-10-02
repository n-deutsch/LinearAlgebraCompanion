def reduce(m, numColumns, numRows):
    matrix = copyMatrix(m)

    solution = rowReduce(matrix)

    solution = [
        [1,2],
        [3,4]
    ]

    solution = simplify(solution)

    return solution
#end reduce()

def copyMatrix(m):
    numRows = len(m)

    #is there at least one row??
    if numRows <= 0:
        return [] #something went wrong

    numColumns = len(m[0])
    matrix = []

    for i in range(0, numRows):
        r = m[i]
        row = []
        for j in range(0, numColumns):
            val = r[j].get()
            val = float(val)
            row.append(val)
        matrix.append(row)

    butts = 69

    return matrix
#end copyMatrix

def rowReduce(matrix):
    solution = []
    numRows = len(matrix)

    #don't process if it's empty
    if numRows <= 0:
        return solution

    #every row has the same length because it's a matrix
    numColumns = len(matrix[0])
    numReductions = numColumns - 1

    startRow = 0

    #iterate through every column c except the last one
    for c in range (0, numReductions):
        #find a row with some nonzero entry at index 'c'
        row = matrix[startRow]
        if row[c] == 0:
            #find some row that doesn't have a zero in column 'c'
            for r in range(startRow, numRows):
                tempRow = matrix[r]
                if tempRow[c] != 0:
                    matrix[r] = matrix[startRow]
                    matrix[startRow] = tempRow
                    row = matrix[startRow]

        #is row[c] STILL zero?? ignore this column 'c'
        if row[c] == 0:
            continue

        #now we have a nonzero entry at row[c]
        for i in range(c,numRows):
            #divide every entry by the leading number so it's "1"
            row[i] = row[i] / row[c]

        

        #next column


    return solution
#end rowReduce()

def simplify(matrix):
    return matrix
#end simplify()