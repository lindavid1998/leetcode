class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(nlogn)
        res = 0
        intervals.sort()
        prevEnd = intervals[0][1]
        
        N = len(intervals)
        for i in range(1, N):
            if intervals[i][0] < prevEnd:
                # overlap found
                res += 1
                # keep interval with smallest end
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
        
        return res