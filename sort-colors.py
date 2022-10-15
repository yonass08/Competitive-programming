class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0, 0, 0]
        
        for i in nums:
            freq[i] += 1
            
        for i in range(len(nums)):
            nums[i] = 0 if i < freq[0] else ( 1 if i < freq[0] + freq[1] else 2)
            
