import sys

def count_representations(N):
    count = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            if i % 2 == 1:  # i가 홀수인 경우
                count += 1
            if i != N // i and (N // i) % 2 == 1:  # N/i가 i와 다르고 홀수인 경우
                count += 1
    return count

N = int(sys.stdin.readline())
print(count_representations(N))