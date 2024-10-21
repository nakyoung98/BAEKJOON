import sys
from collections import deque

input = sys.stdin.readline


def solution():
    # - : 옆 탐색
    # | : 아래 탐색
    R, C = map(int, input().split())
    floorMap = [list(map(str, input().rstrip().split())) for _ in range(R)]

    search(R, C, floorMap)


def search(R, C, floorMap):
    # 방문 체크
    visited = [[0] * C for _ in range(R)]
    # 탐색을 위한 queue
    # 구조(현재 내용,y,x)
    stack = [(floorMap[0][0], 0, 0)]

    visited += 1
    while stack:
        nowFloor, nowY, nowX = stack.pop()

        if visited[nowY][nowX] == 1:  # 이미 방문한 곳이면
            continue

        visited[nowY][nowX] = 1

        if nowY == R - 1 and nowX == C - 1:  # 끝까지 도달시 종료
            break

        if nowFloor == "|":
            # 더이상 아래로 갈 수 없으면 무시
            nextY, nextX = nowY + 1, nowX
            if nextY >= R:
                continue
            
            #만약 다음게 "-"면

            nextFloor = floorMap[nextY][nextX]
            stack.append((nextFloor, nextY, nextX))  # 세로 탐색
        elif nowFloor == "-":
            # 더이상 아래로 갈 수 없으면 무시
            nextY, nextX = nowY, nowX + 1
            if nextX >= C:
                continue

            nextFloor = floorMap[nextY][nextX]
            stack.append((nextFloor, nextY, nextX))  # 가로 탐색
            stack.append((floorMap[nowY][nowX + 1], nowY, nowX + 1))  # 가로 탐색
