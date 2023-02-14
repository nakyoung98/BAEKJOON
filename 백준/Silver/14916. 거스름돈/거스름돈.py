import sys

n = int(sys.stdin.readline())


for coin2 in range(int(n/2)+1):
    if coin2*2 >n:
        break
    for coin5 in range(int(n/5)+1):
        if coin2 *2 + coin5 *5 == n:
            print(coin2+coin5)
            exit()
        if coin2 *2 + coin5 * 5 > n:
            break

print(-1)