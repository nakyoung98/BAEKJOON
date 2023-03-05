import sys

N = int(sys.stdin.readline())

for i in range(1,N+1):
    words = sys.stdin.readline().rstrip().split()
    words.reverse()

    print("Case #{0}:".format(i),*words)