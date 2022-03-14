


import collections


class MyStack:

    def __init__(self):
        self.q1 = collections.deque([])
        self.q2 = collections.deque([])

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        if not self.empty():
            return self.q1.popleft()

    def top(self) -> int:
        if not self.empty():
            return self.q1[0]

    def empty(self) -> bool:
        if self.q1:
            return False
        else:
            return True

