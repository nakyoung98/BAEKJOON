import sys

N = int(sys.stdin.readline())
# N = int(input())

for _ in range(N):
    quiz = sys.stdin.readline()[:-1]
    # quiz = input()
    sum = 0

    for i in range(len(quiz)):
        score = 0
        
        before = "X"
        for j in range(i+1):
            if before == "X" :
                if quiz[j] == "X":
                    score = 0
                else:
                    score += 1
                    before = "O"
            elif before == "O":
                if quiz[j] == "X":
                    score = 0
                    before = "X"
                else:
                    score += 1
        
        sum+= score

    print(sum)