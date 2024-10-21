import math
import heapq


def solution(n, s, a, b, fares):
    routes = [[math.inf if c != r else 0 for c in range(n + 1)] for r in range(n + 1)]

    for fare in fares:
        node1 = fare[0]
        node2 = fare[1]
        fee = fare[2]

        routes[node1][node2], routes[node2][node1] = fee, fee

    dijk(n, s, routes)
    dijk(n, a, routes)
    dijk(n, b, routes)


def dijk(node_count, start, routes):
    result = [math.inf] * (node_count + 1)
    waits = [(0, start)]

    while waits:
        cur_dist, cur_node = heapq.heappop(waits)
        print(waits)
        result[cur_node] = cur_dist

        # 현재 위치에서 갈 수 있는 거리 얻기
        for next_node in range(1, node_count + 1):
            if result[next_node] == math.inf:
                # heapq에 다음 경로까지 거리들 추가하기
                next_dist = cur_dist + routes[cur_node][next_node]
                heapq.heappush(waits, (next_dist, next_node))

    print(result)


solution(
    6,
    4,
    6,
    2,
    [
        [4, 1, 10],
        [3, 5, 24],
        [5, 6, 2],
        [3, 1, 41],
        [5, 1, 24],
        [4, 6, 50],
        [2, 4, 66],
        [2, 3, 22],
        [1, 6, 25],
    ],
)
