from collections import deque

def solution(user_id, banned_id):
    result = set()
    
    queue = deque([(0, set())])
    while queue:
        cur_banned_id_idx, cur_result = queue.popleft()
        
        
        # 결과 추가 부
        if cur_banned_id_idx == len(banned_id):
            #print(cur_banned_id, cur_result)
            candidate = sorted(list(cur_result))
            cur_result_string = ''.join(candidate)
            result.add(cur_result_string)
            continue
            
        cur_banned_id = banned_id[cur_banned_id_idx]
        
        # 탐색 추가 부
        for user in user_id:
            if len(user) != len(cur_banned_id): #길이가 같지 않을 경우 아예 대상에 추가하지 않음
                continue
            
            isSame = True
            for i in range(len(cur_banned_id)):
                #print(cur_banned_id[i], user[i])
                if cur_banned_id[i] == "*": # *인 경우에는 검사하지 않음
                    continue
                if cur_banned_id[i] != user[i]: #다른 부분이 나오면 같지 않은 것으로 취급
                    isSame = False
                    break
            
            if isSame and user not in cur_result: #현재 dict에 추가된적 없고, 매핑이 가능한 유저인 경우만 추가
                new_array = cur_result.copy()
                new_array.add(user)
                #print((cur_banned_id_idx + 1, new_array))
                queue.append((cur_banned_id_idx + 1, new_array))
    
    print(result)
    return len(result)