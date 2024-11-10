def solution(n, computers):
    computer_reps = [i for i in range(n)]

    for r in range(len(computers)):
        for c in range(len(computers[0])):
            if computers[r][c] == 1:
                union(computer_reps, r, c)

    result = set()
    for i in range(n):
        result.add(find(computer_reps,i))
        
    return len(result)
    
def find(computers, com):
    # com 번호의 진짜 대표를 찾을 때까지 계속 따라갑니다
    while computers[com] != com:
        com = computers[com]
    return com
    

def union(computers,com1, com2):
    
    rep1 = find(computers,com1)
    rep2 = find(computers,com2)
    
    computers[rep1] = rep2
    
    
    
    