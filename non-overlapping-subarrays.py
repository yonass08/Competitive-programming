class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        fSums = []
        sSums = []
        sums = 0
        maxSum = 0
        
        for i in range(len(nums)):
            sums += nums[i]
            if i >= firstLen-1:
                fSums.append(sums)
                sums -= nums[i - firstLen + 1]
                
            
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if i >= secondLen - 1:
                sSums.append(sums)
                sums -= nums[i - secondLen + 1]
                
            
        print(fSums)
        print(sSums)
        
        for i in range(len(fSums)):
            for j in range(len(sSums)):
                if j >= i and j-i < firstLen:
                    continue
                if i >= j and i-j < secondLen:
                    continue
                maxSum = max(maxSum, fSums[i] + sSums[j])
                
        return maxSum
        
