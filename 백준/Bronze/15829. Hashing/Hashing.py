import sys

L = int(sys.stdin.readline())
string = sys.stdin.readline()[:-1]

r = 31
m = 1234567891

H = 0

for i in range(len(string)):
    H += (ord(string[i])-96)*(r**i)

H = H%m

print(H)
