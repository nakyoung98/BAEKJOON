import sys

N, M = map(int, sys.stdin.readline().split())
Trees = list(map(int, sys.stdin.readline().split()))

# H 값 자체를 이진 탐색으로 정하자.
start = 0
end = max(Trees)

result = start

while end >= start:

    mid = (start + end) // 2

    total = 0

    for tree in Trees:
        if mid < tree:
            total += (tree - mid)
    
    if  total >= M :
        result = mid
        start = mid + 1

    else:
        end = mid - 1
    
print(result)