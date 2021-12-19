
class MyStack:
    def __init__(self) -> None:
        self.q1 = []
        self.q2 = []
    
    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.pop(0))
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop(0)

    
    def top(self) -> int:
        return not self.q1
