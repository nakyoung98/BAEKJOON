import sys


"""
남학생
1. 스위치 번호 == 받은 수 * k:
    받은 수 스위치 토글
여학생
1. 본인 위치 기준 좌우 대칭인 구간 찾기:
    해당 구간 스위치 모두 변경 
"""

LEN_SWITCHES = int(sys.stdin.readline())
switches = list(map(int, sys.stdin.readline().split()))
students = int(sys.stdin.readline())

BOY = 1
GIRL = 2


def solution(lenSwitches, switches, students):

    for _ in range(students):
        sex, switch = map(int, sys.stdin.readline().split())

        # switch 값 보정 (index 규칙에 맞추기)
        switch -= 1

        # 남학생
        if sex == BOY:
            # 배수 스위치 모두 토글
            ## 스위치 값은 이전에 보정해준 바 있으므로, 점프 간격은 복원해준다
            for i in range(switch, lenSwitches, switch + 1):
                switches[i] = toggle(switches[i])

        # 여학생
        elif sex == GIRL:
            # 대칭 구간 찾기
            left, right = findSwitchesSameRange(switch, switches, lenSwitches)
            # 구간 스위치 토글
            for i in range(left, right + 1):
                switches[i] = toggle(switches[i])

    return formatSwitches(switches)


def findSwitchesSameRange(switch, switches, lenSwitches):
    # 투포인터
    left = switch
    right = switch

    # 구간 찾기
    ## 양쪽 대칭 값이 같을 때 까지는 계속 이동
    # 1 0 1 1
    while (left > -1 and right < lenSwitches) and switches[left] == switches[right]:
        left -= 1
        right += 1

    # 한칸씩 더 갔으므로 복구
    left += 1
    right -= 1

    return left, right


def toggle(status):
    if status == 1:
        return 0
    else:
        return 1


def formatSwitches(switches):
    return "\n".join(
        " ".join(map(str, switches[i : i + 20])) for i in range(0, len(switches), 20)
    )


print(solution(lenSwitches=LEN_SWITCHES, switches=switches, students=students))
