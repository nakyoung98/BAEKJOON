import sys

X = int(sys.stdin.readline())

#index 0 ~ X
dp = [0 for _ in range(X+1)]

#index 2부터 X까지 dp에 값 반영, 1은 어짜피 0임
## 우선 순위가 없음 ##
for i in range(2,X+1):
    
    mins = []
    
    if i%3 == 0:
        mins.append( min(dp[i-1],dp[int(i/3)]) + 1)
    if i%2 == 0:
        mins.append(min(dp[i-1],dp[int(i/2)]) + 1)
    if i%3 != 0 and i%2 != 0:
        mins.append(dp[i-1]+1)

    dp[i] = min(mins)

print(dp[X])