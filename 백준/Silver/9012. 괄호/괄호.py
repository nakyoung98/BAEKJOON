import sys

N = int(sys.stdin.readline())

left = '('
right = ')'

for _ in range(N):
    line = sys.stdin.readline()[:-1]

    isTrue = False

    count = 0

    if line[0] == left and line[-1] == right:

        for letter in line:
            if letter == left:
                count += 1
            else:
                count -= 1
                if count < 0 :
                    break
            
        if count == 0:
            isTrue = True

    if isTrue == True:
        print("YES")
    else:
        print("NO")