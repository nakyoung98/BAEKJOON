import sys

N,K = map(int,sys.stdin.readline().split())

A = list(map(int,sys.stdin.readline().split()))


change = 0
for i in range(len(A),1,-1):
    maxInd = A[:i].index(max(A[:i])) 

    if maxInd != i-1:
        change += 1
        A[i-1],A[maxInd] = A[maxInd],A[i-1]

        if change == K:
            print(A[maxInd],A[i-1])
            break

if change <K:
    print(-1)