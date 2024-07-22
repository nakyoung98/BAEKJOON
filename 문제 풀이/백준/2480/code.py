import sys

'''
입력: 3개의 주사위

같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

출력: 상금

[문제 접근]
주사위 세 개를 모두 비교하여 조건을 확인함
'''
# 상금 변수 초기화
reward = 0
# len = 7이고 초기화 값이 0인 배열(값 배열) 생성
dices = [0 for x in range(7) ]

# [입력]
# 주사위 찢어서 배열 (주사위 배열)에 저장 O(n)
tempDices = list(map(int, sys.stdin.readline().split()))

# 반복 (주사위 배열) O(n)
for dice in tempDices:
    # 주사위 배열의 값을 index로 하는 값 배열의 값 + 1
    dices[dice] += 1
    
try:
    # 3의 index 찾기 => 배열.index 사용 O(n)
    diceValue = dices.index(3)
    # 있으면 상금 = 10,000원+(같은 눈)×1,000원
    reward = 10000 + diceValue * 1000
    
# index 메소드는 찾지 못하면 ValueError가 발생함
except ValueError:
    None

try:
    # 2의 index 찾기 => 배열.index 사용 O(n)
    diceValue = dices.index(2)
    # 있으면 상금 = 1,000원+(같은 눈)×100원
    reward = 1000 + diceValue*100
    
# index 메소드는 찾지 못하면 ValueError가 발생함
except ValueError:
    None
    
# else 
    # 제일 큰 주사위 값 찾기 => 반복문 사용 O(n)
    for i in range(6,0,-1):
        if dices[i] == 1:
            #  상금 = (값)×100원
            reward = i*100
            break

# [출력]
# 상금 값
print(reward)