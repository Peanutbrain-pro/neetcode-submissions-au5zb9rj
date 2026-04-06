class MinStack:

    def __init__(self):
        self.minimum = None
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum != None:
            if val < self.minimum:
                self.minimum = val
        else:
            self.minimum = val
        self.minStack.append(self.minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.minimum = self.minStack[-1] if self.minStack else None 


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
