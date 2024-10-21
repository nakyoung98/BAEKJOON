import sys
import heapq
import math

input = sys.stdin.readline


def solution():
    cities, roads, hopeDistance, startCity = map(int, input().split())

    # city의 개수만큼 로드맵 구현 (인접리스트)
    roadMap = [[] for _ in range(cities + 1)]

    # roadMap 채우기
    for _ in range(roads):
        start, end = map(int, input().split())
        roadMap[start].append(end)

    result = djk(cities, roadMap, hopeDistance, startCity)
    result.sort()
    if result:
        print("\n".join(map(str, result)))
    else:
        print(-1)


def djk(cities, roadMap, hopeDistance, startCity):
    routeMemory = [(0, startCity)]
    visited = [math.inf for _ in range(cities + 1)]
    visited[startCity] = 0  # 출발지점은 항상 0으로 한다
    result = []

    while routeMemory:
        nowDist, nowCity = heapq.heappop(routeMemory)
        if visited[nowCity] < nowDist:
            continue

        visited[nowCity] = nowDist

        if nowDist == hopeDistance:
            result.append(nowCity)
            continue

        for next in roadMap[nowCity]:
            nextDist = nowDist + 1
            heapq.heappush(routeMemory, (nextDist, next))

    return result


solution()
