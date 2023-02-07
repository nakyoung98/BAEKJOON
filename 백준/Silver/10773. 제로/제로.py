import sys

K = int(sys.stdin.readline())

stack = []

sum = 0
for _ in range(K):
    this = int(sys.stdin.readline())
    if this != 0:
        stack.append(this)
        sum += this
    else:
        sum -= stack.pop()

print(sum)

    