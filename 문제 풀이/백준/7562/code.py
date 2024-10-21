import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def solution(T):
    for _ in range(T):
        size = int(input())
        r, c = map(int, input().split())
        destR, destC = map(int, input().split())
        room = [[0] * size for _ in range(size)]
        result = floodFill(r, c, destR, destC, size, room)
        print(result)


def floodFill(r, c, destR, destC, size, room):
    # r,c, 이동횟수
    queue = deque([(r, c, 0)])

    while queue:
        # 담아놓은 장소 뽑기
        nowR, nowC, nowCount = queue.popleft()

        # 바운더리 넘어가면 패스
        if nowR < 0 or nowR >= size or nowC < 0 or nowC >= size:
            continue
        # 이미 온 곳이면 패스
        if room[nowR][nowC] == 1:
            continue

        # 이 곳이 찾는 곳이면 탐색 종료
        if nowR == destR and nowC == destC:
            return nowCount

        # 방문한 곳 표시
        room[nowR][nowC] = 1

        # 반복부
        # 이동 가능한 범위
        d = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
        for dr, dc in d:
            queue.append((nowR + dr, nowC + dc, nowCount + 1))


solution(T)
