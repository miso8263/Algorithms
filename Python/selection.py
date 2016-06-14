import sys

def SelectionSort(A, N):
    for i in range(0, N-1):
        min_index = i
        for j in range(i, N):
            if A[min_index] > A[j]:
                min_index = j
        temp = A[i]
        A[i] = A[min_index]
        A[min_index] = temp
        print A
    return A

def main():
    testArray = [8, 7, 6, 5, 4, 3, 2, 1]
    arraySize = 8

    print "The initial array is:"
    print testArray

    result = SelectionSort(testArray, arraySize)

    print "\nThe final array is:"
    print result



if __name__ == "__main__":
    sys.exit(main())