class MinStack:

    def __init__(self):
        self.vals = []
        self.minimum = float('inf')
        self.minima = []
        

    def push(self, val: int) -> None:
        if val < self.minimum:
            self.minimum = val
        self.minima.append(self.minimum)
        self.vals.append(val)


    def pop(self) -> None:
        # have to check if the global min is unchanged

        local_min = self.minima.pop()
        val = self.vals.pop()
        if self.minima and local_min == val:
            self.minimum = self.minima[-1]
        elif not self.minima:
            self.minimum = float('inf')
        

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.minimum

        
