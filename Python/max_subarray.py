import sys
from max_subarray_bf import MaxSubarrayBF 
#divide and conquer approach

def CalcMiddle(A, i, j, mid):
    max_sum = A[mid]
    curr_sum = A[mid]
    index1 = mid
    index2 = mid
    for k in range(mid-1, i, -1): #middle already included in sum
        curr_sum = curr_sum + A[k]
        if curr_sum > max_sum:
            max_sum = curr_sum
            index1 = k

    curr_sum = max_sum #now add on the right side
    for m in range(mid+1, j): 
        curr_sum = curr_sum + A[m]
        if curr_sum > max_sum:
            max_sum = curr_sum
            index2 = m

    return max_sum, index1, index2


def MaxSubarray(A, i, j):
    if j < 40:
        return MaxSubarrayBF(A, j)
    mid = (i + j) // 2 #integer division, essentially taking the floor
    if(j - i) < 2:
        return A[i], i, j
    sumL, iL, jL = MaxSubarray(A, i, mid)
    sumR, iR, jR = MaxSubarray(A, mid, j)
    sumM, iM, jM = CalcMiddle(A, i, j, mid)

    if(sumL < sumR):
        if(sumR < sumM):
            return sumM, iM, jM
        else:
            return sumR, iR, jR
    else:
        if(sumL < sumM):
            return sumM, iM, jM
        else:
            return sumL, iL, jL


def main():
    testArray = [-2, -100, 10, 9, -6, -2, 12, -2]
    arraySize = len(testArray)

    print "The array is:"
    print testArray
    print ""

    max_sum, i, j = MaxSubarray(testArray, 0, arraySize)

    print "\nThe maximum sum is: "+str(max_sum)+" and the indices are ("+str(i)+","+str(j)+")"



if __name__ == "__main__":
    sys.exit(main())