class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinctCharacters = []
        repeat = None
        slow, fast = 0, 0
        maxCount = 0
        
        while fast < len(s):
            if s[fast] in distinctCharacters:
                repeat = s[fast]
            distinctCharacters.append(s[fast])
            
            
            while repeat:
                if s[slow] == repeat:
                    repeat = None
                    
                distinctCharacters.remove(s[slow])
                slow += 1
                
            maxCount = max(maxCount, fast - slow + 1)
            fast += 1
            
        return maxCount
