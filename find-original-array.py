class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        
        result = []
        hash_map = {}
        changed.sort()
        
        for num in changed:
            hash_map[num] = hash_map.get(num, 0) + 1
            
        for num in changed:
            if hash_map[num] == 0:
                continue
            if hash_map.get(num * 2, 0) == 0:
                return []
            
            result.append(num)
            hash_map[num] -= 1
            hash_map[num * 2] -= 1
            
        return result
                
        
