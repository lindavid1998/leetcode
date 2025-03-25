class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Time: O(nlogn)
        # Space: O(n)
        # Merge intervals, each interval represents the range of values (x or y)
        # that the rectangles span
        # Need at least 3 intervals to be valid

        def check(intervals):
            # sort by start
            intervals.sort()
            count = 0

            # use max_end to track overlaps
            max_end = intervals[0][1]
            for start, end in intervals:
                if max_end <= start:
                    count += 1
                max_end = max(max_end, end)
            return count >= 2
        
        x_intervals = [[start_x, end_x] for start_x, _, end_x, _ in rectangles]
        y_intervals = [[start_y, end_y] for _, start_y, _, end_y in rectangles]

        return check(x_intervals) or check(y_intervals)
