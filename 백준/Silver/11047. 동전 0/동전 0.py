import sys

N,price = map(int,sys.stdin.readline().split())

value = 0
values = []

for _ in range(N):
    value = int(sys.stdin.readline())
    values.append(value)

values.reverse()

total = 0

while price != 0:
    div = int(price / values[0])

    if div < 1:
        values.pop(0)
        if len(values) == 0:
            break
    else:
        total += div
        price -= div * values[0]
        values.pop(0)
        if len(values) == 0:
            break

print(total)    