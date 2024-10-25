"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        N = len(intervals)
        for i in range(N):
            if i + 1 < N and intervals[i].end > intervals[i + 1].start:
                return False
        
        return True