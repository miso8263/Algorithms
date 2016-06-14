import sys

def BubbleSort(A, aSize):
    for i in range(0, aSize):
        for j in range(aSize-1, i, -1):
            if(A[j] < A[j-1]):
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
            print "i = " + str(i) + " and j = " + str(j)
            print A
        print ""
    return A


def main():
    testArray = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    arraySize = len(testArray)

    print "The initial array is:"
    print testArray
    print ""

    result = BubbleSort(testArray, arraySize)

    print "\nThe sorted array is:"
    print result



if __name__ == "__main__":
    sys.exit(main())