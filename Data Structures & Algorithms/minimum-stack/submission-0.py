class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        lastmin = val
        if self.stack:
            lastmin = self.stack[-1][1]

        minval = min(lastmin, val)
        self.stack.append((val, minval))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:   
        return self.stack[-1][1]
        
