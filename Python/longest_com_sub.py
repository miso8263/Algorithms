import random
import sys
"""
Longest Common Subsequence
Michelle Soult, COEN279
Using lecture implementation of longest common subsequence
generate table, reconstruct LCS, and print it out

main generates two random strings of length 10 for testing

run on the command line:
python longest_com_sub.py

requires python 2.7
"""

def LCS(s1, s2):
    m = len(s1)
    n = len(s2)

    M = [[0 for x in range(0, m+1)] for o in range(0, n+1)]

    for i in range(-1, m): #need extra padding for the 0th row and column
        for j in range(-1, n):
            if i == -1 or j == -1:
                M[i+1][j+1] = (0, '')
            elif s1[i] == s2[j]:
                M[i+1][j+1] = (1 + M[i][j][0], s1[i])
            else:
                M[i+1][j+1] = (max(M[i+1][j][0], M[i][j+1][0]), '')

    finalseq = ['' for x in range (0, M[m][n][0])]

    tot =  M[m][n][0]
    i = m
    j = n
    while(tot > 0):
        if i == 0 or j == 0:
            return finalseq
        if i == 1:
            if M[i][j][0] > M[i-1][j][0] and M[i][j][0] > M[i][j-1][0]:
                finalseq[tot-1] = M[i][j][1]
                j = j - 1
                tot = tot - 1
            else:
                j = j - 1
        elif j == 1:
            if M[i][j][0] > M[i-1][j][0] and M[i][j][0] > M[i][j-1][0]:
                finalseq[tot-1] = M[i][j][1]
                i = i - 1
                tot = tot - 1
            else:
                i = i - 1
        elif M[i][j][0] > M[i-1][j][0] and M[i][j][0] > M[i][j-1][0]:
            finalseq[tot-1] = M[i][j][1]
            i = i - 1
            j = j - 1
            tot = tot - 1
        elif M[i][j-1][0] > M[i-1][j][0]:
            j = j - 1
        else:
            i = i -1

    return ''.join(finalseq)

def main():
    listseq1 = []
    listseq2 = []
    for i in range(0, 10):
        listseq1.append(chr(random.randrange(97, 123))) #ascii value of lowercase numbers
        listseq2.append(chr(random.randrange(97, 123)))

    seq1 = ''.join(listseq1)
    seq2 = ''.join(listseq2)
    print "Sequence 1 is:\n"+seq1
    print "Sequence 2 is:\n"+seq2

    result = LCS(listseq1, listseq2)

    print "Their longest common subsequence is:\n"
    print result

if __name__ == "__main__":
    sys.exit(main())