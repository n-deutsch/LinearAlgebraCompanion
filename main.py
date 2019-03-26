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
screenWidth = 1200
screenHeight = 580

screen33x = screenWidth/3  # 1/3 of the screen
screen66x = (screenWidth/3) * 2  # 2/3 of the screen

screen25x = screenWidth/4  # 1/4 of the screen
screen50x = screenWidth/2  # 1/2 of the screen
screen75x = (screenWidth/4) * 3  # 3/4 of the screen

screen16x = screenWidth/6  # 16.6% of the screen
screen83x = (screenWidth/6) * 5  # 83.3% of the screen

screen50y = screenHeight/2  # 1/2 of the screen

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

    cleanUI()
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
    master.geometry("1200x580")

    modeLabel = Label(master, text="Mode:")
    modeLabel.place(x=0, y=5, in_=master)

    MODES = ["Reduction", "Multiplication", "Addition", "Subtraction"]
    modeVar = StringVar()
    modeVar.set("Reduction")
    modeSelect = OptionMenu(master, modeVar, *MODES, command=modeSwap)

    modeSelect.place(x=38, y=0, in_=master)

    matrixReductionSetup()
# end UISetup()


def cleanUI():
    for e in UIElements:
        e.destroy()
    clearMatrix(matrixA)
    clearMatrix(matrixB)
    clearMatrix(solutionMatrix)
# end cleanUI()

def buildMatrix(x, y, originX, originY):
    # print("building matrix...")

    m = []

    offsetX = originX - (x / 2 * cellSize)
    offsetY = originY - (y / 2 * cellSize)

    # build matrix...
    for i in range(0, y):
        row = []
        for j in range(0, x):
            c = Entry(master, width=4)
            # calculate offset...
            cellX = offsetX + cellSize * j
            cellY = offsetY + cellSize * i
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

    matrixA = buildMatrix(a_x, a_y, screen25x, screen50y)
    solutionMatrix = buildMatrix(a_x, a_y, screen75x, screen50y)
# end rowResize()


def columnResizeA(y):
    # global keyword lets us change global variables
    global matrixA
    global solutionMatrix
    global a_x

    a_x = int(y)
    clearMatrix(matrixA)
    clearMatrix(solutionMatrix)

    matrixA = buildMatrix(a_x, a_y, screen25x, screen50y)
    solutionMatrix = buildMatrix(a_x, a_y, screen75x, screen50y)
# end columnResize()


def rowResizeB(x):
    # global keyword lets us change global variables
    global matrixB
    global solutionMatrix
    global b_y

    b_y = int(x)
    clearMatrix(matrixB)
    clearMatrix(solutionMatrix)

    matrixA = buildMatrix(b_x, b_y, screen25x, screen50y)
    solutionMatrix = buildMatrix(b_x, b_y, screen75x, screen50y)
# end rowResize()


def columnResizeB(y):
    # global keyword lets us change global variables
    global matrixB
    global solutionMatrix
    global b_x

    b_x = int(y)
    clearMatrix(matrixB)
    clearMatrix(solutionMatrix)

    matrixA = buildMatrix(b_x, b_y, screen25x, screen50y)
    solutionMatrix = buildMatrix(b_x, b_y, screen75x, screen50y)
# end columnResize()


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

    if(numRows <= 0):
        return

    numColumns = len(solution[0])

    for i in range (0, numRows):
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
    # build matrix A, B, and solution matrix.

    rowVar = StringVar()
    rowVar.set("2")
    columnVar = StringVar()
    columnVar.set("2")

    # MATRIX A
    rowSelect_a = OptionMenu(master, rowVar, *DIMENSIONS, command=rowResizeA)
    rowSelect_a.place(x=(screen16x - 60), y=500, in_=master)

    columnSelect_a = OptionMenu(master, columnVar, *DIMENSIONS, command=columnResizeA)
    columnSelect_a.place(x=(screen16x + 5), y=500, in_=master)

    # dimensions 'x' label for matrix a
    xLabel_a = Label(master, text="x")
    xLabel_a.place(x=(screen16x - 5), y=504, in_=master)

    # dimensions label...
    dimensionsLabel_a = Label(master, text="Matrix A Dimensions:")
    dimensionsLabel_a.place(x=(screen16x - 55), y=480, in_=master)

    # MATRIX B
    rowSelect_b = OptionMenu(master, rowVar, *DIMENSIONS, command=rowResizeB)
    rowSelect_b.place(x=(screen50x - 60), y=500, in_=master)

    columnSelect_b = OptionMenu(master, columnVar, *DIMENSIONS, command=columnResizeB)
    columnSelect_b.place(x=(screen50x + 5), y=500, in_=master)

    # dimensions 'x' label for matrix b
    xLabel_b = Label(master, text="x")
    xLabel_b.place(x=screen50x -5, y=504, in_=master)

    # dimensions label...
    dimensionsLabel_b = Label(master, text="Matrix B Dimensions:")
    dimensionsLabel_b.place(x=(screen50x - 55), y=480, in_=master)

    # SOLUTION ELEMENTS
    # solution label...
    solutionLabel = Label(master, text="Solution matrix")
    solutionLabel.place(x=(screen83x - 50), y=480, in_=master)

    # 'multiply' button
    solveButton = Button(master, text="Multiply", command=multiplyMatrix)
    solveButton.place(x=(screen50x + 200), y=502, in_=master)

    # put all these UI elements in a list so they can be removed later...
    global UIElements
    UIElements.append(dimensionsLabel_a)
    UIElements.append(rowSelect_a)
    UIElements.append(columnSelect_a)
    UIElements.append(xLabel_a)
    UIElements.append(dimensionsLabel_b)
    UIElements.append(rowSelect_b)
    UIElements.append(columnSelect_b)
    UIElements.append(xLabel_b)
    UIElements.append(solutionLabel)
    UIElements.append(solveButton)

    # permission to access global variables
    global matrixA
    global matrixB
    global solutionMatrix

    matrixA = buildMatrix(a_x, a_y, screen16x, screen50y)
    matrixB = buildMatrix(b_x, b_y, screen50x, screen50y)
    solutionMatrix = buildMatrix(a_x, a_y, screen83x, screen50y)
# end matrixMultiplicationSetup()


def matrixReductionSetup():
    # print("setting up matrix reduction...")

    rowVar = StringVar()
    rowVar.set("2")
    columnVar = StringVar()
    columnVar.set("2")

    rowSelect = OptionMenu(master, rowVar, *DIMENSIONS, command=rowResizeA)
    rowSelect.place(x=(screen25x - 65), y=500, in_=master)

    columnSelect = OptionMenu(master, columnVar, *DIMENSIONS, command=columnResizeA)
    columnSelect.place(x=(screen25x + 10), y=500, in_=master)

    # dimensions 'x' label
    xLabel = Label(master, text="x")
    xLabel.place(x=(screen25x - 8), y=504, in_=master)

    # dimensions label...
    dimensionsLabel = Label(master, text="Matrix A Dimensions:")
    dimensionsLabel.place(x=(screen25x - 60), y=480, in_=master)

    # solution label...
    solutionLabel = Label(master, text="Solution matrix")
    solutionLabel.place(x=(screen75x - 50), y=480, in_=master)

    # 'Reduce' button
    solveButton = Button(master, text="Reduce", command=reduceMatrix)
    solveButton.place(x=(screen50x - 25), y=502, in_=master)

    # put all these UI elements in a list so they can be removed later...
    global UIElements
    UIElements.append(dimensionsLabel)
    UIElements.append(rowSelect)
    UIElements.append(columnSelect)
    UIElements.append(xLabel)
    UIElements.append(solutionLabel)
    UIElements.append(solveButton)

    # permission to access global variables
    global matrixA
    global solutionMatrix

    matrixA = buildMatrix(a_x, a_y, screen25x, screen50y)
    solutionMatrix = buildMatrix(a_x, a_y, screen75x, screen50y)
    # print("done!")
# end matrixReductionSetup()


def main():
    if testing:
        test()

    setGlobals()
    UISetup()

    # modeSwap("Multiplication")

    mainloop()
# end main()


def test():
    if integrationTest():
        print("All tests OK!")
# end test()


# start program
main()

