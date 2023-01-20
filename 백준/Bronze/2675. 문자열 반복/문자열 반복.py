import sys

T = int(sys.stdin.readline())

for _ in range(T): #T만큼 줄 추가로 읽음
    lines = sys.stdin.readline().split()
    time = int(lines[0])
    string = lines[1]

    answer = ""
    for letter in string :
        answer += letter*time

    print(answer)
