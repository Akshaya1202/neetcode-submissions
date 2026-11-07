class MinStack:

    def __init__(self):
        self.main = []

    def push(self, val: int) -> None:
        self.main.append(val)

    def pop(self) -> None:
        self.main.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return min(self.main)
