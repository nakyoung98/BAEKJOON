import sys
from math import inf
from collections import defaultdict

input = sys.stdin.readline

N = int(input())


def solution(N):
    roadMap = [[inf if c != r else 0 for c in range(N + 1)] for r in range(N + 1)]
    while True:
        p1, p2 = map(int, input().split())
        if p1 == -1 and p2 == -1:  # 입력 종료조건
            break
        # 양방향
        roadMap[p1][p2] = 1
        roadMap[p2][p1] = 1

    for viaP in range(1, N + 1):  # 경유지 선택
        for startP in range(1, N + 1):  # p1 선택
            for endP in range(1, N + 1):  # p2 선택
                minWeight = min(
                    roadMap[startP][endP], roadMap[startP][viaP] + roadMap[viaP][endP]
                )
                # 양방향
                roadMap[startP][endP] = minWeight
                roadMap[endP][startP] = minWeight

    rankP = defaultdict(list)
    # rank 집단 추가
    for p in range(1, N + 1):
        rankP[max(roadMap[p][1:])].append(p)

    # 최고 랭크 집단 찾기
    rank = 1
    while True:
        if rankP.get(rank) is None:
            rank += 1
            continue
        else:
            break

    print(rank, len(rankP[rank]))
    print(" ".join(map(str, rankP[rank])))


solution(N)
