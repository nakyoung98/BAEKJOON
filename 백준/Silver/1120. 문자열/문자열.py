import sys

X,Y = map(str, sys.stdin.readline().split())
results = []
for i in range(len(Y)-len(X)+1):
    difference = 0
    for index in range(len(X)):
        if X[index] != Y[index+i]:
            difference += 1
    results.append(difference)

print(min(results))