import sys
N, M = map(int,sys.stdin.readline().split())
boxes = [i for i in range(1,N+1)]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())

    boxes[i-1],boxes[j-1] = boxes[j-1],boxes[i-1]

print(*boxes)
