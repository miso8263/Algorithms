import sys

#brute force approach
def MaxSubarrayBF(A, aSize):
    max_sum = A[0]
    index1 = 0
    index2 = 0
    for i in range(0, aSize):
        curr_sum = A[i]
        for j in range(i+1, aSize):
            curr_sum = curr_sum + A[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
                index1 = i
                index2 = j
    return max_sum, index1, index2

def main():
    testArray = [-2, -100, 10, 9, -6, -2, 12, -2]
    arraySize = len(testArray)

    print "The array is:"
    print testArray
    print ""

    max_sum, i, j = MaxSubarray(testArray, arraySize)

    print "\nThe maximum sum is: "+str(max_sum)+" and the indices are ("+str(i)+","+str(j)+")"



if __name__ == "__main__":
    sys.exit(main())