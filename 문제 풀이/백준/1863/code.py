import sys

input = sys.stdin.readline

N = int(input())


class BuildingCounter:
    def __init__(self) -> None:
        self.stack = []
        self.count = 0

    # pop은 class 내에서만 사용되도록 처리
    def __pop(self):
        if self.isEmpty():
            return

        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def put(self, buildingHeight):
        while self.stack and self.stack[-1] >= buildingHeight:
            lastHeight = self.__pop()

            # 만약 buildingHeight보다 큰 친구였다면 다른 건물로 취급
            ## 건물개수  ++
            if lastHeight > buildingHeight:
                self.count += 1
            # 만약 buildingHeight와 같은 높이의 친구라면 같은 건물로 취급
            ## 건물개수 그대로 (if문은 따로 쓰지 않음)

        # 바닥(0)은 건물로 취급하지 않으므로 건물 count에 추가되지 않게 한다
        if buildingHeight > 0:
            self.stack.append(buildingHeight)

    def getCount(self):
        if self.stack:
            self.count += len(self.stack)
            self.stack.clear()

        return self.count


def solution(N):
    buildingCounter = BuildingCounter()

    for _ in range(N):
        # x는 순서 보장이므로 필요 없음
        _, y = map(int, input().split())
        buildingCounter.put(y)

    print(buildingCounter.getCount())


solution(N)
