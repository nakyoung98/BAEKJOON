import sys
'''
[입력]
1. N: 데이터 개수 (1~50000)

3초이므로 3억번까지 가능
N^2 불가
=> NlogN까지 가능
'''

# 반복문에 의한 (O(N))
def solution(N):    
    # 해싱을 위한 딕셔너리 사용
    files = {}
    
    # O(N)
    for _ in range(N):
    # 데이터 저장 O(1)
        file = sys.stdin.readline().rstrip().split('.')
        extension = file[1]
        
        if files.get(extension) == None :
            files[extension] = 1
        else:
            files[extension] += 1
        
    #O(N)
    return '\n'.join(f'{k} {v}' for k, v in sorted(files.items()))
        

N = int(sys.stdin.readline())
print(solution(N))