import sys


def solution(K, N, lines):
    max_line = max(lines)
    min_line = 1
    mid_line = (max_line + min_line) // 2 + 1
    while max_line >= min_line:
        result = sum(map(lambda length: length // mid_line, lines))
        if result < N:
            max_line = mid_line - 1
            mid_line = (min_line + max_line) // 2
        if result >= N:
            min_line = mid_line + 1
            mid_line = (max_line + min_line) // 2
    print(mid_line)


K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]

solution(K, N, lines)
