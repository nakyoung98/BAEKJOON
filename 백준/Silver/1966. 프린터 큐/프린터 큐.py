import sys
from collections import deque

"""
문서를 분석할 때,
한번 중요도 개수를 세서 배열에 추가해놓음 (O(n))
그다음에 프린트가 되면, 해당 문서의 중요도 -1 O(1)
그런데, 우선순위 높은게 남아있다면, 다시 뒤에 붙이기 (O(1))

O(n)은 딱 한번밖에 일어나지 않음
"""


class Print:
    def __init__(self, printQueueDatas) -> None:
        self.printQueue = deque()
        # 우선순위 1~9
        self.priorities = [0] * 10

        for i in range(len(printQueueDatas)):
            # 각 요소: [문서번호, 우선순위] 구조
            self.printQueue.append([i, printQueueDatas[i]])

        # 중요도 개수를 세서 배열에 추가
        for i in range(len(self.printQueue)):
            self.priorities[self.printQueue[i][1]] += 1

    def print(self):
        if self.isEmpty():
            return

        nowPriority = self.printQueue[0][1]

        # 우선순위 높은게 남아있다면, 다시 뒤에 붙이기
        for i in range(nowPriority + 1, len(self.priorities)):
            if self.priorities[i] > 0:
                print = self.printQueue.popleft()
                self.printQueue.append(print)
                return None

        # 아니면 프린트하고, 남은 우선순위 개수 조정
        item = self.printQueue.popleft()
        self.priorities[item[1]] -= 1
        return item[0]

    def isEmpty(self):
        return len(self.printQueue) == 0


def solution(T):
    for _ in range(T):
        allDocNum, selectedDocQueueIdx = map(int, sys.stdin.readline().split())
        priorities = list(map(int, sys.stdin.readline().split()))

        printQueue = Print(priorities)
        printCount = 0

        while True:
            result = printQueue.print()

            if result is not None:
                printCount += 1

            if result == selectedDocQueueIdx:
                print(printCount)
                break


T = int(sys.stdin.readline())
solution(T)
