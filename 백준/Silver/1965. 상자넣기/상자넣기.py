import sys

input = sys.stdin.readline



def solution(N):
    dp = [1]
    numbers = list(map(int, input().split()))

    for numIdx in range(1, len(numbers)):
        # 본인의 이전 숫자들 중 본인보다 작은 숫자 탐색
        # 그 중에서도 dp가 제일 높은 값을 선택
        maxDP = 0
        for beforeNumIDx in range(numIdx):
            if numbers[beforeNumIDx] < numbers[numIdx] and dp[beforeNumIDx] > maxDP:
                maxDP = dp[beforeNumIDx]

        # 만약 앞에 본인보다 큰게 없었다면 maxDP가 0이므로 자동으로 1이 저장될 것이고
        # 본인보다 큰게 있었다면 그 DP 값 +1 로 자연스럽게 이어짐
        dp.append(maxDP + 1)

    result = max(dp)

    return result


N = int(input())
result = solution(N)
print(result)
