import sys
import math
from collections import defaultdict
import heapq

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    roads = defaultdict(
        lambda: defaultdict(lambda: math.inf)
    )  # 없는 값에 대하여 자동으로 이중 딕셔너리 생김

    for _ in range(M):
        A, B, cows = map(int, input().split())
        newCowsInAtoB = min(roads[A].get(B, math.inf), cows)
        roads[A][B] = newCowsInAtoB
        roads[B][A] = newCowsInAtoB

    # 최소거리, 위치 순
    djk = [(0, 1)]  # 시작위치를 넣어놓는다. 시작에서 시작까지의거리는 0이다.
    djkStatus = [math.inf for _ in range(N + 1)]
    djkStatus[1] = 1

    while djk:
        nowDist, nowPos = heapq.heappop(djk)

        # 목적지 도착시 현재 이동거리 반환
        if nowPos == N:
            return djkStatus[nowPos]

        for nextPos, nextDist in roads[nowPos].items():
            nextTotalDist = nowDist + nextDist
            # 새로운 최단경로 파악
            if djkStatus[nextPos] > nextTotalDist:
                djkStatus[nextPos] = nextTotalDist
                heapq.heappush(djk, (nextTotalDist, nextPos))


print(solution())
