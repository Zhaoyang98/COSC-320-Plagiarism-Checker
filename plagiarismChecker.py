# This python program was built to take a bunch of 
# documents as input and determine how much of a target 
# document is similar to the other documents by 
# using various algorithms
import os
d = 256


#First the KMP algorith: reference: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
#This algorithm is for checking single character matching and will be weighed the least
def KMPCheck(pat, txt):
    M = len(pat)
    N = len(txt)

    #longest prefix suffix:
    lps = [0]*M
    j = 0 #pattern index

    computeLPSArray(pat, M, lps)

    i=0; #txt index
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print("Found pattern at index" + str(i-j))
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j= lps[j-1]
            else:
                i+=1

def computeLPSArray(pat, M, lps):
    len = 0 #length of previous lps
    lps[0] 
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i+= 1
        else:
            if len!= 0:
                len = lps[len-1]

            else:
                lps[i] = 0
                i += 1


#Now the Rabin-Karp Algorithm, which checks for entire words that match:
#https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/

def RBKCheck(pat, txt, q):# q must be a prime number
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0 #pattern hash
    h = 0 #txt hash 
    for i in range(M-1):
        h = (h*d)%q
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q

    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
            j+=1
            if j==M:
                print("pattern found at index " + str(i))
        
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))%q

            if t<0:
                t = t + q


#here is where the main program will run

print("here is the current directory: " + os.getcwd())

file1 = open("./example.txt", "r")

text = file1.read() #this text file now holds the entire string from example.txt

print(text)
