# Set(해시)로 묶음 O(1)
# 데이터 10000개 -> N^2 미만

import sys

ENTER_LOG = "ENTER"


def solution(N):
    result = 0
    logs = []

    for _ in range(N):
        log = sys.stdin.readline().rstrip()

        if log == ENTER_LOG:
            # 새 로그 추가
            logs.append(set())
        else:
            # 현재 로그 문서에 log 추가
            logs[-1].add(log)

    result = sum(map(len, logs))
    return result


N = int(sys.stdin.readline())
print(solution(N))
