# Library for GUI
from tkinter import *

# Include other .py files
from test import *
from matrixReduction import *
from matrixMultiplication import *
from matrixAddition import *
from matrixSubtraction import *

# Global Variables
master = Tk()

# variable that decides if we run tests or not
testing = True

# "Dimensions" dropdown values
DIMENSIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# screen resolution variables...
screenWidth = 1000
screenHeight = 500

originA_x = 0
originA_y = 100

originB_x = 350
originB_y = 100

originS_x = 700
originS_y = 100

# List of temporary UI elements
UIElements = []

# Matrix takes the form list of lists
matrixA = []
a_x = 2
a_y = 2
labelA = Label(master, text="")

# Matrix takes the form list of lists
matrixB = []
b_x = 2
b_y = 2
labelB = Label(master, text="")

# Solution set appears here
solutionMatrix = []
s_x = 2
s_y = 2
labelS = Label(master, text="")

rowA = StringVar()
colA = StringVar()

rowB = StringVar()
colB = StringVar()

rowSelectA = OptionMenu(master, rowA, *DIMENSIONS)
colSelectA = OptionMenu(master, colA, *DIMENSIONS)

rowSelectB = OptionMenu(master, rowB, *DIMENSIONS)
colSelectB = OptionMenu(master, colB, *DIMENSIONS)

cellSize = 30

mode = "Reduction"

def setGlobals():
    # set up matrixA
    global matrixA
    matrixA = []
    global a_x
    a_x = 2
    global a_y
    a_y = 2

    # set up matrixB
    global matrixB
    matrixB = []
    global b_x
    b_x = 2
    global b_y
    b_y = 2

    # set up solution matrix
    global solutionMatrix
    solutionMatrix = []
    global s_x
    s_x = 2
    global s_y
    s_y = 2

    global rowA
    rowA.set("2")
    global colA
    colA.set("2")

    global rowB
    rowB.set("2")
    global colB
    colB.set("2")

    global UIElements
    UIElements = []
# end setGlobals

def reset_matricies():
    global a_x
    global a_y
    global b_x
    global b_y
    global s_x
    global s_y
    a_x = a_y = b_x = b_y = s_x = s_y = 2

    rowA.set("2")
    colA.set("2")
    rowB.set("2")
    colB.set("2")

    global matrixA
    global matrixB
    global solutionMatrix

    clearMatrix(matrixA)
    clearMatrix(matrixB)
    clearMatrix(solutionMatrix)

    matrixA = matrixB = solutionMatrix = []
# end set_default_matrix_dimensions()

def modeSwap(x):
    global mode
    mode = x

    # cleanUI()
    reset_matricies()

    if x == "Reduction":
        matrixReductionSetup()
    elif x == "Multiplication":
        matrixMultiplicationSetup()
    elif x == "Addition":
        matrixAdditionSetup()
    elif x == "Subtraction":
        matrixSubtractionSetup()

    # print("mode : ", mode)
# end modeSwap()


def UISetup():
    master.minsize(screenWidth, screenHeight)
    master.geometry("1000x500")

    modeLabel = Label(master, text="Mode:")
    modeLabel.place(x=0, y=5, in_=master)

    MODES = ["Reduction", "Multiplication", "Addition", "Subtraction"]
    modeVar = StringVar()
    modeVar.set("Reduction")
    modeSelect = OptionMenu(master, modeVar, *MODES, command=modeSwap)

    modeSelect.place(x=38, y=0, in_=master)

    aLabel = Label(master, text="Matrix A:")
    aLabel.place(x=-3, y=80, in_=master)

    bLabel = Label(master, text="Matrix B:")
    bLabel.place(x=347, y=80, in_=master)

    sLabel = Label(master, text="Solution Matrix:")
    sLabel.place(x=697, y=80, in_=master)

    solveButton = Button(master, text="Solve", command=solveMatrix)
    solveButton.place(x=700, y=405, in_=master)

    aRowLabel = Label(master, text="A rows: ")
    aRowLabel.place(x=0, y=410)

    aColLabel = Label(master, text="A columns: ")
    aColLabel.place(x=0, y=437)

    global rowSelectA
    rowSelectA = OptionMenu(master, rowA, *DIMENSIONS, command=rowResizeA)
    rowSelectA.place(x=65, y=405, in_=master)

    global colSelectA
    colSelectA = OptionMenu(master, colA, *DIMENSIONS, command=columnResizeA)
    colSelectA.place(x=65, y=433, in_=master)

    bRowLabel = Label(master, text="B rows: ")
    bRowLabel.place(x=347, y=410)

    bColLabel = Label(master, text="B columns: ")
    bColLabel.place(x=347, y=437)

    global rowSelectB
    rowSelectB = OptionMenu(master, rowB, *DIMENSIONS, command=rowResizeB)
    rowSelectB.place(x=412, y=405, in_=master)
    # rowSelectB.config(state=DISABLED)

    global colSelectB
    colSelectB = OptionMenu(master, colB, *DIMENSIONS, command=columnResizeB)
    colSelectB.place(x=412, y=433, in_=master)
    # columnSelectB.config(state=DISABLED)

    matrixReductionSetup()
# end UISetup()


def cleanUI():
    clearMatrix(matrixA)
    clearMatrix(matrixB)
    clearMatrix(solutionMatrix)
# end cleanUI()

def buildMatrix(x, y, originX, originY):
    m = []

    for i in range(0, y):
        row = []
        for j in range(0, x):
            c = Entry(master, width=4)
            # calculate offset...
            cellX = originX + (cellSize * j)
            cellY = originY + (cellSize * i)
            c.place(x=cellX, y=cellY, in_=master)
            c.insert(0, "0")
            row.append(c)
        m.append(row)
    # done building matrix
    return m
# end buildMatrix()


def clearMatrix(matrix):
    # remove all UI elements in matrix
    for row in matrix:
        for cell in row:
            cell.destroy()
    # matrix is now an empty list
    m = []
# end clearMatrix


def rowResizeA(resize):
    # global keyword lets us change global variables
    global matrixA
    global matrixB
    global solutionMatrix

    global a_x
    global b_x
    global a_y
    global b_y

    a_y = int(resize)

    oldMatrixA = copyMatrix(matrixA)
    oldMatrixB = copyMatrix(matrixB)

    if mode == "Reduction":
        clearMatrix(matrixA)
        clearMatrix(solutionMatrix)

        matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
        solutionMatrix = buildMatrix(a_x, a_y, originS_x, originS_y)

        restore(matrixA, oldMatrixA)
    elif mode == "Multiplication":
        clearMatrix(matrixA)
        # clearMatrix(matrixB)
        clearMatrix(solutionMatrix)

        matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
        # matrixB = buildMatrix(b_x, b_y, originB_x, originB_y)
        solutionMatrix = buildMatrix(a_y, b_x, originS_x, originS_y)

        # rowB.set(resize)

        restore(matrixA, oldMatrixA)
        # restore(matrixB, oldMatrixB)
    elif mode == "Addition" or mode == "Subtraction":
        clearMatrix(matrixA)
        clearMatrix(matrixB)
        clearMatrix(solutionMatrix)

        b_y = a_y

        matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
        matrixB = buildMatrix(a_x, a_y, originB_x, originB_y)
        solutionMatrix = buildMatrix(a_x, a_y, originS_x, originS_y)

        rowB.set(resize)

        restore(matrixA, oldMatrixA)
        restore(matrixB, oldMatrixB)
    # clearMatrix(matrixA)
    # clearMatrix(solutionMatrix)

    # matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
    # solutionMatrix = buildMatrix(a_x, a_y, originS_x, originS_y)
# end rowResize()


def columnResizeA(resize):
    # global keyword lets us change global variables
    global matrixA
    global matrixB
    global solutionMatrix

    global a_x
    global b_x
    global a_y
    global b_y

    a_x = int(resize)


    oldMatrixA = copyMatrix(matrixA)
    oldMatrixB = copyMatrix(matrixB)

    if mode == "Reduction":
        clearMatrix(matrixA)
        clearMatrix(solutionMatrix)

        matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
        solutionMatrix = buildMatrix(a_x, a_y, originS_x, originS_y)

        restore(matrixA, oldMatrixA)
    elif mode == "Multiplication":
        clearMatrix(matrixA)
        clearMatrix(matrixB)

        b_y = a_x

        matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
        matrixB = buildMatrix(b_x, b_y, originB_x, originB_y)
        # solutionMatrix = buildMatrix(a_y, b_x, originS_x, originS_y)

        rowB.set(resize)

        restore(matrixA, oldMatrixA)
        restore(matrixB, oldMatrixB)
    elif mode == "Addition" or mode == "Subtraction":
        clearMatrix(matrixA)
        clearMatrix(matrixB)
        clearMatrix(solutionMatrix)

        b_x = a_x

        matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
        matrixB = buildMatrix(a_x, a_y, originB_x, originB_y)
        solutionMatrix = buildMatrix(a_x, a_y, originS_x, originS_y)

        colB.set(resize)

        restore(matrixA, oldMatrixA)
        restore(matrixB, oldMatrixB)


    # clearMatrix(matrixA)
    # clearMatrix(solutionMatrix)

    # matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
    # solutionMatrix = buildMatrix(a_x, a_y, originS_x, originS_y)
# end columnResize()


def rowResizeB(resize):
    # global keyword lets us change global variables
    global matrixA
    global matrixB
    global solutionMatrix

    global a_x
    global b_x
    global a_y
    global b_y

    oldMatrixA = copyMatrix(matrixA)
    oldMatrixB = copyMatrix(matrixB)

    b_y = int(resize)

    # B controls are disabled for matrix reduction
    # if mode == "Reduction":
    #    pass
    if mode == "Multiplication":
        clearMatrix(matrixA)
        clearMatrix(matrixB)

        a_x = b_y

        matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
        matrixB = buildMatrix(b_x, b_y, originB_x, originB_y)
        # solutionMatrix = buildMatrix(a_x, b_y, originS_x, originS_y)

        colA.set(resize)

        restore(matrixA, oldMatrixA)
        restore(matrixB, oldMatrixB)
    elif mode == "Addition" or mode == "Subtraction":
        clearMatrix(matrixA)
        clearMatrix(matrixB)
        clearMatrix(solutionMatrix)

        a_y = b_y

        matrixA = buildMatrix(b_x, b_y, originA_x, originA_y)
        matrixB = buildMatrix(b_x, b_y, originB_x, originB_y)
        solutionMatrix = buildMatrix(b_x, b_y, originS_x, originS_y)

        rowA.set(resize)

        restore(matrixA, oldMatrixA)
        restore(matrixB, oldMatrixB)
    # clearMatrix(matrixB)
    # clearMatrix(solutionMatrix)

    # matrixA = buildMatrix(b_x, b_y, originB_x, originB_y)
    # solutionMatrix = buildMatrix(b_x, b_y, originS_x, originS_y)
# end rowResize()


def columnResizeB(resize):
    # global keyword lets us change global variables
    global matrixA
    global matrixB
    global solutionMatrix

    global a_x
    global b_x
    global a_y
    global b_y

    oldMatrixA = copyMatrix(matrixA)
    oldMatrixB = copyMatrix(matrixB)

    b_x = int(resize)

    # B controls are disabled for matrix reduction
    # if mode == "Reduction":
    #    pass
    if mode == "Multiplication":
        # clearMatrix(matrixA)
        clearMatrix(matrixB)
        clearMatrix(solutionMatrix)

        # matrixA = buildMatrix(a_x, b_x, originA_x, originA_y)
        matrixB = buildMatrix(b_x, b_y, originB_x, originB_y)
        solutionMatrix = buildMatrix(a_y, b_x, originS_x, originS_y)

        # colA.set(resize)

        # restore(matrixA, oldMatrixA)
        restore(matrixB, oldMatrixB)
    elif mode == "Addition" or mode == "Subtraction":
        clearMatrix(matrixA)
        clearMatrix(matrixB)
        clearMatrix(solutionMatrix)

        a_x = b_x

        matrixA = buildMatrix(b_x, b_y, originA_x, originA_y)
        matrixB = buildMatrix(b_x, b_y, originB_x, originB_y)
        solutionMatrix = buildMatrix(b_x, b_y, originS_x, originS_y)

        colA.set(resize)

        restore(matrixA, oldMatrixA)
        restore(matrixB, oldMatrixB)
    # clearMatrix(matrixB)
    # clearMatrix(solutionMatrix)

    # matrixA = buildMatrix(b_x, b_y, originB_x, originB_y)
    # solutionMatrix = buildMatrix(b_x, b_y, originS_x, originS_y)
# end columnResize()


def restore(newMatrix, oldMatrix):
    newRows = len(newMatrix)
    oldRows = len(oldMatrix)

    if newRows > 0:
        newCols = len(newMatrix[0])
    else:
        pass

    if oldRows > 0:
        oldCols = len(oldMatrix[0])
    else:
        oldCols = 0

    for i in range(newRows):
        newRow = newMatrix[i]

        for j in range(newCols):
            if i < oldRows and j < oldCols:
                oldRow = oldMatrix[i]
                oldCell = oldRow[j]
                oldCell = round(oldCell, 0)
                newRow[j].insert(0, oldCell)
# end restore()


def solveMatrix():
    if mode == "Reduction":
        reduceMatrix()
    elif mode == "Multiplication":
        multiplyMatrix()
    elif mode == "Addition":
        addMatrix()
    elif mode == "Subtraction":
        subtractMatrix()
# end solveMatrix()


def reduceMatrix():
    solution = reduce(matrixA)
    displaySolution(solution)
# end reduceMatrix


def multiplyMatrix():
    solution = multiply(matrixA, matrixB)
    displaySolution(solution)
# end multiplyMatrix()


def addMatrix():
    solution = add(matrixA, matrixB)
    displaySolution(solution)
# end addMatrix()


def subtractMatrix():
    solution = subtract(matrixA, matrixB)
    displaySolution(solution)
# end subtractMatrix


def displaySolution(solution):
    numRows = len(solution)
    if numRows <= 0:
        return

    numColumns = len(solution[0])

    for i in range(0, numRows):
        row = solutionMatrix[i]
        r = solution[i]
        for j in range(0, numColumns):
            row[j].delete(0, 100)
            row[j].insert(0, r[j])
# end displaySolution()


def matrixSubtractionSetup():
    # recycles the exact same logic as matrix multiplication
    matrixMultiplicationSetup()
# end matrixSubtractionSetup()


def matrixAdditionSetup():
    # recycles the exact same logic as matrix multiplication
    matrixMultiplicationSetup()
# end matrixAdditionSetup()


def matrixMultiplicationSetup():
    global matrixA
    global matrixB
    global solutionMatrix

    global rowSelectB
    global colSelectB

    rowSelectB.config(state=NORMAL)
    colSelectB.config(state=NORMAL)

    matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
    matrixB = buildMatrix(b_x, b_y, originB_x, originB_y)
    solutionMatrix = buildMatrix(a_x, a_y, originS_x, originS_y)
# end matrixMultiplicationSetup()


def matrixReductionSetup():
    global matrixA
    global matrixB
    global solutionMatrix

    global rowSelectB
    global colSelectB

    rowSelectB.config(state=DISABLED)
    colSelectB.config(state=DISABLED)

    clearMatrix(matrixB)

    matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
    solutionMatrix = buildMatrix(a_x, a_y, originS_x, originS_y)
# end matrixReductionSetup()


def main():
    if testing:
        test()

    setGlobals()
    UISetup()
    mainloop()
# end main()


def test():
    if integrationTest():
        print("All tests OK!")
# end test()


# start program
main()

