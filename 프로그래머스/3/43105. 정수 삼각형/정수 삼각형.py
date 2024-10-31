def solution(triangle):
    DP = [[0 for _ in range(i+1)]for i in range(len(triangle))]
    DP[0][0] = triangle[0][0]
    
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0:
                DP[i][j] = DP[i-1][j] + triangle[i][j]
            elif j == i:
                DP[i][j] = DP[i-1][j-1] + triangle[i][j]
            else:
                DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + triangle[i][j]

    return(max(DP[-1]))
