import sys

N = int(sys.stdin.readline())


def buildArray(N):
    array = list(map(int, sys.stdin.readline().split()))
    newArray = []
    for idx, value in enumerate(array):
        newArray.append([value, idx])
    return newArray


def solution(N):
    numbersWithIndex = buildArray(N)
    numbersWithIndex.sort(key=lambda x: x[0])

    lastIdx = -1
    lastNum = None
    for i in range(len(numbersWithIndex)):
        # 이전 숫자랑 다른 숫자면
        ## 마지막 숫자를 대체
        ## idx += 1
        if lastNum != numbersWithIndex[i][0]:
            lastNum = numbersWithIndex[i][0]
            lastIdx += 1

        # idx 값으로 대체
        numbersWithIndex[i][0] = lastIdx

    # 순서 원복
    numbersWithIndex.sort(key=lambda x: x[1])

    print(" ".join(str(x[0]) for x in numbersWithIndex))


solution(N)
