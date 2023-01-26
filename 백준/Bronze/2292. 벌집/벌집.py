import sys

N = int(sys.stdin.readline())

if N-1 == 0:
    print(1)
else:
    N = N-1
    
    room = 1
    while True:
        N -= 6*room
        if N > 0:
            room += 1
        else:
            break

    print(room+1)