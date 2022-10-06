class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        last = nums[length - k:]
        
        for i in range(length-1, k-1, -1):
            nums[i] = nums[i-k]
        
        for i in range(k):
            nums[i] = last[i]
