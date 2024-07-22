import sys


def solution(data):
    # dp 생성 및 초기값
    dp = [0, 1, 2]

    if data < len(dp):
        return dp[data]

    # 현재를 기준으로 나올 수 있는 경우의 수는
    # 이전 결과에 세로를 추가로 붙이는 것과
    # 이전이전 결과에 가로 두개를 병렬로 붙이는 것이다.

    # 위 두 경우의 수는 결코 겹치지 않는다.
    # 이전이전이전까지는 같은 모양이라 하였더라도
    # 이전이전부터 분기가 일어나기 때문이다.

    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[data]


n = int(sys.stdin.readline())
print(solution(n) % 10007)
