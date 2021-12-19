
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
            # 把s1中的元素移到s2中去
            while self.s1:
                self.s2.append(self.s1.pop())
            # 为什么这里要变为None
            self.front = None
        return self.s2.pop()
    
    def peek(self) -> int:
        # 当其中s1中没有元素时，才需要从s2中取，
        if self.s2:
            return self.s2[-1]
        return self.front
    
    def empty(self):
        return not self.s1 and not self.s2
