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

def assertEqual(matrix1, matrix2):
    numRows = len(matrix1)

    #unequal number of rows?
    if numRows != len(matrix2):
        return False

    #empty matrix?
    if numRows <= 0:
        return True

    numColumns = len(matrix1[0])

    #unequal number of columnms?
    if numColumns != len(matrix2[0]):
        return False

    #compare matrix row by row
    for r in range(0,numRows):
        r1 = matrix1[r]
        r2 = matrix2[r]
        for c in range(0,numColumns):
            if r1[c] != r2[c]:
                return False

    return True
#end assertEqual()