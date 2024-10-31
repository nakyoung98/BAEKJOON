def solution(words):
    trie = Node(None)
    for word in words:
        head = trie
        for letter in word:
            head.add(letter)
            # 다음 letter 삽입 가능하도록 맵 구성
            head = head.get_next_node(letter)
    
    # 문자열 문자 하나씩 타고 내려가는데, 더이상 본인 외의 자식이 없다면 
    sum_counts = 0
    for word in words:
        head = trie
        count = 0
        for letter in word:
            # 해당 문자 위치에 대한 노드 가지고 옴
            head = head.get_next_node(letter)
            count += 1
            if head.count == 1:
                break
                                                                                                                                                                                                                                                                                                                 
        sum_counts += count
    
    return sum_counts
            
    
class Node():
    def __init__(self, letter):
        self.letter = letter
        self.count = 1
        self.children = [None] * 26
    
    def add(self, child):
        child_ord = ord(child) - ord('a')
        if self.children[child_ord] is None:
            self.children[child_ord] = Node(child)
        else:
            self.children[child_ord].count += 1
    
    def get_next_node(self, next_letter):
        next_letter_ord = ord(next_letter) - ord('a')
        return self.children[next_letter_ord]
    