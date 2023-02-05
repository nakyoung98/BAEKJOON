import sys

N = int(sys.stdin.readline())

for i in range(N):
    letters = [0 for _ in range(26)]

    line = sys.stdin.readline().rstrip()

    for letter in line:
        if letter != ' ':
            letters[ord(letter)-97] += 1

    max = letters[0]
    maxIndex = 0
    isOne = True

    for j in range(1,26):
        if max < letters[j]:
            max = letters[j]
            maxIndex = j
            isOne = True
        elif max == letters[j]:
            isOne = False
    
    if isOne == True:
        print(chr(maxIndex+97))
    else:
        print('?')
