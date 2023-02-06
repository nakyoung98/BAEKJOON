import sys

line = sys.stdin.readline().rstrip()

while line != ".":

    stack = []

    Answer = True

    for letter in line:

        if letter == '[' or letter == '(':
            stack.append(letter)


        elif letter == ']' or letter == ')':
            if len(stack) >0:
                popLetter = stack.pop()

                if letter == ']':
                    if popLetter == '(':
                        Answer = False
                        break

                elif letter == ')':
                    if popLetter == '[':
                        Answer = False
                        break
            else:
                Answer = False
                break

    if len(stack) != 0:
        Answer = False


    if Answer == True:
        print('yes')
    else:
        print('no')

    line = sys.stdin.readline().rstrip()