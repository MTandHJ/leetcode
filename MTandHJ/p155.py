


class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        if self.s2:
            theMin = min(val, self.s2[-1])
        else:
            theMin = val
        self.s1.append(val)
        self.s2.append(theMin)

    def empty(self):
        if self.s1:
            return False
        else:
            return True

    def pop(self) -> None:
        if not self.empty():
            self.s1.pop()
            self.s2.pop()

    def top(self) -> int:
        if not self.empty():
            return self.s1[-1]

    def getMin(self) -> int:
        if not self.empty():
            return self.s2[-1]



