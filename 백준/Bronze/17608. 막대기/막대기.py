import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    stack.append(int(sys.stdin.readline()))

result = []
pops = 0

for _ in range(len(stack)):
    # print('pops',pops)
    now = stack.pop()
    if  now > pops:
        # print('pop',now)
        result.append(now)
        pops = now
    # else:
    #     pops = now

print(len(result))