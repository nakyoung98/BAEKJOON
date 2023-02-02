import sys

N = int(sys.stdin.readline())

words = set()

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    words.add(word)

words = list(words)

wordList = []

for i in range(len(words)):
    wordList.append((len(words[i]),words[i]))

wordList.sort()

for lenWord, word in wordList:
    print(word)
