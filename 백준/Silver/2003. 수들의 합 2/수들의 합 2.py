import sys

"""
[입력]
1. N: 수열 개수 M: 원하는 합
2. N개의 수열 원소

[과정]
! window 와 비슷하게 계산 (창문을 옆으로 여는 것 같이)

1. i~j sum < M 이면 계속 j 증가
o o o o o o o o o o
i   j->

2. i~j sum == M 이면 경우의 수 증가

3. i~j sum > M 이면 계속 i 증가 
o o o o o o o o o o
i-> j

[출력]
수열[i] ~ 수열[j]까지의 합이 M이 되는 모든 경우의 수
"""

# [입력]
## 수열 개수, 합
N, expectSum = map(int, sys.stdin.readline().split())
## 수열
nums = list(map(int, sys.stdin.readline().split()))

i, j = 0, 0
sum = 0
cases = 0

# i나 j index가 수열 범위를 벗어나면 종료
while j <= N and i <= j:
    try:
        if sum == expectSum:
            cases += 1
            sum += nums[j]
            j += 1
        elif sum < expectSum:
            sum += nums[j]
            j += 1
        else:
            sum -= nums[i]
            i += 1
    except IndexError:
        break

print(cases)
