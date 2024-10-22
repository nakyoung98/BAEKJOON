from collections import deque

def solution(n, wires):
    tree = [[-1] * (n+1) for _ in range(n+1)]
    diffs = []
    
    for wire in wires:
        node1 = wire[0]
        node2 = wire[1]
        
        tree[node1][node2] = 0
        tree[node2][node1] = 0
    
    # 특정 wire가 없어졌을 때 양쪽 노드 개수 탐색하기
    for delete_wire in wires:
        # 방문한 노드 개수 (한쪽 트리의 노드 개수와 같음)
        visited = dfs(n, delete_wire, tree)
        
        # 두 트리의 노드 개수 차이 구해서 저장
        diff = abs(n - 2*visited)
        diffs.append(diff)
    
    # 최소 diff 값 구하기
    return min(diffs)
    
def dfs(n, delete_route, tree):
    # 1부터 시작함
    waits = deque([1])
    visited = [0] * (n+1)
    
    while waits:
        cur_node = waits.pop()
        visited[cur_node] = 1
        
        # 갈 수 있는 곳 탐색 - 끊어진 다리는 탐색 대상에서 제외
        for next_node in range(1, n+1):
            if visited[next_node] == 1:
                continue
                
            if tree[cur_node][next_node] == -1:
                continue
            
            if (cur_node == delete_route[0] and next_node == delete_route[1]) or (cur_node == delete_route[1] and next_node == delete_route[0]):
                continue
                        
            waits.append(next_node)
        
    return len(list(filter(lambda visit: visit == 1, visited)))
        
        
        