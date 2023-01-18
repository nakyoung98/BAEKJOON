import sys

#  a ASCII CODE : 97
#  A ASCII CODE : 65

line = sys.stdin.readline()
line = line.upper()

if line[-1] == "\n":
    line = line[:-1]

letters = [0 for _ in range(26)]

for letter in line:
    letters[ord(letter)-65] += 1

most = chr(letters.index(max(letters))+65)

letters = sorted(letters)

if letters[-1] == letters[-2]:
    print("?")
else:
    print(most)