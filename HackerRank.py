#HackerRank
#Weird Algorithm
def weird(n):
    if n % 2 == 0:
        if n > 2 and n < 5:
            print("Not Weird")
        elif n > 6 and n < 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
    else:
        print("Weird")
weird(4)

#Algorithms Warmup
#Compare the Triplets
#https://www.hackerrank.com/challenges/compare-the-triplets/problem
def comparetriplets(a,b):
    scoresA = 0
    scoresB = 0 #Initialise object scores to zero
    for i in range(0,len(a)): #Loop through every index of the array
        if a[i] > b[i]:
            scoresA += 1 #Increment the step by 1, essentially scoresA = scoresA + 1
        elif a[i] < b[i]:
            scoresB += 1 #Increment the step by 1, essentially scoresB = scoresB + 1
        elif a[i] == b[i]:
            None #Nothing will happen
    return [scoresA,scoresB] #After the loop, return the two values into an array
j = [4,8,2]
k = [7,1,4]
comparetriplets(j,k)

#A Very Big Sum
#https://www.hackerrank.com/challenges/a-very-big-sum/problem?h_r=next-challenge&h_v=zen
def aVeryBigSum(ar):
    return sum(ar)

#A Diagnoal Difference
#https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def diagonalDifference(arr):
    ctr = 0 #Initialise counter to zero
    rctr = len(arr)-1 #Initialise reversed counter to the length of the array, subtract by 1
    ltrd = []
    rtld = [] #Initialise empty lists
    for i in range(len(arr)):
        ltrd.append(arr[ctr][ctr])
        ctr += 1
        fltrd = sum(ltrd)
    ctr = 0
    for i in range(len(arr)):
        rtld.append(arr[ctr][rctr])
        ctr+=1
        rctr-=1
        frtld = sum(rtld)
    difference = abs(fltrd - frtld)
    return difference
test = [[11,2,4],[4,5,6],[10,8,-12]]
diagonalDifference(test)
#Extra Long Factorials
#https://www.hackerrank.com/challenges/extra-long-factorials/problem
def extraLongFactorials(n):
    total = 1 #Intialise counter, make it equal to 1
    for i in range(1,n+1): #Since input is integer, this is how you write the range
        total *= i #Increment the total variable
    print(total)
extraLongFactorials(25)
#Staircase
#https://www.hackerrank.com/challenges/staircase/problem
def staircase(n):
    for i in range (1,n+1):
        hsh = "#" * i 
        print(hsh.rjust(n))
staircase(6)
#Append and Delete
#https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_v=zen
def appendAndDelete(s,t,k):
    for i 