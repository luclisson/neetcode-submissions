class MinStack:

    def __init__(self):
        self.stack = []
        self.minSt = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minSt or val < self.minSt[-1]:
            self.minSt.append(val)
        else:
            self.minSt.append(self.minSt[-1])

    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack)-1]
        self.minSt = self.minSt[:len(self.minSt)-1]

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minSt[-1]
        
