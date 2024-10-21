import sys

input = sys.stdin.readline

T = int(input())


def code(T):
    for _ in range(T):
        A, B = map(int, input().split())
        result = solution(A, B)

        print(10 * result)


def solution(A, B):
    # 힙 개념 활용
    AandParents = getHeapParents(A)
    BandParents = getHeapParents(B)

    i = -1
    mostParent = 1
    while i >= -len(AandParents) and i >= -len(BandParents):

        # 조상이 분기되면 종료
        if AandParents[i] != BandParents[i]:
            break

        # 공통조상 업데이트
        mostParent = AandParents[i]

        i -= 1

    return mostParent


def getHeapParents(N):
    NandParents = []

    while True:
        NandParents.append(N)

        if N == 1:
            break

        N = N // 2

    return NandParents


code(T)
