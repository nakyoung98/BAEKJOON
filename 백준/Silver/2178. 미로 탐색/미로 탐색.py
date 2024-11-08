import sys
from collections import deque
import math

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
input = sys.stdin.readline

N, M = map(int, input().split())

# maps 만들기
maps = [[0] * (M + 1) for _ in range(N + 1)]
visits = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input().rstrip()
    for j in range(1, M + 1):
        maps[i][j] = int(row[j-1])

queue = deque([(1, 1, 1)])
min_result = math.inf

while queue:
    cur_r, cur_c, cur_count = queue.popleft()

    if visits[cur_r][cur_c] == 1:
      continue

    visits[cur_r][cur_c] = 1

    if cur_r == N and cur_c == M:
        if min_result > cur_count:
            min_result = cur_count
        continue

    for dr, dc in d:
        next_r = cur_r + dr
        next_c = cur_c + dc

        if not (1 <= next_r <= N and 1 <= next_c <= M):
            continue

        if maps[next_r][next_c] == 0:
            continue
          
        if visits[next_r][next_c] == 1:
            continue

        queue.append((next_r, next_c, cur_count + 1))

print(min_result)
