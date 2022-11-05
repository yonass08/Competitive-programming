class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = []

        for trip in trips:
            diff += [(trip[1], trip[0]), (trip[2], -trip[0])]
        diff.sort()

        carried = 0
        for item in diff:
            carried += item[1]
            if carried > capacity: return False

        return True
