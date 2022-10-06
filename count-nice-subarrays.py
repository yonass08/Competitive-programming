class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddnessMap = [i%2 for i in nums]
        count = 0 

        currentSum = 0
        prefixes = {0: 1}
        
        for i in oddnessMap:
            currentSum += i
            diff = currentSum - k
            count += prefixes.get(diff, 0)
            prefixes[currentSum] = prefixes.get(currentSum, 0) + 1
       
        return count
