#Library for GUI
from tkinter import *

#Global Variables
master = Tk()

#variable that decides if we run tests or not. 0 means testing is enabled
testing = 0

#list of temporary UI elemetns
UIElements = []

#matrix takes the form list of lists
matrixA = []
a_x = 2
a_y = 2
labelA = Label(master, text="")

#matrix takes the form list of lists
matrixB = []
b_x = 2
b_y = 2
labelB = Label(master, text="")

#solution set appears here
solutionMatrix = []
s_x = 2
s_y = 2
labelS = Label(master, text="")

cellSize = 35

#include other .py files
from matrixReduction import *
from matrixMultiplication import *
from matrixAddition import *
from matrixSubtraction import *

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

    global cellSize
    cellSize = 35

    global UIElements
    UIElements = []
# end setGlobals

def modeSwap(x):
    if(x == "Reduction"):
        matrixReductionSetup()
    elif(x == "Multiplication"):
        matrixMultiplicationSetup()
    elif(x == "Addition"):
        matrixAdditionSetup()
    elif(x == "Subtraction"):
        matrixSubtractionSetup()
#end modeSwap()

def UISetup():
    master.minsize(1280, 720)
    master.geometry("1280x720")

    modeLabel = Label(master, text="Mode:")
    modeLabel.place(x=0, y=5, in_=master)

    MODES = ["Reduction","Multiplication","Addition","Subtraction"]
    modeVar = StringVar()
    modeVar.set("Reduction")
    modeSelect = OptionMenu(master, modeVar, *MODES, command=modeSwap)

    modeSelect.place(x=38, y=0, in_=master)

    matrixReductionSetup()
#end UISetup()

def cleanUI():
    for e in UIElements:
        e.destroy()
    clearMatrixA()
    clearSolutionMatrix()
#end cleanUI()

def matrixReductionSetup():
    #print("setting up matrix reduction...")

    #dimensions label...
    dimensionsLabel = Label(master, text="Matrix A Dimensions:")
    dimensionsLabel.place(x=365, y=0, in_=master)

    #dimensions dropdown
    DIMENSIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    rowVar = StringVar()
    rowVar.set("2")
    columnVar = StringVar()
    columnVar.set("2")
    rowSelect = OptionMenu(master, rowVar, *DIMENSIONS, command=rowResizeA)
    rowSelect.place(x=357, y=20, in_=master)
    columnSelect = OptionMenu(master, columnVar, *DIMENSIONS, command=columnResizeA)
    columnSelect.place(x=437, y=20, in_=master)

    #dimensions 'x' label
    xLabel = Label(master, text="x")
    xLabel.place(x=417, y=25, in_=master)

    #'calculate' button
    solveButton = Button(master, text="Reduce", command=reduceMatrix)
    solveButton.place(x=625, y=690, in_=master)

    #put all these UI elements in a list so they can be removed later...
    global UIElements
    UIElements.append(dimensionsLabel)
    UIElements.append(rowSelect)
    UIElements.append(columnSelect)
    UIElements.append(xLabel)
    UIElements.append(solveButton)

    buildMatrixA(a_x, a_y)
    buildSolutionMatrix(a_x, a_y)

    #print("done!")
#end matrixReductionSetup()

def buildMatrixA(x, y):
    #print("building matrix A...")
    # starting coordinates of matrixA
    startX = 427
    startY = 360

    offsetX = startX - (x / 2 * cellSize)
    offsetY = startY - (y / 2 * cellSize)

    row = []
    # build matrixA...
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
        matrixA.append(row)
    # done building matrixA

    # label signifying input matrix'
    global labelA
    labelA = Label(master, text="Matrix A")
    labelAvertical = 320 - (a_y / 2) * cellSize
    labelA.place(x=395, y=labelAvertical, in_=master)
#end buildMatrixA()

def buildSolutionMatrix(x, y):
    print("building solution matrix...")
    # starting coordinates of solution matrix
    solutionStartX = 853
    solutionStartY = 360

    offsetX = solutionStartX - (x / 2 * cellSize)
    offsetY = solutionStartY - (y / 2 * cellSize)

    row = []
    # build solution matrix...
    for i in range(0, y):
        row = []
        for j in range(0, x):
            c = Entry(master, width=4)
            # calculate offset...
            cellX = offsetX + cellSize * j
            cellY = offsetY + cellSize * i
            c.place(x=cellX, y=cellY, in_=master)
            c.insert(0, "-")
            row.append(c)
        solutionMatrix.append(row)
    # done building solution matrix

    global labelS
    labelS = Label(master, text="Solution Matrix")
    labelSvertical = 320 - (a_y / 2) * cellSize
    labelS.place(x=803, y=labelSvertical, in_=master)
#end buildSolutionMatrix

def clearMatrixA():
    #permission to change matrixA
    global matrixA
    for r in matrixA:
        for c in r:
            c.destroy()

    # destroy "solution matrix" label
    labelA.destroy()
    matrixA = []
#end clearMatrixA()

def clearSolutionMatrix():
    #permission to change solutionMatrix
    global solutionMatrix
    # permission to change matrixA
    for r in solutionMatrix:
        for c in r:
            c.destroy()

    #destroy "solution matrix" label
    labelS.destroy()
    solutionMatrix = []
#end clearMatrixA()

def rowResizeA(x):
    #print("row resize A")

    #global keyword lets us change a_x
    global a_y
    a_y = int(x)
    clearMatrixA()
    clearSolutionMatrix()
    buildMatrixA(a_x, a_y)
    buildSolutionMatrix(a_x, a_y)
#end rowResize()

def columnResizeA(y):
    #print("column resize A")

    #global keyword lets us change a_y
    global a_x
    a_x = int(y)
    clearMatrixA()
    clearSolutionMatrix()
    buildMatrixA(a_x, a_y)
    buildSolutionMatrix(a_x, a_y)
#end columnResize()

def reduceMatrix():
    #print("REDUCE MATRIX!!!!")
    #solve matrixA
    solution = reduce(matrixA)
    #display solution matrix
    displaySolution(solution)
#end reduceMatrix

def displaySolution(solution):
    numRows = len(solution)

    if(numRows <= 0):
        return

    numColumns = len(solution[0])

    for i in range (0,numRows):
        row = solutionMatrix[i]
        r = solution[i]
        for j in range(0,numColumns):
            row[j].delete(0,100)
            row[j].insert(0,r[j])
#end displaySolution()

def matrixSubtractionSetup():
    #print("setting up matrix subtraction...")
    #print("done!")
    pass
#end matrixReductionSetup()

def matrixMultiplicationSetup():
    #print("setting up matrix multiplication...")
    #print("done!")
    pass
#end matrixReductionSetup()

def matrixAdditionSetup():
    #print("setting up matrix addition...")
    #print("done!")
    pass
#end matrixReductionSetup()

def main():
    if (testing == 0):
        test()

    setGlobals()
    UISetup()
    mainloop()
#end main()

def test():
    testMatrixReduction()
    testMatrixSubtraction()
    testMatrixMultiplication()
    testMatrixAddition()
#end test()

#start program
main()