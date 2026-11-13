class MinStack:

    def __init__(self):
        self.st = []
        self.st_min = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.st_min:
            self.st_min.append(val)
        else:
            self.st_min.append(min(val,self.st_min[-1]))

    def pop(self) -> None:
        self.st.pop()
        self.st_min.pop()

    def top(self) -> int:
        if len(self.st) > 0:
            return self.st[-1]
        else:
            return 0

    def getMin(self) -> int:
        return self.st_min[-1]
        
