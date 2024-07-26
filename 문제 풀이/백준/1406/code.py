import sys
from enum import Enum
from collections import deque


class Direction(Enum):
    L = "L"
    R = "R"


class Editor:
    def __init__(self, document) -> None:
        self.documentL = deque(document)
        self.documentR = deque()

    def __moveCursor(self, direction: Direction):
        if direction == Direction.L and not self.isCursorFirst():
            letter = self.documentL.pop()
            self.documentR.appendleft(letter)
        elif direction == Direction.R and not self.isCursorLast():
            letter = self.documentR.popleft()
            self.documentL.append(letter)

    def isCursorFirst(self):
        return len(self.documentL) == 0

    def isCursorLast(self):
        return len(self.documentR) == 0

    def __deleteLeft(self):
        if self.isCursorFirst():
            return

        self.documentL.pop()

    def __insertLeft(self, letter):
        self.documentL.append(letter)

    def instruct(self, instruct, data=None):
        if instruct == "L":
            self.__moveCursor(direction=Direction.L)
        elif instruct == "D":
            self.__moveCursor(direction=Direction.R)
        elif instruct == "B":
            self.__deleteLeft()
        elif instruct == "P" and data is not None:
            self.__insertLeft(data)

    def __str__(self) -> str:
        return "".join(self.documentL) + "".join(self.documentR)


def solution(N, data):
    editor = Editor(data)

    for _ in range(N):
        command = sys.stdin.readline().rstrip().split()
        instruction = command[0]
        data = command[1] if len(command) == 2 else None

        editor.instruct(instruction, data)

    print(editor)


data = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
solution(N, data)
