import sys
from math import inf

input = sys.stdin.readline


def solution():
    studentCount, comparisonCount = map(int, input().split())
    # 가중치 관계 X, 단순히 관계성 설명 가능여부, inf를 사용하지 않음
    heightMap = [[0 for _ in range(studentCount + 1)] for _ in range(studentCount + 1)]

    for _ in range(comparisonCount):
        st1, st2 = map(int, input().split())
        # 단방향 그래프, 단순히 관계만을 알기위해 1로 정의
        heightMap[st1][st2] = 1

    # 플루이드 워셜 - 최단거리 갱신
    for viaSt in range(1, studentCount + 1):
        for startSt in range(1, studentCount + 1):
            for endSt in range(1, studentCount + 1):
                if heightMap[startSt][viaSt] and heightMap[viaSt][endSt]:
                    heightMap[startSt][endSt] = 1

    result = 0
    # 본인보다 큰 사람수(가로)와, 본인보다 작은 사람(세로) 수를 셈
    for me in range(1, studentCount + 1):
        # 본인보다 큰 사람 수
        bigger = heightMap[me].count(1)
        smaller = 0
        for i in range(1, studentCount + 1):
            smaller += heightMap[i][me]

        # 본인 기준 모두의 관계를 알고있다면
        if bigger + smaller + 1 == studentCount:
            result += 1

    print(result)


solution()
