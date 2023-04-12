import sys

n = int(sys.stdin.readline())
permutation = list(map(int, sys.stdin.readline().split()))
permutation.insert(0,0)

dp = [[] for _ in range(len(permutation))]
dp[1] = [permutation[1]]

maxDp = 1

for i in range(2,n+1):
    now = permutation[i]

    if now > dp[i-1][-1] and len(dp[i-1]) == maxDp:
        templist = dp[i-1][:]
        templist.append(now)
        dp[i] = templist

        maxDp += 1

    else:
        max = 0
        index = 0
        for j in range(1,i):
            if dp[j][-1] < now and len(dp[j]) > max:
                max = len(dp[j])
                index = j

        templist = dp[index][:]
        templist.append(now)
        dp[i] = templist

        if  len(dp[i]) > maxDp:
            maxDp += 1

    # print(*dp)
    # print("maxDp", maxDp)

print(maxDp)