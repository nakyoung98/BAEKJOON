import sys
import math

input = sys.stdin.readline


def solution(N):
    return math.floor(math.log2(N) + 8 + 2)


N = int(input())
print(solution(N))
