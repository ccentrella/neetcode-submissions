class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Min should be min of existing min and new element
        existing_min = self.min[-1] if len(self.min) > 0 else float('inf')
        self.min.append(min(existing_min, val))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
