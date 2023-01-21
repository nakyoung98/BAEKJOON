import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

result = str(A*B*C)
numbers = [0 for _ in range(10)]

for letter in result:
    numbers[int(letter)] += 1

for number in numbers:
    print(number)
