import sys
from collections import deque


# stack 구현
# instruction  기반으로 실행되므로, instruction을 제외한 나머지 메소드는 private 처리
class Stack:
    def __init__(self) -> None:
        # instruction에 대응되는 메소드 정의
        self.rules = {
            "push": self.__push,
            "pop": self.__pop,
            "size": self.__size,
            "empty": self.__empty,
            "top": self.__top,
        }

        self.stack = deque()

    def __push(self, i: int):
        self.stack.append(i)

    def __pop(self):
        return self.stack.pop() if not self.__empty() else -1

    def __size(self):
        return len(self.stack)

    def __empty(self):
        return 1 if self.__size() == 0 else 0

    def __top(self):
        return self.stack[-1] if not self.__empty() else -1

    def instruct(self, instruction, data=None):
        result = None

        if data:
            result = self.rules[instruction](data)
        else:
            result = self.rules[instruction]()

        return result


def solution(N):
    stack = Stack()

    for _ in range(N):
        command = sys.stdin.readline().split()
        instruction = command[0]
        data = int(command[1]) if len(command) > 1 else None

        result = stack.instruct(instruction, data)
        print(result) if result is not None else None


N = int(sys.stdin.readline())
solution(N)
