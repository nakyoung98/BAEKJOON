import sys

# 정수의 개수 N, 찾고자하는 합 S
N, S = map(int,sys.stdin.readline().split())
Numbers = list(map(int,sys.stdin.readline().split()))

# 경우의 수를 담을 변수
result = 0

def dfs(i,sum):
    sum += Numbers[i]

    # 합이 S일 경우 경우의 수 ++
    # 음수가 포함된 순열인만큼, 이후에 똑같은 값이 또 나올 수 있음
    if sum == S:
        global result
        result += 1
        
    # i 값이 N과 같거나 클 경우 더이상 Numbers 중 접근 가능한 인덱스가 없으므로 종료
    # i 값이 N-1인 경우에는, 이미 마지막 계산인 sum+=Numbers[N-1]까지 했음에도 sum != S이므로 더이상 계산할 필요가 없어 종료
    if N-1 <= i:
        return
    
    # list의 다음 숫자들에 대해 dfs 탐색
    for j in range(i+1, N):
        dfs(j,sum)

    return

# 가장 먼저 담길 수 지정
for i in range(N):
    dfs(i,0)

print(result)