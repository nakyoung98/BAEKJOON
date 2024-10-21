import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())


def solution(N):
    aliasDict = defaultdict(int)  # 모든 prefix파악 위해 hash 사용

    for _ in range(N):
        nickname = input().rstrip()
        alias = None
        for prefixEndIdx in range(1, len(nickname)):
            currentPrefix = nickname[:prefixEndIdx]
            # 사전에 해당 prefix가 없다면, 즉 누구의 prefix도 아니라면
            # 해당 유저의 prefix로 정함
            if alias is None and aliasDict.get(currentPrefix, -1) == -1:
                alias = currentPrefix

            aliasDict[
                currentPrefix
            ]  # 다른 유저가 중복되지 않도록, prefix 사전에 추가해놓기
        # 본인 닉네임에는 +1을 하여, 닉네임 자체가 중복인 유저가 있는지 파악
        aliasDict[nickname] += 1
        if alias is None:  # 끝까지 별칭을 못정했으면 닉네임 +사람 수로 지정
            sameNicknameUsers = aliasDict[nickname]
            alias = f"{nickname}{ sameNicknameUsers if sameNicknameUsers > 1 else '' }"

        print(alias)


solution(N)
