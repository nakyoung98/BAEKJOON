import sys

dwarfs = []
sum = 0
for i in range(9):
    dwarf = int(sys.stdin.readline())
    dwarfs.append(dwarf)
    sum += dwarf

dwarfs.sort()

isFinish = False

for i in range(8):
    for j in range(i,9):

        if sum - dwarfs[i] - dwarfs[j] == 100:
            dwarfs.pop(j)
            dwarfs.pop(i)

            isFinish = True
            break

    if isFinish == True:
        break


print('\n'.join(map(str,dwarfs)))