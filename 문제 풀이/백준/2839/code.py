import sys

'''
[입력]
N: 설탕 무게

설탕 무게에서 5를 나눈 몫(quatientBy5)을 기억 (봉투 수를 최소로 하기 위함)

전체 - 5*quatientBy5 % 3 == 0이면 완료
아니면 quatientBy5가 0이될 때까지 quatientBy5-1해서 반복
모두 안되면 -1

[출력]
최소 개수(불가능시 -1)
'''
# default 결과값 저장
result = -1

# 설탕 무게 입력
N = int(sys.stdin.readline())

# 결과값을 최소화 하기 위해 제일 큰 값으로 나누기
quatientBy5 = N // 5

# quatientBy5가 음수가 될 때까지 반복
while quatientBy5>=0:
    # if 전체 -  5*quatientBy5 % 3 == 0
    left = N - 5*quatientBy5
    if left %3 == 0:
        # 3으로 나눈 몫 저장
        quatientBy3 = left// 3
        # result에 quatientBy5와 3으로 나눈 몫 저장
        result = quatientBy5 + quatientBy3
        break
    
    quatientBy5 -= 1
    
print(result)
    