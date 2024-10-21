import sys
import heapq
import math

input = sys.stdin.readline

N = int(input())


def solution(N):
    rooms = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    changes = [[math.inf] * N for _ in range(N)]
    changes[0][0] = 0
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 구성 (changes, posy,posx)
    djk = [(0, 0, 0)]
    # 모든 room은 방문 가능
    while djk:
        nowChanges, nowPosY, nowPosX = heapq.heappop(djk)

        if nowPosY == N - 1 and nowPosX == N - 1:  # 맨 끝에 도달하면 종료
            return changes[nowPosY][nowPosX]

        for dy, dx in d:
            nextPosY = nowPosY + dy
            nextPosX = nowPosX + dx

            # 범위를 벗어나면 종료
            if (nextPosY >= N or nextPosY < 0) or (nextPosX >= N or nextPosX < 0):
                continue

            #  다음 방이 검정 방이라면 changes +1,
            nextChanges = nowChanges + (1 if rooms[nextPosY][nextPosX] == 0 else 0)

            # 미방문한 다음 노드 후보를 탐색
            if nextChanges < changes[nextPosY][nextPosX]:
                changes[nextPosY][nextPosX] = nextChanges
                heapq.heappush(djk, (nextChanges, nextPosY, nextPosX))


print(solution(N))
