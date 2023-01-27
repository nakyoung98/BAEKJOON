import sys

N,K = map(int, sys.stdin.readline().split())

if N/2<K:
    K = N-K

numerator = 1
denominator = 1

for i in range(N,N-K,-1):
    numerator *= i

for i in range(1,K+1):
    denominator *= i

print(int(numerator/denominator))
