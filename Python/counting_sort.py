import sys
import random
"""
Two implementations of counting sort
Michelle Soult, COEN279
Counting sort A is the implementation from lecture
(does not handle negative numbers)
Counting sort B is Michelle's implementation
(does handle negative numbers)

main generates random array for testing

run on the command line:
python radix_sort.py

requires python 2.7
"""

#Lecture implementation
def countingSortA(A):
    # running time = O(N+K)
    k = max(A)

    B = [0 for x in range(0, k+1)]

    for j in range(0, len(A)):
        B[A[j]] = B[A[j]]+1

    for m in range(1, k+1):
        B[m] = B[m] + B[m-1]

    C = [0 for x in range(0, len(A))] 
    for x in range(0, len(A)):
        C[B[A[x]]-1] = A[x]
        B[A[x]] = B[A[x]] - 1

    return C

#Michelle's implementation; different than lecture
def countingSortB(A): 
    #find min/max
    a_max = A[0]
    a_min = A[0]
    for item in A: 
        if item > a_max:
            a_max = item
        elif item < a_min:
            a_min = item

    shift = 0
    if a_min < 0:
        shift = abs(a_min)

    #generate array
    sorty = []
    for i in range(0, (a_max + shift + 2)):
        sorty.append(0)

    #accumulate number of eac hitem
    for item in A:
        sorty[item+shift]+=1

    #regenerate array
    k = 0
    for j in range(0, len(sorty)):
        while(sorty[j] > 0):
            A[k] = j - shift
            sorty[j] = sorty[j] - 1
            k += 1
    return A

def main():
    #generate an array of 10 random items in the range 0-100
    testArray = []
    for i in range(0, 10):
        testArray.append(random.randrange(0, 100))
    arraySize = len(testArray)

    print "The initial array is:"
    print testArray

    result = countingSortB(testArray)

    print "\nThe sorted array is:"
    print result

    result2 = countingSortA(testArray)
    print "\nThe sorted array from lecture is:"
    print result2

if __name__ == "__main__":
    sys.exit(main())
