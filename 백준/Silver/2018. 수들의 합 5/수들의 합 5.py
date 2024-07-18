import sys

"""
[입력]
1. N: 합 기댓값

[로직]

! 최대 복잡도
제한: 2초
데이터: 10,000,000
logN = 최대 23정도
가능 계산횟수: N * logN


! 투포인터 O(n)
투포인터를 연속된 수의 시작(i)과 끝+1(j)로 지칭

ex) 기대값 15

j가 N+1에 도달할 때까지 반복
    j가 N+1을 넘으면 어떻게 해도 N보다 큼

    1. 합 == 기대값
        i:1 j:6 -> 1+2+3+4+5 : 15

        경우의수 +1
        j 하나 늘리기, sum 조정

    2. 합 > 기대값
        i:1 j:7 -> 21

        i 하나 늘리기, sum 조정

    3. 합 < 기대값
        i:6 j:8 -> 13
        
        j 하나 늘리기, sum 조정


[출력]
경우의 수
"""

expectedSum = int(sys.stdin.readline())
sum = 0
min, max = 0, 0
cases = 0

# 투포인터로 접근 O(expectedSum)
while max <= expectedSum + 1 and min <= max:
    # 실 합과 기대값이 같으면
    if sum == expectedSum:
        cases += 1

        sum += max
        max += 1

    elif sum > expectedSum:
        sum -= min
        min += 1

    elif sum < expectedSum:
        sum += max
        max += 1

print(cases)
