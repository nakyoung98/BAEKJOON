import sys

N = int(sys.stdin.readline())

queue = []

for _ in range(N):
    command = sys.stdin.readline().rstrip()
    
    if "push" in command:
        A,B = map(str, command.split())
        queue.append(int(B))
        
    elif "pop" in command:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
            
    elif "size" in command:
        print(len(queue))
        
    elif "empty" in command:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
        
    elif "front" in command:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    
    elif "back" in command:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])