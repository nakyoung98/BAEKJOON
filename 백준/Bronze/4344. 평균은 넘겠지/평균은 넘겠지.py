import sys

'''
[입력]
1. C: 테스트 케이스 개수
2~. 각 테스트 케이스에 대한 값
    N: 학생의 수 
    ...: N명의 점수 (0<=score<=100 정수)

# C의 값 구간을 알 수 없어 명확하게 시간 복잡도를 파악하기 어려움

점수 모두 더해 저장
N*해당 학생 점수 > sum보다 큰 경우 개수 구하기
비율 구하기

[출력]
~. 각 케이스 당 평균을 넘는 학생의 비율 (소수점 넷째자리서 반올림)
'''

# [입력]
# 테스트 케이스 개수 받기
C = int(sys.stdin.readline())

# C만큼 반복 O(C)
for _ in range(C):
    # [입력]
    # N과 나머지 점수(배열) 분리
    N, *scores = map(int, sys.stdin.readline().split())
    
    # 넘는 학생수용 변수 선언
    overScoreStudents = 0
    
    # 점수 sum 구하기 O(N)
    sumScores=  sum(scores)
    
    # 학생 수만큼 반복
    for score in scores:
        # if 학생점수 * n > sum
        if score * N > sumScores:
            # 넘는 학생수 += 1
            overScoreStudents += 1
        
    # 비율 구하기 (소수점 넷째자리에서 반올림)
    proportion = overScoreStudents * 100 /N 
    
    # [출력]
    # 셋째자리까지 출력
    # 내장 반올림 기능으로 인해 자동으로 업데이트 됨
    print(f'{proportion:.3f}%')
    
    