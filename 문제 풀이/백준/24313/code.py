import sys


def solution(a1, a0, c, n0):
    # 정의 불만족
    result = 0

    # 정의 만족
    ## 간단한 설명
    ## f(n) = a1n + a0 라면 기울기가 a1이고 y절편이 a0인 일차함수 그래프로 이해할 수 있다
    ## c(n) = cn 으로 두자면 기울기가 c이고 y절편이 0인 일차함수 그래프로 이해할 수 있다
    ## a0가 음수가 가능하기 때문에, n0 시점에는 c(n0) >= f(n0)이지만,
    ## f(n) 기울기가 c(n)보다 크다면 n0 이후 어느 특정 시점에서 결국 f(n)의 그래프가 c(n)의 그래프를 추월하게 된다 (한 점에서 만난다)
    ## 따라서, f(n)의 기울기 a1또한 통제되어야한다.
    if a1 * n0 + a0 <= c * n0 and a1 <= c:
        result = 1

    return result


a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

print(solution(a1, a0, c, n0))
