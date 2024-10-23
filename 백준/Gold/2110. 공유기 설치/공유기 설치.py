import sys


def solution(N, C, homes):

    sorted_homes = sorted(homes)

    min_d = 1
    max_d = sorted_homes[-1] - sorted_homes[0]
    mid_d = (min_d + max_d) // 2

    while min_d <= max_d:
        mid_d = (min_d + max_d) // 2

        count = 1
        cur_x = sorted_homes[0]
        for i in range(1, len(sorted_homes)):
            if sorted_homes[i] >= cur_x + mid_d:
                count += 1
                cur_x = sorted_homes[i]

        if count >= C:
            min_d = mid_d + 1
        elif count < C:
            max_d = mid_d - 1

    print(max_d)


N, C = map(int, sys.stdin.readline().split())
homes = [int(sys.stdin.readline()) for _ in range(N)]
solution(N, C, homes)
