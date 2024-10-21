import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


R, C = map(int, input().split())


def solution(R, C):
    places = [list(input().rstrip()) for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]

    result = {"sheep": 0, "wolf": 0}

    for r in range(R):
        for c in range(C):
            sheep, wolf = visit(r, c, R, C, visited, places)
            if sheep > wolf:
                result["sheep"] += sheep
            else:
                result["wolf"] += wolf

    return result["sheep"], result["wolf"]


def visit(r, c, R, C, visited, places):
    # 범위를 벗어나면 돌아가기
    if r < 0 or r >= R or c < 0 or c >= C:
        return 0, 0

    # 방문했던 곳이면 돌아가기
    if visited[r][c] == 1:
        return 0, 0

    # 울타리면 탐색 종료
    if places[r][c] == "#":
        return 0, 0

    # 방문기록
    visited[r][c] = 1

    sheep, wolf = (
        (1, 0) if places[r][c] == "k" else (0, 1) if places[r][c] == "v" else (0, 0)
    )

    # 전방위 탐색
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in d:
        s, w = visit(r + dx, c + dy, R, C, visited, places)
        sheep += s
        wolf += w

    # 탐색 끝나면 (주변이 다 1이라는 것이니, 숫자 센 결과 정리)
    # 양수: 양, 음수: 늑대가 살아남았다는 의미
    return sheep, wolf


print(*solution(R, C))
