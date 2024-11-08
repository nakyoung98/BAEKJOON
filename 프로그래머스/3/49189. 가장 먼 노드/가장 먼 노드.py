import heapq
import math

def solution(n, edge):
    answer = 0
    
    # 간선 맵 만들기
    maps = {i:set() for i in range(1,n+1)}
    for ed in edge:
        n1 = ed[0]
        n2 = ed[1]
        
        maps[n1].add(n2)
        maps[n2].add(n1)

    return dijk(n, maps)

def dijk(n, maps):
    distances = [math.inf]*(n+1)
    distances[0] = -1
    distances[1] = 0
    
    heap = [(1,0)] #(현 노드, 1번노드와의 거리)
    
    while heap:
        cur_node, cur_distance = heapq.heappop(heap)
        
        if distances[cur_node] < cur_distance:
            continue
        
        
        for next_node in maps[cur_node]:
            if distances[next_node] > cur_distance + 1:
                distances[next_node] = cur_distance + 1
                heapq.heappush(heap,(next_node,distances[next_node]))
    
    print(distances)
    max_distance = max(distances)
    return distances.count(max_distance)
    
    