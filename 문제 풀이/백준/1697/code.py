import sys
from collections import deque

input = sys.stdin.readline


def solution():
    me, sister = map(int, input().split())
    visited = [0 for i in range(100001)]

    # 최단거리 탐색을 위해 bfs 사용
    # (내 위치, 현재까지 누적 이동 시간)
    queue = deque([(me, 0)])

    while queue:
        # 주변 우선 탐색
        nowMe, time = queue.popleft()

        # 범위를 벗어나서 이동할 수는 없으므로 무시
        if nowMe < 0 or nowMe > 100000:
            continue
        # 방문한 곳이면 무시
        if visited[nowMe] == 1:
            continue

        # 방문한 곳 표시
        visited[nowMe] = 1

        # 동생을 찾았을 경우 종료
        if nowMe == sister:
            return time

        # 갈 수 있는 방향으로 탐색
        queue.append((nowMe - 1, time + 1))
        queue.append((nowMe + 1, time + 1))
        queue.append((nowMe * 2, time + 1))


print(solution())
