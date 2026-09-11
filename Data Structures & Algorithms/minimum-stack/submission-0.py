class MinStack:

    def __init__(self):
        self.con = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))
        self.con.append(val)

    def pop(self) -> None:
        self.mins.pop()
        return self.con.pop()

    def top(self) -> int:
        return self.con[-1]

    def getMin(self) -> int:
        return self.mins[-1]
