import sys
from enum import Enum

input = sys.stdin.readline


class Direction(Enum):
    L = (-1, 0)
    R = (1, 0)
    U = (0, -1)
    D = (0, 1)


class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # 새 위치 객체 반환
    def getNext(self, direction: Direction):
        dx, dy = direction.value
        return Position(self.x + dx, self.y + dy)


def get_row(is_border):
    if is_border:
        return [-1] * 7
    return [-1] + list(map(int, input().split())) + [-1]


def solution():
    board = [get_row(i in [0, 6]) for i in range(7)]

    result = set()

    for r in range(1, 6):
        for c in range(1, 6):
            pos = Position(r, c)
            recurse(board, pos, "", result)

    print(len(result))


def recurse(board, now: Position, currentNumber: str, result: set):
    # boundary로 진입 (실패)
    if board[now.x][now.y] == -1:
        return

    # 현재 숫자 추가
    currentNumber += str(board[now.y][now.x])

    # 숫자 완성 (성공)
    if len(currentNumber) >= 6:
        result.add(currentNumber)
        return

    # 상하좌우로 이동 (새로운 숫자 탐색)
    recurse(board, now.getNext(Direction.L), currentNumber, result)
    recurse(board, now.getNext(Direction.R), currentNumber, result)
    recurse(board, now.getNext(Direction.U), currentNumber, result)
    recurse(board, now.getNext(Direction.D), currentNumber, result)


solution()
