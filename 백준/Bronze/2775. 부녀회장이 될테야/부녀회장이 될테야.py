import sys


def solution(T):
    result = []
    for _ in range(T):
        floor = int(sys.stdin.readline())
        room = int(sys.stdin.readline())

        #  기본 값 0층 dp[0] 과 나머지 층에 대한 빈 배열 생성 : 이중배열
        ## [*][0]  = 0 으로 유지
        dp = [[i for i in range(room + 1)]] + [[0] * (room + 1) for _ in range(floor)]

        for nowFloor in range(1, floor + 1):
            for nowRoom in range(1, room + 1):
                dp[nowFloor][nowRoom] = sum(dp[nowFloor - 1][: nowRoom + 1])

        result.append(dp[nowFloor][nowRoom])

    return "\n".join(map(str, result))


T = int(sys.stdin.readline())
print(solution(T))
