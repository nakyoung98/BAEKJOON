import sys
 
N = int(sys.stdin.readline())
# N = int(input())

numbers = [0 for _ in range(10001)]
for _ in range(N):
    i = int(sys.stdin.readline())
    # i = int(input())
    numbers[i] += 1

for i in range(10001):
    for _ in range(numbers[i]):
        print(i)
