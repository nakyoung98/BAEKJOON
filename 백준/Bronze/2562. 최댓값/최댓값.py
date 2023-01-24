import sys

max = int(sys.stdin.readline())
maxIndex = 0

for i in range(1,9):
    number = int(sys.stdin.readline())
    if max < number:
        max = number
        maxIndex = i

print(max)
print(maxIndex+1)