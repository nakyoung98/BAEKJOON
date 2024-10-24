def solution(n):
    answer = []
    H(n,1,3, answer)
    return answer

def H(n, x, y, answer):
    if n == 1:
        answer.append([x,y])
        return 
    
    H(n-1, x, 6-x-y,answer)
    answer.append([x,y])
    H(n-1, 6-x-y , y,answer)