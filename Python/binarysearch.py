import sys

def BinarySearch(A, begin, end, val):
    mid = (begin + end) / 2
    if val == A[mid]:
        return A[mid]
    elif end - begin < 2:
        return None
    elif val > A[mid]:
        return BinarySearch(A, mid, end, val)
    else:
        return BinarySearch(A, begin, mid, val)


def main():
    testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arraySize = len(testArray)

    print "The initial array is:"
    print testArray

    result = BinarySearch(testArray, 0, arraySize, 1)

    print "\nFound:"
    print result



if __name__ == "__main__":
    sys.exit(main())