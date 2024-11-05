import sys
sys.setrecursionlimit(10000)

result = 0

def solution(n, money):
    recursion(n, money, 0)
    
    global result
    return result % 1000000007

def recursion(rest, money, index):
    global result
    if index == len(money) - 1:
        if rest % money[index] == 0:
            result += 1
        return
    if rest == 0:
        result += 1
        return


    cur_coin = money[index]    

    while rest >= 0:
        recursion(rest, money, index + 1 )
        rest -= cur_coin
        