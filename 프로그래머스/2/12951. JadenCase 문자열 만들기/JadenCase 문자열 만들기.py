def solution(s):
    answer = []
    
    for i in range(len(s)):
        if i == 0 or s[i-1] == " ":
            answer.append(s[i].upper())
        else:
            answer.append(s[i].lower())
           
    return ''.join(answer)