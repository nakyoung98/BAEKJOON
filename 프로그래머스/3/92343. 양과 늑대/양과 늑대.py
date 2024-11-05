from collections import deque

def solution(info, edges):
    # 2차원 배열 트리 17*17이므로 크지 않음
    tree = [[] for _ in range(len(info))]
    sheep_count = info.count(0)
    # 0: 양, 1: 늑대
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        
        tree[parent].append(child)
        
    max_sheep = 1
    stack = deque([(0, 1, 0,set([0]))]) # index, sheep, wolf, 방문한 모든 자식 노드
    while stack:
        cur_idx, cur_sheep, cur_wolf, possible_nodes = stack.pop()
                
        next_possible_nodes = possible_nodes.copy()
        next_possible_nodes.remove(cur_idx)
        
        next_possible_nodes.update(tree[cur_idx]) 
        
        for possible_node in next_possible_nodes:
            node_info = info[possible_node] 
            if node_info == 0: # 양이면
                stack.append((possible_node, cur_sheep+1, cur_wolf,next_possible_nodes))
            elif node_info == 1: #늑대면
                if cur_wolf + 1 < cur_sheep:
                    stack.append((possible_node, cur_sheep, cur_wolf+1, next_possible_nodes))
        if max_sheep < cur_sheep:
            max_sheep = cur_sheep
        if max_sheep == sheep_count:
            break
                        
    
    return max_sheep

