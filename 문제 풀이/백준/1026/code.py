import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))


def solution(N, A, B):
    reverseSortedA = sorted(A, reverse=True)
    sortedB = sorted(B)

    S = 0

    for i in range(N):
        S += reverseSortedA[i] * sortedB[i]

    print(S)


solution(N, A, B)
