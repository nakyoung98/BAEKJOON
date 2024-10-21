import math
"""
다익스트라
"""

def solution(n, s, a, b, fares):
    start = s
    a_end = a
    b_end = b
    
    # 요금표만들기 (1~n번까지)
    routes = [[math.inf] * (n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        routes[i][i] = 0
    
    for fare in fares:
        node1 = fare[0]
        node2 = fare[1]
        fee = fare[2]
        
        routes[node1][node2] = fee
        routes[node2][node1] = fee
        
    # 전체에서 출발하고 전체 노드에 도착하는 각 요금 구하기
    for m in range(1,n+1):
        for s in range(1,n+1):
            for e in range(1,n+1):
                if routes[s][m] + routes[m][e] <= routes[s][e]:
                    routes[s][e] = routes[s][m] + routes[m][e]
                    
    # 최소 요금 구하기
    # 중간 경유지까지의 요금 + m to a + m to b 요금이 최소인 경우 구하기
    min_fee = routes[start][a_end] + routes[start][b_end] # 초기값으로, 각자 알아서 갔을 때 비용
    for m in range(1,n+1):
        if routes[start][m] + routes[m][a_end] + routes[m][b_end] < min_fee:
            min_fee = routes[start][m] + routes[m][a_end] + routes[m][b_end]
        
    return min_fee