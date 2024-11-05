from collections import deque

def solution(info, edges):
    # 2차원 배열 트리 17*17이므로 크지 않음
    tree = [[-1] * len(info) for _ in range(len(info))]
    # 0: 양, 1: 늑대
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        
        tree[parent][child] = info[child]
        
    max_sheep = 1
    stack = deque([(0, 1, 0,set([0]))]) # index, sheep, wolf, 방문한 모든 자식 노드
    while stack:
        cur_idx, cur_sheep, cur_wolf, possible_nodes = stack.pop()
        possible_nodes.remove(cur_idx)
        
        for i in range(len(info)):
            child = tree[cur_idx][i] 
            if child == -1: # 자식관계아니면 나가라
                continue
            else:
                possible_nodes.add(i)
        
        for possible_node in possible_nodes:
            node_info = info[possible_node] 
            if node_info == 0: # 양이면
                stack.append((possible_node, cur_sheep+1, cur_wolf,possible_nodes.copy()))
            elif node_info == 1: #늑대면
                if cur_wolf + 1 < cur_sheep:
                    stack.append((possible_node, cur_sheep, cur_wolf+1, possible_nodes.copy()))
        if max_sheep < cur_sheep:
            max_sheep = cur_sheep
                        
    
    return max_sheep

