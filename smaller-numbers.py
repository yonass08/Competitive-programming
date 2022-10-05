class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list = [0] * 101
        result = []
        for i in nums:
            list[i] += 1
        for i in nums:
            result.append(sum(list[:i]))
        return result
        
