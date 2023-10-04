import sys

N = int(sys.stdin.readline())
antenna = list(map(int,sys.stdin.readline().split()))
antenna.sort()

mid = 0
if N %2 == 0: # 짝수
    mid = N//2 - 1
else: # 홀수
    mid = N//2

print(antenna[mid])