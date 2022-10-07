class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longestCount = 0
        flipCount = 0
        
        start, end = 0, 0
        while end < len(nums):
            if nums[end] == 0:
                flipCount += 1
            
            while flipCount > k:
                if nums[start] == 0:
                    flipCount -= 1
                start += 1

                
            longestCount = max(longestCount, end - start + 1)
            end += 1
        
        return longestCount
