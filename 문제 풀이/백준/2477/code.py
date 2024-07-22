import sys

'''
[입력]
1. C: 1m2당 참외 개수
2~. 각 방향의 데이터 값
    D: direction (동1, 서2, 남3, 북4)
    L: length
    
circular double linked list에 각 방향 데이터값 추가 및 연결
안쪽으로 꺾이는 구간 찾기: 노드를 순회하여 A->B->A->B 패턴 찾기
찾은 패턴 기반으로, 큰 사각형과(WH) 뺄 사각형(innerWH) 크기 구하기

[출력]
최종 사각형 너비 X 1m2당 참외개수 출력
'''
# 노드 클래스 구현
class Node:
    def __init__(self, direction, length) -> None:
        self.direction = direction
        self.length = length
        
        self.prev:Node = None
        self.next:Node = None
    
# 노드 리스트 클래스 구현
class DoubleLinkedList:
    def __init__(self) -> None:
        self.head:Node = None
    
    def isEmpty(self):
        return self.head is None
    
    def append(self, node:Node):
        if self.isEmpty():
            self.head = node
            
            node.prev = node
            node.next = node
            
        else:
            # 새 노드의 prev, next 추가
            node.prev = self.head.prev
            node.next = self.head
            # 마지막 노드의 next 새 노드로 변경
            self.head.prev.next = node
            # 첫 노드의 prev 새 노드로 변경
            self.head.prev = node

### [실제 코드] ###
# C: 1m2당 참외 개수 저장
C = int(sys.stdin.readline())

# 노드 리스트 생성
nodeList = DoubleLinkedList()

#  방향 개수만큼 반복
for _ in range(6):
    d, l = map(int, sys.stdin.readline().split())
    
    # 노드 추가하기
    node = Node(d,l)
    nodeList.append(node)
    
# 순회를 시작할 노드 선택
now = nodeList.head

squareMeter = 0

# 무한반복
while True:    
    # if head prev == next
    if now.prev.direction == now.next.direction:
        # if head == head next next
        if now.direction == now.next.next.direction:
            # 각 길이 정의하기
            ## 큰 사각형 WH
            W = now.prev.prev.length
            H = now.next.next.next.length
            ## 작은 사각형 innerWH
            innerW = now.length
            innerH = now.next.length
            
            # 사각형 크기 구하기
            ## 큰 사각형 S
            S = W * H
            ## 작은 사각형 innerS
            innerS = innerW * innerH
            
            # 큰 사각형 - 작은 사각형
            squareMeter = S - innerS
        
            # 반복문 탈출
            break
            
    # 다음 노드 head 이동
    now = now.next

# [출력]
# C * 사각형 넓이
print(C * squareMeter)