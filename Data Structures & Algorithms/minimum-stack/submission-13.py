class MinStack:
    def __init__(self):
        self.body = []

    def push(self, val: int) -> None:
        current_min = min(val, self.body[-1][1]) if self.body else val
        self.body.append((val, current_min))

    def pop(self) -> None:
        if self.body:
            self.body.pop()

    def top(self) -> int:
        return self.body[-1][0]

    def getMin(self) -> int:
        return self.body[-1][1]