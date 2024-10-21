def solution(x):
    str_x = str(x)
    sum_num = 0
    
    # 각 자리 수 더하기
    for i in range(len(str_x)):
        sum_num += int(str_x[i])
    
    return True if x % sum_num == 0 else False
    
