import sys
from collections import deque


def solution(N, K):
    table = deque(i for i in range(1, N + 1))
    result = []

    for _ in range(N):
        table.rotate(-(K - 1))
        result.append(table.popleft())

    print(f'<{", ".join(map(str,result))}>')


N, K = map(int, sys.stdin.readline().split())
solution(N, K)
