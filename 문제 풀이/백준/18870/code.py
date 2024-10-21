import sys

N = int(sys.stdin.readline())


def solution(N):
    numbers = list(map(int, sys.stdin.readline().split()))
    # set으로 중복제거, 및 정렬하여 특정 숫자가 가지는 rank 획득
    uniqueSortedNumbers = sorted(set(numbers))

    # 특정 value의 rank값 조회용 dict 생성
    rankDict = {number: rank for rank, number in enumerate(uniqueSortedNumbers)}

    # rank로 변환 한 결과 저장 (join 용이성을 위해 str로 저장)
    result = [str(rankDict[number]) for number in numbers]

    # 결과 출력
    print(" ".join(result))


solution(N)
