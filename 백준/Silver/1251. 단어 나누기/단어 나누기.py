import sys

word = sys.stdin.readline().rstrip()
words = []

for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        first = word[:i][::-1]
        second = word[i:j][::-1]
        last = word[j:][::-1]

        newWord = first + second + last
        # print(newWord, "first {0} second {1} last {2}".format(first, second, last))
        words.append(newWord)

words.sort()
print(words[0])