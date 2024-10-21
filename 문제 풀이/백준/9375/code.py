import sys


def solution(Test):

    for _ in range(Test):
        clothes = {}
        wears = int(sys.stdin.readline())
        for __ in range(wears):
            cloth, category = sys.stdin.readline().split()
            clothes.setdefault(category, [])
            clothes[category].append(cloth)

        result = 1
        for value in clothes.values():
            result *= len(value) + 1

        # 아무것도 안입는 경우 빼기
        result -= 1
        print(result)


T = int(sys.stdin.readline())
solution(T)
