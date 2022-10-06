class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted = []
        
    def insertSort(self, val: int) -> None:
        if len(self.sorted) == 0:
            self.sorted.append(val)
        else:
            i = 0
            while (i < len(self.sorted)):
                if (val <= self.sorted[i]):
                    self.sorted.insert(i, val)
                    break
                i += 1
            if i == len(self.sorted):
                self.sorted.append(val)
                
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.insertSort(val)

        

    def pop(self) -> None:
        self.sorted.remove(self.stack.pop())


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.sorted[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
