import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())

    bridges = [[0 for i in range(N+1)] for i in range(M+1)]

    for i in range(1,M+1):
        for j in range(1,N+1):
            if j == 1 :
                bridges[i][j] = i
            elif i == j:
                bridges[i][j] = 1
            elif j<i:
                bridges[i][j] = bridges[i-1][j]+bridges[i-1][j-1]

    print(bridges[M][N])