import sys
import heapq


class Hammer:
    class ExhaustedError(Exception):
        """해머 사용횟수가 모두 소진되었습니다"""

        pass

    def __init__(self, maxHitCount):
        self.maxHitCount = maxHitCount
        self.count = 0

    def hit(self, data):
        if self.isExhausted():
            raise self.ExhaustedError()

        self.maxHitCount -= 1
        self.count += 1
        return data // 2 if data // 2 != 0 else 1

    def isExhausted(self):
        return self.maxHitCount <= 0


def solution(population, centiH, maxHitCount):
    heights = []
    hammer = Hammer(maxHitCount)

    for _ in range(population):
        height = int(sys.stdin.readline())

        # 큰 것들만 저장
        if height >= centiH:
            heights.append(-height)

    # heapify로 배열 => heap
    # 최소힙을 만들기 때문에, 최대값을 픽해야하는 현 문제에서는 음수로 저장
    heapq.heapify(heights)

    # maxHitCount나 heights의 크기를 비교해가며 pop
    while not hammer.isExhausted() and len(heights) > 0:
        # 거인 뽑아서
        peek = -heapq.heappop(heights)
        # 키작게하고
        peek = hammer.hit(peek)
        # 크면 다시 heap에 넣고
        if peek >= centiH:
            heapq.heappush(heights, -peek)

    if heights:
        print("NO")
        print(-heights[0])
    else:
        print("YES")
        print(hammer.count)


population, centiH, maxHitCount = map(int, sys.stdin.readline().split())
solution(population, centiH, maxHitCount)
