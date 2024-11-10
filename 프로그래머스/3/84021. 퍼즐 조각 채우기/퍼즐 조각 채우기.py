from collections import deque

d = [(-1,0),(1,0),(0,-1),(0,1)]
def solution(game_board, table):
    answer = 0
    
    # 블록 찾기
    # 1. 보드에서 구멍찾기
    holes = find_zone(game_board,0)
    # print(holes)
                
    # 2. 테이블에서 블록찾기
    blocks = find_zone(table, 1)
    #print(blocks)

    for hole in holes:
        # print("구멍",hole)
        # print("남은 블록", blocks)
        hole_r = len(hole)
        hole_c = len(hole[0])
        for block in blocks:
            origin_block = block
            hasBlock = False
            for i in range(4):
                block = rotate(block)
                block_r = len(block)
                block_c = len(block[0])
                if hole_r == block_r and hole_c == block_c:
                    isSame = True
                    
#                     print("블록 비교")
#                     for r in range(block_r):
#                         for c in range(block_c):
#                             print(hole[r][c], end='')
#                         print()
                        
#                     print("==")
#                     for r in range(block_r):
#                         for c in range(block_c):
#                             print(block[r][c], end='')
#                         print()
                                
                    for r in range(block_r):
                        for c in range(block_c):
                            if hole[r][c] ^ block[r][c] == 0:
                                isSame = False

                    if isSame:
                        # print("성공")
                        block_count = 0
                        for r in range(block_r):
                            for c in range(block_c):
                                print(hole[r][c], end='')
                                if block[r][c] == 1:
                                    block_count += 1
                            # print()

                        answer += block_count
                        # print("블록 개수", block_count)
                        blocks.remove(origin_block)
                        hasBlock = True
                        break
                        
            if hasBlock:
                break
            
    # blocks holes 대조는 xor 로 하면됨 

    return answer

def rotate(block): #90도 회전
    origin_r = len(block)
    origin_c = len(block[0])
    
    new_block = [[0]*origin_r for _ in range(origin_c)]
    
    for r in range(origin_r):
        for c in range(origin_c):
            new_block[c][origin_r-r-1] = block[r][c]
            
    return new_block

def find_zone(origin_map, find_number):
    duplicate_map = [[origin_map[r][c] for c in range(len(origin_map[0]))] for r in range(len(origin_map))]
    zones = []
    for r in range(len(duplicate_map)):
        for c in range(len(duplicate_map[0])):
            if not duplicate_map[r][c] == find_number:
                continue
            
            min_r, min_c = r, c
            max_r, max_c = r, c
            queue = deque([(r,c)])
            while queue:
                cur_r, cur_c = queue.popleft()
                
                if not duplicate_map[cur_r][cur_c] == find_number:
                    continue
                duplicate_map[cur_r][cur_c] = -1 # 방문의 의미
                
                if min_r > cur_r:
                    min_r = cur_r
                if min_c > cur_c:
                    min_c = cur_c
                if max_r < cur_r:
                    max_r = cur_r
                if max_c < cur_c:
                    max_c = cur_c
                
                for dr, dc in d:
                    next_r = cur_r + dr
                    next_c = cur_c + dc
                    if not (0<=next_r<len(duplicate_map) and 0<=next_c<len(duplicate_map[0])):
                        continue
                    if duplicate_map[next_r][next_c] != find_number:
                        continue
                    
                    queue.append((next_r,next_c))
                
            zone = [row[min_c:max_c+1] for row in origin_map[min_r:max_r+1]]
            zones.append(zone)
            
    return zones