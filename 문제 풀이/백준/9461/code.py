import sys

input = sys.stdin.readline

# 패턴
# 직전 삼각형 + 5번째 전 삼각형이 합쳐지는 형태
# 단, 맨 앞 1,1,1,2,2는 고정 값


def solution(N):
    dp = [1, 1, 1, 2, 2]

    for i in range(5, N):
        dp.append(dp[i - 1] + dp[i - 5])

    # N번째 삼각형 변 길이 반환
    return dp[N - 1]


def code():
    T = int(input())

    for _ in range(T):
        N = int(input())
        result = solution(N)
        print(result)


code()
