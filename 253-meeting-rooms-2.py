"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # O(nlogn)
        # minHeap contains end times of meetings in progress
        # size of minHeap = number of overlapping meetings = number of rooms needed 
        
        intervals.sort(key=lambda i:i.start) # O(n log n)
        if len(intervals) == 0:
            return 0

        minHeap = [intervals[0].end]
        heapq.heapify(minHeap) 
        res = 1
        # iterate over each meeting time
        for i in range(1, len(intervals)):
            # if it starts after the meeting with the earliest end time
            while minHeap and intervals[i].start >= minHeap[0]:
                # remove that meeting from the heap
                heapq.heappop(minHeap) # O(log n)
            heapq.heappush(minHeap, intervals[i].end)
            res = max(res, len(minHeap))
        
        return res