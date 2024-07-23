import sys

BOUND = -1
checkerBoard = [[BOUND] * 21 for _ in range(21)]


def solution():
    for r in range(1, 20):
        for c in range(1, 20):
            if checkerBoard[r][c] != 0:
                result = isOmok(r, c)
                if result:
                    return [checkerBoard[r][c], result[0], result[1]]
    return [0]


def isOmok(nowR, nowC):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # 우  # 하  # 우하  # 우상
    for dr, dc in directions:
        if searchOmok(nowR, nowC, dr, dc):
            # 가장 왼쪽 또는 가장 위의 돌 위치 반환
            if dr <= 0 and dc > 0:  # 우, 우상
                return nowR, nowC
            elif dr > 0 and dc == 0:  # 하
                return nowR, nowC
            elif dr > 0 and dc > 0:  # 우하
                return nowR, nowC
    return None


def searchOmok(r, c, dr, dc):
    color = checkerBoard[r][c]
    count = 1

    # 정방향 확인
    for i in range(1, 5):
        nr, nc = r + dr * i, c + dc * i
        if checkerBoard[nr][nc] != color:
            return False
        count += 1

    # 육목 방지
    if checkerBoard[r + dr * 5][c + dc * 5] == color:
        return False
    if checkerBoard[r - dr][c - dc] == color:
        return False

    return count == 5


def setCheckerBoard():
    for i in range(1, 20):
        checkerBoard[i][1:20] = list(map(int, sys.stdin.readline().split()))


setCheckerBoard()
result = solution()

if len(result) == 1:
    print(*result)
else:
    print(result[0])
    print(result[1], result[2])
