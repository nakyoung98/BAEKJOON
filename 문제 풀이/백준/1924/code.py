import sys

'''
입력: x(월) y(일)

x월 y일이 2007년 며칠째인지 계산
계산값을 7로 나누면 무슨 요일인지 알 수 있음

출력: 요일
'''

# [입력]
# x y 입력
x, y = map(int, sys.stdin.readline().split())

# 1월부터 12월까지 한 달의 날짜(daysOfMonth)를 배열에 저장
daysOfMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# 월-일(daysOfWeek)까지 배열에 저장
dayOfWeeks = ['SUN','MON','TUE','WED','THU','FRI','SAT']

# 2007년으로부터 며칠째인지 저장하는 변수
days = 0

# x월 y일이 1월 1일로부터 며칠 지난 것인지 계산
# x월 -1번 index까지 daysOfMonth의 값을 더하기
for month in range(x):
    days += daysOfMonth[month]
# y일 더하기
days += y

# 7 나눈 나머지로 요일 추출
dayOfWeek = days % 7

# [출력]
# 요일 출력
print(dayOfWeeks[dayOfWeek])

