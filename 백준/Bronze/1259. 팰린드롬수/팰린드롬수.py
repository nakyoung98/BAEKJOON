import sys

number = sys.stdin.readline()[:-1]

while number != "0":
    isBreak = False

    for i in range(int(len(number)/2)):
        if number[i] != number[-(i+1)]:
            print("no")
            isBreak = True
            break
        
    if isBreak == False:
        print("yes")

    number = sys.stdin.readline()[:-1]

