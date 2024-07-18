import sys


def code(twoDArray, i, j, x, y):
    result = 0

    for row in range(i, x + 1):
        result += sum(twoDArray[row][j : y + 1])

    return result


r, c = map(int, sys.stdin.readline().split())
twoDArray = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
k = int(sys.stdin.readline())

for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())

    print(code(twoDArray, i - 1, j - 1, x - 1, y - 1))
