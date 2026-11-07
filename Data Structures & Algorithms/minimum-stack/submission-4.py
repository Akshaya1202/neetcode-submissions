class MinStack:

    def __init__(self):
        self.main = []
        self.mins = []

    def push(self, val: int) -> None:
        self.main.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(self.mins[-1],val))

    def pop(self) -> None:
        self.main.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.mins[-1]