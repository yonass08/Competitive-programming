class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        monotonicStack = []
        
        for i in nums2:
            while monotonicStack != [] and i > monotonicStack[-1]:
                elem = monotonicStack.pop()
                if elem in nums1:
                    result[nums1.index(elem)] = i
            monotonicStack.append(i)
            
        return result
            
                
       
