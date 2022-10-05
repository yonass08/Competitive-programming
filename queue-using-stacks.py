class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []
        

    def push(self, x: int) -> None:
        while len(self.front) > 0:
            self.back.append(self.front.pop())
        self.front.append(x)
        while len(self.back) > 0:
            self.front.append(self.back.pop())
        

    def pop(self) -> int:
        return self.front.pop()
        

    def peek(self) -> int:
        return self.front[-1]
        

    def empty(self) -> bool:
        return len(self.front) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
