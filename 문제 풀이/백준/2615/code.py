import sys

BOUND = -1
checkerBoard = [[BOUND] * 21 for _ in range(21)]


def solution():
    for r in range(1, 20):
        for c in range(1, 20):
            if checkerBoard[r][c] != 0:
                result = isOmok(r, c)

                if result == 0:
                    return [checkerBoard[r][c], r + 4, c - 4]
                elif result > 0:
                    return [checkerBoard[r][c], r, c]
    return [0]


def isOmok(nowR, nowC):
    directions = [
        (lambda i: nowR + i, lambda i: nowC - i),  # 좌하
        (lambda i: nowR + i, lambda i: nowC),  # 하
        (lambda i: nowR + i, lambda i: nowC + i),  # 우하
        (lambda i: nowR, lambda i: nowC + i),  # 우
    ]

    for i in range(len(directions)):
        if searchOmok(nowR, nowC, directions[i][0], directions[i][1]):
            return i

    return -1


def searchOmok(nowR, nowC, newRFunc, newCFunc):
    color = checkerBoard[nowR][nowC]
    count = 1

    for i in range(1, 5):
        newR, newC = newRFunc(i), newCFunc(i)
        if checkerBoard[newR][newC] != color:
            return False
        count += 1

    # 정확히 5개이고, 양쪽 끝이 같은 색이 아닐 때 (육목 방지)
    return (
        count == 5
        and checkerBoard[newRFunc(5)][newCFunc(5)] != color
        and checkerBoard[newRFunc(-1)][newCFunc(-1)] != color
    )


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
