import sys
import math
import heapq

input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def performDjk(maps, size):
    visitQueue = [(maps[0][0], 0, 0)]
    # 다익스트라 지도 구성
    djk = [[math.inf] * size for _ in range(size)]
    # 다익스트라 초기값
    djk[0][0] = maps[0][0]

    while visitQueue:
        # 최소힙 (무조건 항상 최소값을 꺼냄)
        nowRupee, nowR, nowC = heapq.heappop(visitQueue)

        # 끝에 도달했으면 종료
        if nowR == size - 1 and nowC == size - 1:
            return nowRupee

        # 갈 수 있는 방향 탐색
        for dr, dc in d:
            # 다음 위치
            nextR = nowR + dr
            nextC = nowC + dc

            # 다음 위치가 범위 밖이면 포기
            if (nextR < 0 or nextR >= size) or (nextC < 0 or nextC >= size):
                continue

            nextRupee = maps[nextR][nextC]
            # 다음 위치에 이동시 다음위치까지의 총 경로 cost
            nextRupeeSum = nowRupee + nextRupee
            # 이미 존재하는 값보다 작아야 이동할 가치가 있음
            if nextRupeeSum >= djk[nextR][nextC]:
                continue

            # 다음 위치 값 더해놓기
            djk[nextR][nextC] = nextRupeeSum
            # 최소합이 되어 다시 최소부터 꺼낼 수 있도록 정리
            heapq.heappush(visitQueue, (nextRupeeSum, nextR, nextC))


count = 1

while True:
    size = int(input())
    if size == 0:
        break

    # 지도 구성
    maps = [list(map(int, input().split())) for _ in range(size)]

    result = performDjk(maps, size)
    print(f"Problem {count}: {result}")
    count += 1
