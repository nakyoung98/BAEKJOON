"""
spell에 있는 알파벳을 한번씩만 모두 사용한 단어를 찾아내기
존재하면 1 안하면 2
"""
def solution(spell, dic):
    result = 2
    
    for word in dic:
        dicti = {x:0 for x in spell}
        for letter in word:
            try:
                dicti[letter] += 1
            except:
                pass
        
        if list(dicti.values()).count(1) == len(dicti):
            result = 1
            break
    
    return result
        