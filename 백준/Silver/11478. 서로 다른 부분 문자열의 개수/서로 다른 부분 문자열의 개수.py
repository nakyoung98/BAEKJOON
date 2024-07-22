import sys

'''
부분문자열

두개의 반복문 중첩이 필요
최소 O(N^2)

데이터 1000
반복 제외, 데이터 저장에서 O(N)되면 안됨

[주의]
일반 배열 사용 시, 탐색에 O(N)이 걸린다고 함
따라서 dict(해시) 사용
'''

def solution(string):
    sets = {}

    #O(N)
    for left in range(len(string)):
        #O(N-left)
        for right in range(left,len(string)):
            partString = string[left:right+1]
            
            #O(1)
            if partString not in sets:
                sets[partString] = 0
            
    return len(sets)


string = sys.stdin.readline().rstrip()
print(solution(string))