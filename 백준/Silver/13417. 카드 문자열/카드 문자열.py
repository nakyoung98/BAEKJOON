import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def solution(N):
    letters = input().rstrip().split()
    word = deque([letters[0]])
    for i in range(1, len(letters)):
        # 맨 앞 글자보다 작은 글자면 앞으로
        if ord(word[0]) >= ord(letters[i]):
            word.appendleft(letters[i])
        # 아니면 뒤로
        else:
            word.append(letters[i])

    return "".join(word)


def code(T):
    for _ in range(T):
        N = int(input())
        result = solution(N)
        print(result)


code(T)
