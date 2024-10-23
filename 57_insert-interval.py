class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        N = len(intervals)

        for i in range(N):
            # if spot to insert found, insert new interval and concat the rest of the intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # add the intervals in front 
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                continue
            
            # merge the intervals
            start = min(newInterval[0], intervals[i][0])
            end = max(newInterval[1], intervals[i][1])
            newInterval = [start, end]

        # insert new interval at end if it hasn't been inserted already
        res.append(newInterval)
        return res