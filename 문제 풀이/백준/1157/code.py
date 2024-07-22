import sys

def solution(data:str):
    result = None
    
    # [알파벳,개수]로 이루어진 배열 생성
    ## 배열에서 제공하는 기능 사용 위함
    letters = [[chr(i),0] for i in range(65,91)]
    
    # 아스키 코드 변환 -> 배열 저장
    for letter in data:
        letters[ord(str.upper(letter))-65 ][1] += 1
    
    # 개수 기준으로 오름차순 정렬
    letters.sort(key= lambda x: x[1])
    
    # -1,-2 인덱스 값이 같지만 않으면 최대 개수가 겹치지 않는 것으로 판단
    if letters[-1][1] == letters[-2][1]:
        result = "?"
    else :
        result = letters[-1][0]
        
    return result

word = sys.stdin.readline().rstrip()
print(solution(word))
