import sys

N = int(sys.stdin.readline())
# N = int("3\n")
scores = list(map(int,sys.stdin.readline().split()))
# scores =list(map(int,"10 20 30\n".split()))

maxScore = max(scores)

newSum = 0
for score in scores:
    newSum += float(score)/float(maxScore)*100

newAvg = newSum/N

print(newAvg)