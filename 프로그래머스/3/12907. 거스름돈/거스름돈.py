def solution(n, money):
    # dp 배열 초기화
    dp = [0] * (n + 1)
    dp[0] = 1  # 0원을 만드는 방법은 1가지 (아무 동전도 사용하지 않는 경우)

    # 각 동전에 대해 반복
    for coin in money:
        # 현재 동전으로 만들 수 있는 금액을 업데이트
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    return dp[n]%1000000007