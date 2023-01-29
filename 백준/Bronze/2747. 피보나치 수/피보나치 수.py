import sys

N = int(sys.stdin.readline())


f = [0,1]


for i in range(2,N+1):
    f.append(f[i-2]+f[i-1])

print(f[-1])
