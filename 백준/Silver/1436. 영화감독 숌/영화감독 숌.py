import sys

N = int(sys.stdin.readline())

titles = []

number = 666

while len(titles)<N:
    if '666' in str(number) :
        titles.append(number)
    
    number += 1

print(titles[-1])