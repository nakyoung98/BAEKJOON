class MaxHeap:
    def __init__(self, array=[]):
        self.heap = [0] + array
        self._build_heap()

    def _build_heap(self):
        for i in range((len(self.heap) - 1) // 2, 0, -1):
            self._sift_down(i)

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def popMost(self):
        if len(self.heap) <= 1:
            raise IndexError("더이상 꺼낼 요소가 없습니다")
        if len(self.heap) == 2:
            return self.heap.pop()

        max_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._sift_down(1)
        return max_val

    def _sift_up(self, i):
        while i > 1 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def _sift_down(self, i):
        max_index = i
        while True:
            left = 2 * i
            right = 2 * i + 1
            if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
                max_index = left
            if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
                max_index = right
            if i == max_index:
                break
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            i = max_index

    def __len__(self) -> int:
        return len(self.heap) - 1

    def __str__(self) -> str:
        return "[" + ", ".join(map(str, self.heap[1:])) + "]"


import sys


class Hammer:
    def __init__(self, maxHammeringCount):
        self.maxHammeringCount = maxHammeringCount
        self.count = 0

    def hit(self, value):
        if self.isExhausted():
            raise ValueError("횟수를 모두 소진했습니다")

        self.count += 1
        self.maxHammeringCount -= 1

        if value == 1:
            return 1

        return value // 2

    def isExhausted(self):
        return self.maxHammeringCount == 0

    def __len__(self) -> int:
        return self.maxHammeringCount


def solution(population, centiH, maxHammerCount):
    result = "YES"
    heights = []

    # 센티보다 큰 거인 키 수집
    for _ in range(population):
        height = int(sys.stdin.readline())
        if height >= centiH:
            heights.append(height)

    # heigh ts maxHeap 정렬
    heights = MaxHeap(heights)
    hammer = Hammer(maxHammerCount)

    # heights에서 하나씩 꺼내어 해머링
    while not hammer.isExhausted() and heights:
        try:
            peek = heights.popMost()
            peek = hammer.hit(peek)
            if peek >= centiH:
                heights.insert(peek)
        except IndexError:
            break
        except ValueError:
            break

    if not heights:
        print("YES")
        print(hammer.count)
    else:
        print("NO")
        print(heights.popMost())


population, centiH, maxHammerCount = map(int, sys.stdin.readline().split())
solution(population, centiH, maxHammerCount)
