import sys

N = int(sys.stdin.readline())

cards = list(map(int,sys.stdin.readline().split()))

lines = [1]

for i in range(1,N):
    lines.insert(i-cards[i],i+1)

print(' '.join(map(str,lines)))