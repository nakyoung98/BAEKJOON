"""
[사람수로 min max]
min = 1
max = n
작은쪽에 사람을 몰아주기
젤작은시간 * 중간 사람 수 = cur time
그다음 순서의 시간의 합이 curtime보다 크지 않을때까지만 사람 부여
계속 반복
맨 마지막에 까지 했는데 사람이 남았다? => 제일 작은 쪽에 사람 더 늘려야함 (즉, 지금 시간으론 아예 문제가 성립하지 않음)
맨 마지막까지 가기 전에 사람이 끝나거나 딱 맞았다? => 제일 작은 쪽에 사람 더 줄여야함 (즉, 지금 시간으론 아직 최소시간보다 큼), 더 적은 시간으로 끝낼 수도 있으니까 끝까지 가봐야함

[예시]
min = 1
max = 6
cur time = 3*7 = 21
21 // 10 = 2
1명 남음 -> 안됨

min = 4
max = 6
cur time = 5*7 = 35
35//10 = 3
0명 남음

min = 4
max = 4
mid = 4
cur time = 4*7 = 28
28//10 = 2
0명 남음

min = 4
max = 3
min이 max보다 커졌으므로 종료
"""
def solution(n, times):
    # 시간 정렬
    times.sort()
    
    min_t = 1
    max_t = times[-1]*n
    
    while min_t <= max_t:
        mid_t = (min_t + max_t)//2
        
        # 맨마지막까지 갔을 때 몇명이나 남는지 확인
        cur_p = n
        for time in times:
            cur_avail_p = mid_t // time
            cur_p -= cur_avail_p
            
        if cur_p > 0: #입국심사 받을 사람이 남음, 즉 전부 수용하지 못했음
            min_t = mid_t + 1
        else: # 입국 심사 받을 사람이 앞에서 끝났음, 즉 더 시간을 줄일 가능ㅇ성이 있음
            max_t = mid_t - 1
            
    return min_t
    