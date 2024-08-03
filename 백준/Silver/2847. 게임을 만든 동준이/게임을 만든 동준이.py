import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    totalCount = 0
    scores = []
    for _ in range(N):  # 점수 입력받기
        score = int(input())
        scores.append(score)

    for i in range(len(scores) - 2, -1, -1):  # 맨 끝하나 앞부터 시작
        nextLevel = scores[i + 1]
        target = nextLevel - 1
        current = scores[i]

        if (
            nextLevel > current
        ):  # 현재 레벨 점수가 이미 다음 레벨보다 작다면 내릴 필요가 없음
            continue

        downCount = current - target
        totalCount += downCount
        scores[i] = target  # 변경된 스코어로 대체

    return totalCount


print(solution())
