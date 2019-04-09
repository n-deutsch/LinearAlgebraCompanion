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

    global matrixA
    global matrixB
    global solutionMatrix

    matrixA = matrixB = solutionMatrix = []
# end set_default_matrix_dimensions()

def modeSwap(x):
    global mode
    mode = x

    # cleanUI()
    # reset_matricies()

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
    # print("building matrix...")
    m = []

    # build matrix...
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


def clearMatrix(m):
    # remove all UI elements in matrix
    for r in m:
        for c in r:
            c.destroy()
    # matrix is now an empty list
    m = []
# end clearMatrix


def rowResizeA(x):
    # global keyword lets us change global variables
    global matrixA
    global solutionMatrix
    global a_y

    a_y = int(x)
    clearMatrix(matrixA)
    clearMatrix(solutionMatrix)

    matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
    solutionMatrix = buildMatrix(a_x, a_y, originS_x, originS_y)
# end rowResize()


def columnResizeA(y):
    # global keyword lets us change global variables
    global matrixA
    global solutionMatrix
    global a_x

    a_x = int(y)
    clearMatrix(matrixA)
    clearMatrix(solutionMatrix)

    matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)
    solutionMatrix = buildMatrix(a_x, a_y, originS_x, originS_y)
# end columnResize()


def rowResizeB(x):
    # global keyword lets us change global variables
    global matrixB
    global solutionMatrix
    global b_y

    b_y = int(x)
    clearMatrix(matrixB)
    clearMatrix(solutionMatrix)

    matrixA = buildMatrix(b_x, b_y, originB_x, originB_y)
    solutionMatrix = buildMatrix(b_x, b_y, originS_x, originS_y)
# end rowResize()


def columnResizeB(y):
    # global keyword lets us change global variables
    global matrixB
    global solutionMatrix
    global b_x

    b_x = int(y)
    clearMatrix(matrixB)
    clearMatrix(solutionMatrix)

    matrixA = buildMatrix(b_x, b_y, originB_x, originB_y)
    solutionMatrix = buildMatrix(b_x, b_y, originS_x, originS_y)
# end columnResize()


def solveMatrix():
    if mode == "Reduction":
        reduceMatrix()
    elif mode == "Multiplication":
        multiplyMatrix()
    elif mode == "Addition":
        pass
    elif mode == "Subtraction":
        pass
# end solveMatrix()


def reduceMatrix():
    solution = reduce(matrixA)
    displaySolution(solution)
# end reduceMatrix


def multiplyMatrix():
    solution = multiply(matrixA, matrixB)
    displaySolution(solution)
# end multiplyMatrix()


def displaySolution(solution):
    numRows = len(solution)

    if (numRows <= 0):
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
    pass
# end matrixSubtractionSetup()


def matrixAdditionSetup():
    pass
# end matrixAdditionSetup()


def matrixMultiplicationSetup():
    pass
# end matrixMultiplicationSetup()


def matrixReductionSetup():
    # print("setting up matrix reduction...")
    global matrixA
    global matrixB
    global solutionMatrix
    # matrixA = buildMatrix(a_x, a_y, originA_x, originA_y)

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

