import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x, rCount, cCount, room):
    sheep, wolf = 0, 0
    stack = [(y, x)]

    # 울타리 하나 bfs 탐색
    while stack:
        y, x = stack.pop()

        # 현위치가 바운더리 밖 무시
        if y < 0 or y >= rCount or x < 0 or x >= cCount:
            continue

        state = room[y][x]

        # 울타리면 건너뛰기
        if state == "#":
            continue

        # 양 수 세기
        if state == "v":
            wolf += 1
        if state == "k":
            sheep += 1

        # 방문한 곳을 다시 방문할 수 없도록 #처리
        room[y][x] = "#"

        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in d:
            stack.append((y + dy, x + dx))

    return sheep if sheep > wolf else -wolf


def solution():
    R, C = map(int, input().split())
    room = [list(input().rstrip()) for _ in range(R)]
    sheep = 0
    wolf = 0

    for r in range(R):
        for c in range(C):
            result = bfs(r, c, R, C, room)
            if result > 0:
                sheep += result
            else:
                wolf -= result

    print(sheep, wolf)


solution()
