import sys

A, B, V = map(int, sys.stdin.readline().split())
# A, B, V = 2,1,5

if A == V:
    print("1")
else:
    m = 1
    result = (V-A)/(A-B)
    if result - int(result) > 0:
        m += 1+int(result)
    else:
        m+= int(result)

    print(m)
