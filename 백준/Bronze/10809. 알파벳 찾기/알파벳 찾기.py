import sys

S = sys.stdin.readline().rstrip()
letters = [-1 for _ in range(26)]


for i in range(len(S)):
    letterToIndex = ord(S[i])-97
    
    if letters[letterToIndex] == -1:
        letters[letterToIndex] = i

print(*letters)
