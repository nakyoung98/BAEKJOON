import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    #dp를 위한 임시 저장 리스트
    aparts = [[0 for _ in range(n+1)] for _ in range(k)]
    
    #1층의 기저 값 입력
    for i in range(n+1):
        aparts[0][i] = i

    #k-1층 n호까지의 인원수 구하기 
    for floor in range(1,k):

        for room in range(1,n+1):
            peopleSum = 0
            
            for people in range(room):
                peopleSum += aparts[floor-1][people]
            peopleSum += aparts[floor-1][room]

            aparts[floor][room] = peopleSum
    
    #k층 n호의 인원수
        #k-1층의 1호부터 n호까지 합한다.
    result = 0
    for room in range(1,n+1):
        result += aparts[k-1][room]


    print(result)