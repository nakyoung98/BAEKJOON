import sys
from math import inf

input = sys.stdin.readline


def solution():
    location, findRangeLimit, roadCount = map(int, input().split())
    items = [0]
    items.extend(map(int, input().split()))
    roadMap = [
        [inf if c != r else 0 for c in range(location + 1)] for r in range(location + 1)
    ]
    for _ in range(roadCount):
        loc1, loc2, roadWeight = map(int, input().split())
        # 양방향 도로
        roadMap[loc1][loc2] = roadWeight
        roadMap[loc2][loc1] = roadWeight

    # 플루이드 워셜로 모든 방향 -> 모든 방향으로의 최단거리 탐색
    for viaLoc in range(1, location + 1):  # 경유지 설정
        for startLoc in range(1, location + 1):  # 시작 지점 설정
            for endLoc in range(1, location + 1):  # 도착 지점 설정
                # 최소값 갱신 로직
                minDist = min(
                    roadMap[startLoc][endLoc],
                    roadMap[startLoc][viaLoc] + roadMap[viaLoc][endLoc],
                )
                # 양방향 도로
                roadMap[startLoc][endLoc] = minDist
                roadMap[endLoc][startLoc] = minDist

    # 지점에서 범위내에 갈 수 있는 지점의 아이템 값들을 추가하는 로직
    result = [0] * (location + 1)
    for startLoc in range(1, location + 1):
        # 거리 내에 있는 지점의 아이템개수만 결과에 추가
        for endLoc in range(1, location + 1):
            if roadMap[startLoc][endLoc] <= findRangeLimit:
                result[startLoc] += items[endLoc]

    # 얻을 수 있는 최대 아이템 개수 반환
    return max(result)


print(solution())
