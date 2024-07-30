import sys

input = sys.stdin.readline
from collections import deque


N, M, K, X = map(int, input().split())

roadMap = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    # 인접 연결 리스트 생성
    roadMap[A].append(B)


def bfs():
    queue = deque([(0, X)])
    visited = [0] * (N + 1)
    result = []

    while queue:
        dist, city = queue.popleft()
        if visited[city] == 1:
            continue

        visited[city] = 1

        if dist == K:
            result.append(city)
            continue

        if dist > K:
            continue

        for next in roadMap[city]:
            queue.append((dist + 1, next))

    return result


result = bfs()
result.sort()

if result:
    print("\n".join(map(str, result)))
else:
    print(-1)
