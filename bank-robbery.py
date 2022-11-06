class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return list(range(len(security)))
        
        decreasing = []
        increasing = set()

        count = 1
        for i in range(1, len(security)):
            if security[i] <= security[i-1]:
                count += 1
            else:
                count = 1

            if count == time+1:
                decreasing.append(i)
                count -= 1

        count = 1
        for i in range(1, len(security)):
            if security[i] >= security[i-1]:
                count += 1
            else:
                count = 1

            if count == time+1:
                increasing.add(i - time )
                count -= 1

        res = []
        for i in decreasing:
            if i in increasing: res.append(i)

        return res
