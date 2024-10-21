import sys

input = sys.stdin.readline

depth = int(input())


def solution(depth):
    visited = list(map(int, input().split()))
    visited.reverse()

    treeVisited = [0 for _ in range(2**depth - 1)]

    visit(0, treeVisited, visited, len(visited) - 1)

    # 결과 출력을 위한 매핑
    result = [
        " ".join(map(str, treeVisited[2**h - 1 : 2 ** (h + 1) - 1]))
        for h in range(depth)
    ]
    print("\n".join(result))


def visit(now, treeVisited, visited: list, max):
    if now > max:
        return

    # 왼쪽 자식 방문
    visit(2 * now + 1, treeVisited, visited, max)

    # 현재 노드 추가
    treeVisited[now] = visited.pop()

    # 오른쪽 자식 방문
    visit(2 * now + 2, treeVisited, visited, max)


solution(depth)
