import sys

def merge(A, begin, mid, end):
    #now merge
    leftHalf = A[begin:mid]
    rightHalf = A[mid:end]

    #handle array with different size sections
    leftHalf.append(10000000000)
    rightHalf.append(10000000000)

    i = 0
    j = 0
    for k in range(begin, end):
        if(leftHalf[i] < rightHalf[j]):
            A[k] = leftHalf[i]
            i = i + 1
        else: #equal goes in this side
            A[k] = rightHalf[j]
            j = j + 1
    return A

def MergeSort(A, begin, end):
    if(end > begin):
        if(end == (begin+1)):
            #if we've got only 2 items in the array
            return A
        #split
        mid = (begin + end) / 2 #integer division; ignore decimal component; a.k.a. floor
        MergeSort(A, begin, mid)
        MergeSort(A, mid, end)

        merge(A, begin, mid, end)

    return A


def main():
    testArray = [8, 7, 6, 5, 4, 3, 2, 1]
    arraySize = len(testArray)

    print "The initial array is:"
    print testArray

    result = MergeSort(testArray, 0, arraySize)

    print "\nThe final array is:"
    print result



if __name__ == "__main__":
    sys.exit(main())