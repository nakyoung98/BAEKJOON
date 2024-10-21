import sys

input = sys.stdin.readline

N = int(input())


def solution(N):
    # set: 단어 중복 제거
    words = set()
    for _ in range(N):
        words.add(input().rstrip())

    # 정렬 조건
    ## 1. 문자 길이
    ## 2. 문자 사전순
    result = sorted(words, key=lambda x: (len(x), x))

    print("\n".join(result))


solution(N)
