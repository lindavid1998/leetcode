class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        
        # sort the array from start
        intervals.sort()

        res = []
        N = len(intervals)
        for i in range(N):
            # if interval overlaps with next, merge and overwrite next
            if i + 1 < N and intervals[i][1] >= intervals[i + 1][0]:
                start = min(intervals[i][0], intervals[i + 1][0])
                end = max(intervals[i][1], intervals[i + 1][1])
                intervals[i + 1] = [start, end]
            # if there's no overlap, then add current interval to res
            else:
                res.append(intervals[i])

        return res