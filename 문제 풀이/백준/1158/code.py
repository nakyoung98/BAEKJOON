import sys
from collections import deque


# 직접 인덱스를 순환하는 대신
# queue의 Head를 돌리면서 찾기 (O(K))
def solution(N, K):
    table = deque(i for i in range(1, N + 1))
    result = []

    for _ in range(N):
        table.rotate(-(K - 1))
        result.append(table.popleft())

    print(f'<{", ".join(map(str,result))}>')


N, K = map(int, sys.stdin.readline().split())
solution(N, K)
