import sys
import heapq


class Santa:
    def __init__(self) -> None:
        self.presents = []

    def __popPresent(self):
        result = -1
        try:
            result = -heapq.heappop(self.presents)
        except IndexError:
            pass

        return result

    def __addPresents(self, presents):
        for present in presents:
            heapq.heappush(self.presents, -present)

    def instruct(self, dataArray):
        if dataArray[0] == 0:
            return self.__popPresent()
        else:
            self.__addPresents(dataArray[1:])
            return None


def solution(N):
    santa = Santa()

    for _ in range(N):
        data = list(map(int, sys.stdin.readline().split()))
        flow = santa.instruct(data)
        if flow is not None:
            print(flow)


N = int(sys.stdin.readline())
solution(N)
