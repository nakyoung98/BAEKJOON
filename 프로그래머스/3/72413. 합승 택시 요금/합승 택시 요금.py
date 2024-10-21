import math
import heapq

def solution(n, s, a, b, fares):
    routes = [[math.inf if c != r else 0 for c in range(n+1)] for r in range(n+1)]

    for fare in fares:
        node1 = fare[0]
        node2 = fare[1]
        fee = fare[2]
        
        routes[node1][node2], routes[node2][node1] = fee, fee
    
    s_dijk = dijk(n, s, routes)
    a_dijk = dijk(n, a, routes)
    b_dijk = dijk(n, b, routes)
    
    # 경유지 기반 값 계산
    min_fee = a_dijk[s] + b_dijk[s] # 기본값: 각자 따로 갔을 때
    for via in range(1,n+1):
        if min_fee > s_dijk[via] + a_dijk[via] + b_dijk[via]:
              min_fee = s_dijk[via] + a_dijk[via] + b_dijk[via]  
        
    return min_fee
        
    
def dijk(node_count, start, routes):
    result = [math.inf]*(node_count+1)
    waits = [(0,start)]
    
    while waits:
        cur_dist, cur_node = heapq.heappop(waits)
        
        # 가능 시, 최소값 갱신
        if result[cur_node] > cur_dist:
            result[cur_node] = cur_dist
        
        # 현재 위치에서 갈 수 있는 거리 얻기
        for next_node in range(1, node_count+1):
            if result[next_node] == math.inf:
                # heapq에 다음 경로까지 거리들 추가하기
                next_dist = cur_dist + routes[cur_node][next_node]
                if next_dist != math.inf:
                    heapq.heappush(waits, (next_dist, next_node))

    return result
            
            
        
        
    
        
        
