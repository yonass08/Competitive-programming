class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop = 0
        stack = []
        
        for push in pushed:
            stack.append(push)
            while stack != [] and stack[-1] == popped[pop]:
                stack.pop()
                pop += 1
            
        return stack == []
            
                
