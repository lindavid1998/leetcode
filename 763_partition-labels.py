class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # O(n) time and space
        # problem becomes an interval problem. need to merge any overlapping intervals
        # each interval is a substring 

        # create table of char -> start, end
        charFirstLast  = {}
        for i, c in enumerate(s):
            if c not in charFirstLast :
                charFirstLast [c] = [i, i]
            else:
                charFirstLast [c][1] = i

        intervals = list(charFirstLast .values())

        res = []
        for i, interval in enumerate(intervals):
            start, end = interval
            # if it overlaps with next interval
            if i + 1 < len(intervals) and end > intervals[i + 1][0]:
                # merge and overwrite next interval
                nxtStart, nxtEnd = intervals[i + 1]
                intervals[i + 1] = [min(start, nxtStart), max(end, nxtEnd)]
            else:
                res.append(end - start + 1)
        
        return res