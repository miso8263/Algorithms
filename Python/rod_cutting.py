import sys
import random

"""
Rod Cutting
Michelle Soult, COEN279
Using lecture implementation of top-down with memoization rod cutting
Determines highest value cuts and prints the total price of all cuts

main generates random rod length (1-10) and price list (0-5) for testing

run on the command line:
python rod_cutting.py

requires python 2.7
"""

#top-down with memoization
def cut_rod_t(n, P, RM):
    if n == 0:
        return 0
    if n in RM.keys():
        return RM[n]
    rm = P[n]
    for i in range(1, n+1):
        rm = max(rm, P[i] + cut_rod_t(n-i, P, RM))
    RM[n] = rm
    return rm

def main():
    myRodLen = random.randrange(1, 10)
    priceList = [0]
    for i in range(0, myRodLen):
        priceList.append(random.randrange(0, 5))

    print "My rod is "+str(myRodLen)+" units long."
    print "The price list is: "
    print "length \t|\t price"
    for j in range(1, myRodLen+1):
        print " "+str(j)+"\t \t"+str(priceList[j])

    memoization = {}
    result = cut_rod_t(myRodLen, priceList, memoization)

    print "The value of my best cuts is: "

    print result

if __name__ == "__main__":
    sys.exit(main())