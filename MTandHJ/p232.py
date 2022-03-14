

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.front = None
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            return self.front
        else:
            return self.s2[-1]

    def empty(self) -> bool:
        if self.s1 or self.s2:
            return False
        else:
            return True
