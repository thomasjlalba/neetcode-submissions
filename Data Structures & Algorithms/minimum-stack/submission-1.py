class MinStack:

    def __init__(self):
        self.mins = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0 or self.mins[-1] >= val:
            self.mins.append(val)

    def pop(self) -> None:
        if self.mins[-1] == self.stack[-1]:
            self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
