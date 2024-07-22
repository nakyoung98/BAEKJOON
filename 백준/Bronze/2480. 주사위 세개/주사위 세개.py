# 값 세개 찢어서 받기
a,b,c = map(int, input().split())

# 상금 초기화
reward = 0

# 세 수가 모두 같으면
if a==b and b==c:
    reward = 10000 + a*1000
# 두 수가 같으면
elif a==b or b==c:
    reward = 1000 + b*100
elif a==c:
    reward = 1000 + a*100
# 다 다르면
else:
    reward = max(a,b,c)*100
    
print(reward)