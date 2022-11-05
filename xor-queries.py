class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorPrefix = [0]
        
        for num in arr:
            xorPrefix.append(xorPrefix[-1] ^ num)

        res = []
        for query in queries:
            res.append(xorPrefix[query[0]] ^ xorPrefix[query[1]+1])

        return res
