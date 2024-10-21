import sys
from collections import deque

input = sys.stdin.readline

computers = int(input())
edges = int(input())

routeMap = [[] for _ in range(computers + 1)]

for _ in range(edges):
    computer1, computer2 = map(int, input().split())
    # 양방향 연결 리스트 만들기
    routeMap[computer1].append(computer2)
    routeMap[computer2].append(computer1)


def bfs():
    queue = deque([1])
    visited = [0] * (computers + 1)

    while queue:
        nowComputer = queue.popleft()

        # 방문했었으면 패스
        if visited[nowComputer] == 1:
            continue

        visited[nowComputer] = 1

        # 다음 갈 수 있는 곳 탐색
        for next in routeMap[nowComputer]:
            queue.append(next)

    # 방문한 친구들은 전부 바이러스에 걸렸음
    return visited


visitedResult = bfs()
# 모든 방문한 컴퓨터의 개수를 찾되 1번 컴퓨터 자기자신은 계산에서 빼야함
print(visitedResult.count(1) - 1)
