class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        
        left = 0
        right = len(tokens)-1
        
        
        while left <= right:
            power -= tokens[left]
            if power < 0:
                if score == 0: break
                power += tokens[right]
                score -= 1
                right -= 1
            
            score += 1
            left += 1
            
        return score
            
