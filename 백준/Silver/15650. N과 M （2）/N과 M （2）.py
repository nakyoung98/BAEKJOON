"""
[입력]
1. N: 자연수의 끝
2. M: 선택 개수 (중복X)

[로직]
백트랙킹 실행

반환부 -> 선택 가능한 개수가 0 
실행부 -> 현재 자연수를 선택
재귀부 -> 다음 수 고르게 시키기

[출력]
모든 경우 출력
"""

import sys


def solution(N, M):
    # 선택된 수 저장 배열
    selected = [0 for _ in range(M)]

    def recursion(now, left):
        # [반환부]
        # 마지막 선택이면 결과에 저장하고 return
        if left == 0:
            print(" ".join(map(str, selected)))

            return

        # [실행부]
        # 현재 수 이상의 값으로 배열 채우기
        for i in range(now, N + 1):
            # 배열 안에 없는 값이면 추가
            if i not in selected:
                selected[M - left] = i
                recursion(i + 1, left - 1)
                # 탐색 원상복구
                selected[M - left] = 0

    recursion(1, M)


N, M = map(int, sys.stdin.readline().split())
solution(N, M)
