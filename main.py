#Library for GUI
from tkinter import *

#Global Variables
master = Tk()

#matrix takes the form list of lists
matrixA = []
a_x = 0
a_y = 0

#matrix takes the form list of lists
matrixB = []
b_x = 0
b_y = 0

#solution set appears here
solutionMatrix = []
s_x = 0
s_y = 0

cellSize = 35

#include other .py files
from matrixReduction import *
from matrixMultiplication import *
from matrixAddition import *
from matrixSubtraction import *


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

def matrixReductionSetup():
    print("setting up matrix reduction...")

    #dimensions label...
    dimensionsLabel = Label(master, text="Dimensions:")
    dimensionsLabel.place(x=395, y=0, in_=master)

    #dimensions dropdown
    DIMENSIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    rowVar = StringVar()
    rowVar.set("2")
    columnVar = StringVar()
    columnVar.set("2")
    modeSelect = OptionMenu(master, rowVar, *DIMENSIONS, command=rowResizeA)
    modeSelect.place(x=367, y=20, in_=master)
    modeSelect = OptionMenu(master, columnVar, *DIMENSIONS, command=columnResizeA)
    modeSelect.place(x=447, y=20, in_=master)

    #dimensions 'x' label
    dimensionsLabel = Label(master, text="x")
    dimensionsLabel.place(x=429, y=25, in_=master)

    #'calculate' button
    solveButton = Button(master, text="Reduce", command=reduceMatrix)
    solveButton.place(x=625, y=690, in_=master)

    #double for loop setup
    i = 0
    j = 0

    #matrixA is 2x2 by default
    a_x = 2
    a_y = 2

    buildMatrixA(a_x, a_y)
    buildSolutionMatrix(a_x, a_y)

    print("done!")
#end matrixReductionSetup()

def buildMatrixA(x, y):
    print("building matrix A...")
    # starting coordinates of matrixA
    startX = 427
    startY = 360

    offsetX = startX - (x / 2 * cellSize)
    offsetY = startY - (y / 2 * cellSize)

    row = []
    # build matrixA...
    for i in range(0, y):
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
        for j in range(0, x):
            c = Entry(master, width=4)
            # calculate offset...
            cellX = offsetX + cellSize * j
            cellY = offsetY + cellSize * i
            c.place(x=cellX, y=cellY, in_=master)
            c.insert(0, "0")
            row.append(c)
        solutionMatrix.append(row)
    # done building solution matrix
#end buildSolutionMatrix

def clearMatrixA():
    matrixA = []
#end clearMatrixA()

def clearSolutionMatrix():
    solutionMatrix = []
#end clearMatrixA()

def rowResizeA(x):
    print("row resize A")
    a_x = int(x)
    clearMatrixA()
    clearSolutionMatrix()
    buildMatrixA(a_x, a_y)
    buildSolutionMatrix(a_x, a_y)
#end rowResize()

def columnResizeA(y):
    print("column resize A")
    a_y = int(y)
    buildMatrixA(a_x, a_y)
    buildSolutionMatrix(a_x, a_y)
#end columnResize()

def reduceMatrix():
    print("REDUCE MATRIX!!!!")
#end reduceMatrix

def matrixSubtractionSetup():
    print("setting up matrix subtraction...")
    print("done!")
#end matrixReductionSetup()

def matrixMultiplicationSetup():
    print("setting up matrix multiplication...")
    print("done!")
#end matrixReductionSetup()

def matrixAdditionSetup():
    print("setting up matrix addition...")
    print("done!")
#end matrixReductionSetup()

def main():
    UISetup()
    mainloop()
#end main()

#start program
main()