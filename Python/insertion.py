import sys

def InsertionSort(A, N):
    for i in range(0, N):
        temp = A[i]
        j = i - 1
        while((A[j] > temp) and (j >= 0)):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = temp
    return A

def main():
    testArray = [-2, -100, 10, 9, -6, -2, 12, -2]
    arraySize = len(testArray)

    print "The initial array is:"
    print testArray

    result = InsertionSort(testArray, arraySize)

    print "\nThe final array is:"
    print result



if __name__ == "__main__":
    sys.exit(main())