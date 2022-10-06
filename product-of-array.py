class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        for i in range(len(nums) - 1):
            result.append(result[i] * nums[i])
            
        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= rightProduct
            rightProduct *= nums[i]
            
        return result
