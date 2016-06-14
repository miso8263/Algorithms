import sys
import random
"""
Radix sort
Michelle Soult, COEN279
Using lecture implementation of counting sort,
which is stable but doesn't handle negative numbers

main generates random array for testing

run on the command line:
python radix_sort.py

requires python 2.7
"""

def radixSort(A, dig):
    #generate the "columns" in the array
    splitA = []
    for item in A:
        line = []
        if len(str(item)) < dig: #pad with extra 0s
            padLen = dig - len(str(item))
            for i in range(0, padLen):
                line.append(0)
            for j in str(item):
                line.append(int(j))
        else:
            line = [int(x) for x in str(item)]
        splitA.append(line)

    #do the actual sorting part
    for column in range(dig-1, -1, -1): #least significant to most significant
        splitA = countingSortA(splitA, column)
    
    #turn the "columns" back into a normal array
    combineA = []
    for arr in splitA:
        newline = [str(x) for x in arr]
        combineA.append(int(''.join(newline)))
    return combineA

#Lecture implementation
def countingSortA(A, col):
    # running time = O(N+K)
    #find max
    k = A[0][col]
    for i in range(0, len(A)):
        if k < A[i][col]:
            k = A[i][col]

    #generate indices array
    B = [0 for x in range(0, k+1)]

    for j in range(0, len(A)):
        B[(A[j][col])] = B[(A[j][col])]+1

    for m in range(1, k+1):
        B[m] = B[m] + B[m-1]

    #generate return array 
    C = [0 for x in range(0, len(A))] 

    for x in range(len(A)-1, -1, -1):
        C[B[(A[x][col])]-1] = A[x]
        B[(A[x][col])] = B[(A[x][col])] - 1

    return C

def main():
    #generate an array of 10 random items in the range 0-100
    testArray = []
    for i in range(0, 10):
        testArray.append(random.randrange(0, 10000))

    print "The initial array is:"
    print testArray

    result2 = radixSort(testArray, 4) #add in number of digits
    print "\nThe sorted array is:"
    print result2

if __name__ == "__main__":
    sys.exit(main())
