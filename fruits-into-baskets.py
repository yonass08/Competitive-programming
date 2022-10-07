class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        maxCount = 0
        slow, fast = 0, 0
        
        while fast < len(fruits):
            freq[fruits[fast]] = freq.get(fruits[fast], 0) + 1
            
            while len(freq.keys()) > 2:
                freq[fruits[slow]] -= 1
                if freq[fruits[slow]] == 0:
                    del freq[fruits[slow]]
                slow += 1
            
            maxCount = max(maxCount, fast - slow + 1)
            
            fast += 1
        
        return maxCount
