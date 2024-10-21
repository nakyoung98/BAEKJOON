"""
매일 1명의 가수가 노래
시청자들의 문자 투표수로 가수에게 점수를 부여
지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념
"""
def solution(k, score):
    scores = []
    answer = []
    for today_score in score:
        put_and_sort(scores, today_score)
        scores = scores[:k]
        answer.append(scores[-1])
    return answer

def put_and_sort(list, item):
    for i in range(len(list)):
        if list[i] < item:
            list.insert(i, item)
            return
        
    
    list.append(item)
        
    
    
    