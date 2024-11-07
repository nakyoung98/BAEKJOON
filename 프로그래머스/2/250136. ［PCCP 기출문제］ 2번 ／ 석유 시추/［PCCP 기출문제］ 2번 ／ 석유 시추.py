from collections import deque

d = [(-1,0),(1,0),(0,-1),(0,1)]

sail_idx = 2
sails = {}
def solution(land):
    max_result = 0
    for c in range(len(land[0])):
        sail_set = set()
        result = 0
        for r in range(len(land)):
            dfs(r,c,land)
            if land[r][c] > 1: #석유가 있는 땅이면
                sail_set.add(land[r][c]) #이 석유 지나간다고 기록해놓기
        for sail in sail_set:
            result += sails[sail]
        if result > max_result:
            max_result = result
        
    return max_result

def dfs(r, c, land):
    if land[r][c] != 1: #방문하지 않은 석유가 없는 땅
        return

    stack = deque([(r,c)])
    result = 0
    
    global sail_idx
    
    while stack:
        cur_r, cur_c = stack.pop()
        if land[cur_r][cur_c] != 1: # 이미 방문했었다면
            continue
            
        land[cur_r][cur_c] = sail_idx
        result += 1
        
        global d
        for dr,dc in d:
            next_r = cur_r + dr
            next_c = cur_c + dc
            
            if 0<= next_r <len(land) and 0<= next_c < len(land[0]) and land[next_r][next_c] == 1: # 갈 수 있는 석유가 있으면
                stack.append((next_r, next_c))  
    
    sails.setdefault(sail_idx, result)
    sail_idx += 1
    
    return