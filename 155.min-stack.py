class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # min should be index to smallest element
        self.min = None

    def push(self, x: int) -> None:
        # increase size of array if not dynamically allocated array language
        # but python, it is
        self.stack.append(x)
        
        self.getMin()

    def pop(self) -> None:
        if self.stack:
            self.stack = self.stack[:len(self.stack)-1]
        
            # check if we removed min
            if self.min >= len(self.stack)-1:
                self.getMin()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        if self.min is None and self.stack:
            self.min = 0
            return self.stack[0]
        elif not self.stack:
            self.min = None
            return
        elif self.min is not None:
            tmp = 0
            for i in range(len(self.stack)):
                if self.stack[tmp] > self.stack[i]:
                    tmp = i
                    
            self.min = tmp
            return self.stack[self.min]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()