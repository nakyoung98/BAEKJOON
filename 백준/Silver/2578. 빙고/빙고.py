import sys

input = sys.stdin.readline


def solution():
    # 철수 빙고판
    bingo = [list(map(int, input().split())) for _ in range(5)]
    # 사회자
    numberOrder = []
    for _ in range(5):
        numberOrder.extend(map(int, input().split()))

    # 숫자 기준으로 빙고판 만들기
    bingoIndices = [0] * 26
    for y in range(5):
        for x in range(5):
            bingoIndices[bingo[y][x]] = (y, x)

    # 빙고 관련 값
    BingoRows = [0, 0, 0, 0, 0]
    BingoCols = [0, 0, 0, 0, 0]
    BingoCross = [0, 0]

    bingos = 0
    for orderIdx, order in enumerate(numberOrder):
        # 해당 숫자 위치 찾기
        y, x = bingoIndices[order]

        # 빙고 관련된 값 숫자 올리기
        BingoRows[y] += 1  # y번째 행에 대한 빙고 현황
        BingoCols[x] += 1  # x 번째 열에 대한 빙고 현황
        bingos += int(BingoRows[y] == 5) + int(BingoCols[x] == 5)  # 현재 빙고 현황
        if x == y:
            BingoCross[0] += 1  # 우하향 대각선 빙고 현황
            bingos += int(BingoCross[0] == 5)
        if x == 4 - y:
            BingoCross[1] += 1  # 우상향 대각선 빙고 현환
            bingos += int(BingoCross[1] == 5)

        # 3빙고 이상 되었는지 확인
        if bingos >= 3:
            return orderIdx + 1  # idx + 1 == 현재 부른 횟수


print(solution())
