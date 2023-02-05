import sys
N = int(sys.stdin.readline())

stack = []
size = -1

for _ in range(N):
    command = list(map(str,sys.stdin.readline().split()))

    if command[0] == 'push':
        stack.append(int(command[1]))
        size += 1
    
    elif command[0] == 'top':
        if size == -1:
            print(-1)
        else:
            print(stack[size])

    elif command[0] == 'pop':
        if size>-1:
            print(stack.pop())
            size -= 1
        else:
            print(-1)

    elif command[0] == 'empty':
        if size == -1:
            print(1)
        else:
            print(0)

    elif command[0] == 'size':
        print(size+1)