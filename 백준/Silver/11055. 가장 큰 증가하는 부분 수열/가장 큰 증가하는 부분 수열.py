import sys

input = sys.stdin.readline

"""
인사이트:
현재 숫자 기준으로, 이전 숫자중에 본인보다 큰 숫자가 있다면
이는 점점 작아지는 수열을 구성할 수 있다는 의미이다.
여기서 핵심은, 그 수열들 중 가장 큰 길이를 구해야하는 것인데
이전까지 구해진 값들 중 본인보다 큰 숫자들의 dp값들 중 가장 큰 것을 선택하면 된다.

[ex]
예시  ) 10 20 30 20 00 10
dp값 ) 01 01 01 02 03 03

위와 같은 경우에서
10은 초기값이므로 1,
20은 10이 본인보다 작으므로 1
30은 10과 20이 본인보다 작으므로 1
20은 30이 본인보다 크므로 수열 만들기 가능(30,20) 30의 dp +1인 2
0은 20이 본인보다 큰 수들 중 dp가 제일 크므로  해당 수열에 이어붙이기함 (30,20,0) 20의 dp +1 인 3
10은 20이 본인보다 큰 수들 중 dp가 제일 크므로 해당 수열에 이어붙이기 함 (30,20,10) 20의 dp + 1인 3

이에 따라 max(dp) = 3
"""


def solution(N):
    dp = []
    numbers = list(map(int, input().split()))
    dp.append(numbers[0])

    for numIdx in range(1, len(numbers)):
        # 본인의 이전 숫자들 중 본인보다 작은 숫자 탐색
        # 그 중에서도 dp가 제일 높은 값을 선택
        maxDP = 0
        for beforeNumIDx in range(numIdx):
            if numbers[beforeNumIDx] < numbers[numIdx] and dp[beforeNumIDx] > maxDP:
                maxDP = dp[beforeNumIDx]

        # 만약 앞에 본인보다 큰게 없었다면 maxDP가 0이므로 자동으로 본인 값만 저장될 것이고
        # 본인보다 큰게 있었다면 그 DP 값 + 현재값으로 추가
        dp.append(maxDP + numbers[numIdx])

    result = max(dp)

    return result


N = int(input())
result = solution(N)
print(result)
