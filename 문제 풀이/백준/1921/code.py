import sys
import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def instruct(self, value):
        result = None
        if value == 0:
            try:
                result = heapq.heappop(self.heap)
            # 힙이 비어 있으면, IndexError가 발생한다
            except IndexError:
                result = 0

        else:
            heapq.heappush(self.heap, value)

        return result


def solution(N):
    heap = MinHeap()
    result = []

    for _ in range(N):
        value = int(sys.stdin.readline())
        instructResult = heap.instruct(value)

        if instructResult is not None:
            result.append(str(instructResult))

    print("\n".join(result))


N = int(sys.stdin.readline())
solution(N)
