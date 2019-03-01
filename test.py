# test.py handles unit and integration tests
from matrixReduction import *

def integrationTest():
    if not testMatrixReduction():
        print("matrix reduction failed")
        return False

    if not testMatrixAddition():
        print("matrix addition failed")
        return False

    if not testMatrixSubtraction():
        print("matrix subtraction failed")
        return False

    if not testMatrixMultiplication():
        print("matrix multiplication failed")
        return False

    return True
# end integrationTest()

def testMatrixReduction():
    print("testing matrix reduction...")

    # test case 1: normal matrix
    test1 = [
        [0, 3, -6, 6, 4, -5],
        [3, -7, 8, -5, 8, 9],
        [3, -9, 12, -9, 6, 15]
    ]

    solution1 = [
        [1, 0, -2, 3, 0, -24],
        [0, 1, -2, 2, 0, -7],
        [0, 0, 0, 0, 1, 4]
    ]

    # test case 2: matrix that results in a row of zeros
    test2 = [
        [1, 2, 1, 1, 7],
        [1, 2, 2, -1, 12],
        [2, 4, 0, 6, 4]
    ]

    solution2 = [
        [1, 2, 0, 3, 2],
        [0, 0, 1, -2, 5],
        [0, 0, 0, 0, 0]
    ]

    # test case 3: matrix with an empty row
    test3 = [
        [4, 3, 3, 4, 1],
        [0, 0, 0, 0, 0],
        [3, 2, 8, 7, 1],
        [4, 1, 11, 4, 3],
        [8, 7, 3, 11, 9]
    ]
    solution3 = [
        [1, 0, 0, 0, 9],
        [0, 1, 0, 0, -13.488],
        [0, 0, 1, 0, -3.122],
        [0, 0, 0, 1, 3.707],
        [0, 0, 0, 0, 0]
    ]

    # test case 4: matrix with an empty column
    test4 = [
        [4, 0, 31, 11, 9],
        [3, 0, 21, 2, 3],
        [1, 0, 3, 14, 10],
        [9, 0, 1, 32, 9],
        [11, 0, 4, 1, 12]
    ]
    solution4 = [
        [1, 0, 0, 0, 1.368],
        [0, 0, 1, 0, -0.114],
        [0, 0, 0, 1, 0.641],
        [0, 0, 0, 0, -23.709],
        [0, 0, 0, 0, -3.236]
    ]

    # test case 5: zero matrix
    test5 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    solution5 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    # test case 6: empty matrix
    test6 = []
    solution6 = []

    test1 = rowReduce(test1)
    output = assertEqual(test1, solution1)
    if not output:
        print("test1 failed")
        return False

    test2 = rowReduce(test2)
    output = assertEqual(test2, solution2)
    if not output:
        print("test2 failed")
        return False

    test3 = rowReduce(test3)
    output = assertEqual(test3, solution3)
    if not output:
        print("test3 failed")
        return False

    test4 = rowReduce(test4)
    output = assertEqual(test4, solution4)
    if not output:
        print("test4 failed")
        return False

    test5 = rowReduce(test5)
    output = assertEqual(test5, solution5)
    if not output:
        print("test5 failed")
        return False

    test6 = rowReduce(test6)
    output = assertEqual(test6, solution6)
    if not output:
        print("test6 failed")
        return False

    # print("Matrix reduction OK!")
    return True
# end testMatrixReduction()

def testMatrixAddition():
    return True
# end testMatrixAddition()

def testMatrixSubtraction():
    return True
# end testMatrixSubtraction()

def testMatrixMultiplication():
    return True
# end testMatrixMultiplication()



