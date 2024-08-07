import sys
import re

input = sys.stdin.readline


# 접근방식
## -를 만나면, 다음 -를 만날때까지 지나는 모든 수는 -의 괄호로 묶는다.
## 하지만 다시 생각해보면 처음 -를 만나면 그떄부터 끝까지 만나는 모든 수들을 빼도 동일하다
### 예시
### 100 - 50 + 40 + 20 - 80 + 30 = 100 - (50 + 40 + 20) - (80 + 30)
###  == 100 - 50 - 40 - 20 - 80 - 30
result = 0

initialExpressions = input().rstrip()
# +와 - 나 숫자 정규표현식
reg = r"[+\-]"
operands = list(map(int, re.split(reg, initialExpressions)))
# +와 - 나 숫자 정규표현식
operators = re.findall(reg, initialExpressions)

# 첫 - 위치 찾기
try:
    firstMinusIdx = operators.index("-")

    # N번째에 -가 있다면, 0~N까지는 덧셈을 수행해야함
    plusPart = operands[: firstMinusIdx + 1]
    minusPart = operands[firstMinusIdx + 1 :]
    result = sum(plusPart) - sum(minusPart)
except ValueError:  # 만약 -가 배열 내에 없다면  index 함수 수행 과정에서 오류가 발생함
    # 없다면 다 합치고
    result = sum(operands)

print(result)
