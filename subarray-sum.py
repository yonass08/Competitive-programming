class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0 
        currentSum = 0
        prefixes = {0: 1}
        
        for i in nums:
            currentSum += i
            diff = currentSum - k
            answer += prefixes.get(diff, 0)
            prefixes[currentSum] = prefixes.get(currentSum, 0) + 1
            
        return answer
