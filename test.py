# test.py handles unit and integration tests

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
    return True
#end testMatrixReduction()

def testMatrixAddition():
    return True
#end testMatrixAddition()

def testMatrixSubtraction():
    return True
#end testMatrixSubtraction()

def testMatrixMultiplication():
    return True
#end testMatrixMultiplication()



