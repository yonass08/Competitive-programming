class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        
        if citations[0] >= n:
            return n
        
        for i in range(1, n):
            if citations[i] >= n-i and citations[i-1] <= n-i:
                return n-i
            
        return 0
    
