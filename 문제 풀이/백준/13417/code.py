import sys

sys.setrecursionlimit(10000)

from collections import deque

input = sys.stdin.readline

T = int(input())


def recursion(idx, letters, word: deque, results):
    if idx == len(letters):
        results.append("".join(word))
        return

    # 다음 단어 추출
    now = letters[idx]

    # 재귀 실행
    # 앞에도 붙여보고
    word.append(now)
    recursion(idx + 1, letters, word, results)
    word.pop()

    # 뒤에도 붙여보고
    word.appendleft(now)
    recursion(idx + 1, letters, word, results)
    word.popleft()


def solution(N):
    results = []
    letters = input().rstrip().split()
    word = deque()
    recursion(0, letters, word, results)

    results.sort()
    return results[0]


def code(T):
    for _ in range(T):
        N = int(input())
        result = solution(N)
        print(result)


code(T)
