def matrixMul(Mx1, Mx2, Mx1rowSize, Mx1colSize, Mx2colSize):
    result = ""
    for i in range(Mx1rowSize):
        for j in range(Mx2colSize):
            mulSum = 0
            for k in range(Mx1colSize):
                mulSum += Mx1[i][k] * Mx2[k][j]

            result += f"{mulSum} "

        result += "\n"

    return result


import sys

# 행렬 곱의 결과는 ArowSize * BcolSize 이며, 각 요소는 AcolSize 및 BcolSize와 관련있음
# 또한 행렬 곱의 조건에는 AcolSize = BrowSize이므로 BrowSize는 크게 사용할 일이 없음
ArowSize, AcolSize = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(ArowSize)]

BrowSize, BcolSize = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(BrowSize)]

print(
    matrixMul(
        Mx1=A, Mx2=B, Mx1rowSize=ArowSize, Mx1colSize=AcolSize, Mx2colSize=BcolSize
    )
)
