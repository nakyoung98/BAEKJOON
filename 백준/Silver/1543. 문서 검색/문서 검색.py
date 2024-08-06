import sys

input = sys.stdin.readline


def solution():
    sentence = input().rstrip()
    findWord = input().rstrip()

    sentenceSplitByFindWord = sentence.split(findWord)
    return len(sentenceSplitByFindWord) - 1


print(solution())
