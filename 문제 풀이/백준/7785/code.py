import sys

def solution(N):
    # 이름 검색 속도 향상을 위해 dict (해시) 사용
    logs= {}
    
    for _ in range(N):
        name, info = sys.stdin.readline().split()
        
        # 입 기록
        if info == "enter":
            logs[name] = 0
        
        # 출 기록
        if info == "leave":
            del(logs[name])
        
    # 이름을 역순으로 정렬하여 한 줄씩 반환
    return '\n'.join(sorted(logs.keys(), reverse=True))
        
        

N = int(sys.stdin.readline())
print(solution(N))
