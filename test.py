# test.py handles unit and integration tests
from matrixReduction import *
from matrixMultiplication import *
from matrixSubtraction import *
from matrixAddition import *

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
    print("testing matrix addition...")

    # test case 1: regular 2x2 matricies
    test1_a = [
        [1, 2],
        [3, 4]
    ]

    test1_b = [
        [5, 6],
        [7, 8]
    ]

    solution1 = [
        [6, 8],
        [10, 12]
    ]

    # test case 2 - invalid dimensions
    test2_a = [
        [1, 1, 1],
        [1, 1, 1],
        [0, 0, 0],
    ]

    test2_b = [
        [0, 1],
        [0, 1]
    ]

    solution2 = []

    # test case 3 - zero matrix
    test3_a = [
        [0, 0],
        [0, 0]
    ]

    test3_b = [
        [0, 0],
        [0, 0]
    ]

    solution3 = [
        [0, 0],
        [0, 0]
    ]

    test4_a = [
        [-1, -1, -1],
        [-2, -2, -2],
        [3, 3, 3]
    ]

    test4_b = [
        [1, 1, 1],
        [2, 2, 2],
        [-3, -3, -3]
    ]

    solution4 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    test1 = matrixAddition(test1_a, test1_b)
    output = assertEqual(test1, solution1)
    if not output:
        print("test1 failed")
        return False

    test2 = matrixAddition(test2_a, test2_b)
    output = assertEqual(test2, solution2)
    if not output:
        print("test2 failed")
        return False

    test3 = matrixAddition(test3_a, test3_b)
    output = assertEqual(test3, solution3)
    if not output:
        print("test3 failed")
        return False

    test4 = matrixAddition(test4_a, test4_b)
    output = assertEqual(test4, solution4)
    if not output:
        print("test4 failed")
        return False

    return True
# end testMatrixAddition()

def testMatrixSubtraction():
    print("testing matrix subtraction...")

    # test case 1: regular 2x2 matricies
    test1_a = [
        [1, 2],
        [3, 4]
    ]

    test1_b = [
        [5, 6],
        [7, 8]
    ]

    solution1 = [
        [-4, -4],
        [-4, -4]
    ]

    # test case 2 - invalid dimensions
    test2_a = [
        [1, 1, 1],
        [1, 1, 1],
        [0, 0, 0],
    ]

    test2_b = [
        [0, 1],
        [0, 1]
    ]

    solution2 = []

    # test case 3 - zero matrix
    test3_a = [
        [0, 0],
        [0, 0]
    ]

    test3_b = [
        [0, 0],
        [0, 0]
    ]

    solution3 = [
        [0, 0],
        [0, 0]
    ]

    test4_a = [
        [-1, -1, -1],
        [-2, -2, -2],
        [3, 3, 3]
    ]

    test4_b = [
        [1, 1, 1],
        [2, 2, 2],
        [-3, -3, -3]
    ]

    solution4 = [
        [-2, -2, -2],
        [-4, -4, -4],
        [6, 6, 6]
    ]

    test1 = matrixSubtraction(test1_a, test1_b)
    output = assertEqual(test1, solution1)
    if not output:
        print("test1 failed")
        return False

    test2 = matrixSubtraction(test2_a, test2_b)
    output = assertEqual(test2, solution2)
    if not output:
        print("test2 failed")
        return False

    test3 = matrixSubtraction(test3_a, test3_b)
    output = assertEqual(test3, solution3)
    if not output:
        print("test3 failed")
        return False

    test4 = matrixSubtraction(test4_a, test4_b)
    output = assertEqual(test4, solution4)
    if not output:
        print("test4 failed")
        return False

    return True
# end testMatrixSubtraction()

def testMatrixMultiplication():
    print("testing matrix multiplication...")

    # test case 1: regular 2x2 matricies
    test1_a = [
        [1, 2],
        [3, 4]
    ]

    test1_b = [
        [5, 6],
        [7, 8]
    ]

    solution1 = [
        [19, 22],
        [43, 50]
    ]

    # test case 2 - invalid dimensions
    test2_a = [
        [1, 2, 3],
        [11, 12, 13],
        [5, 15, 0]
    ]

    test2_b = [
        [9, 9, 10],
        [4, 11, 10]
    ]

    solution2 = []

    # test case 3 - 3x2 matrix and 2x4 matrix
    test3_a = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    test3_b = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]

    solution3 = [
        [11, 14, 17, 20],
        [23, 30, 37, 44],
        [35, 46, 57, 68]
    ]

    #test case 4 - zero matrix
    test4_a = [
        [0, 0],
        [0, 0]
    ]

    test4_b = [
        [0, 0],
        [0, 0]
    ]

    solution4 = [
        [0, 0],
        [0, 0]
    ]

    # test case 5 - big dimensions
    test5_a = [
        [11, 12, 87, 8, 92],
        [98, 73, 37, 2, 8],
        [11, 42, 44, 2, 1],
        [8, 76, 72, 22, 29],
        [8, 11, 7, 17, 16],
        [81, 8, 9, 12, 27],
        [8, 98, 71, 72, 98],
        [72, 82, 72, 6, 7]
    ]

    test5_b = [
        [1, 7, 27, 67, 7, 9, 22, 21],
        [76, 2, 78, 7, 23, 62, 60, 8],
        [55, 12, 8, 19, 8, 99, 81, 60],
        [11, 18, 90, 55, 40, 33, 95, 70],
        [3, 9, 55, 6, 5, 78, 4, 8]
    ]

    solution5 = [
        [6072, 2117, 7709, 3466, 1829, 16896, 9137, 6843],
        [7727, 1384, 9256, 7938, 2781, 9761, 9755, 5066],
        [5648, 734, 4160, 1983, 1480, 7203, 6520, 3355],
        [10073, 1729, 10295, 3820, 3405, 14900, 12774, 6868],
        [1464, 612, 3540, 1777, 1125, 3256, 3082, 1994],
        [1397, 1150, 5448, 6476, 1438, 4618, 4239, 3361],
        [12447, 3282, 20298, 7119, 6248, 23197, 19039, 11036],
        [10351, 1703, 9841, 7138, 3241, 13604, 12934, 6964]
    ]

    test1 = matrixMultiplication(test1_a, test1_b)
    output = assertEqual(test1, solution1)
    if not output:
        print("test1 failed")
        return False

    test2 = matrixMultiplication(test2_a, test2_b)
    output = assertEqual(test2, solution2)
    if not output:
        print("test2 failed")
        return False

    test3 = matrixMultiplication(test3_a, test3_b)
    output = assertEqual(test3, solution3)
    if not output:
        print("test3 failed")
        return False

    test4 = matrixMultiplication(test4_a, test4_b)
    output = assertEqual(test4, solution4)
    if not output:
        print("test4 failed")
        return False

    test5 = matrixMultiplication(test5_a, test5_b)
    output = assertEqual(test5, solution5)
    if not output:
        print("test5 failed")
        return False

    return True
# end testMatrixMultiplication()



