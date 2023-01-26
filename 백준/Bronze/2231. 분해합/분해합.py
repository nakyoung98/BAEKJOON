import sys

number = sys.stdin.readline()[:-1]
# number = input()

origin = int(number) - 9*len(number)

number = int(number)

if origin <= 0:
    origin = 1

while origin != number :

    strOrigin = str(origin)

    sum = 0
    for i in range(len(strOrigin)):
        sum += int(strOrigin[i])
    
    check = origin + sum

    if number - check == 0:
        print(origin)
        break

    origin += 1

if origin == number:
    print(0)