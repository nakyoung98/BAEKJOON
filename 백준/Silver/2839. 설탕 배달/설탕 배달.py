import sys

N = int(sys.stdin.readline())

X = int(N/5)
Y = 0

while X >= 0:
    if (N-(5*X))%3 == 0:
        Y = int((N-5*X)/3)
        break

    X -= 1

if(X<0):
    print(-1)
else:
    print(X+Y)