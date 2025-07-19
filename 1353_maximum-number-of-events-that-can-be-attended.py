class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        intuition: greedy. process events in chronological order and attend events
        by prioritizing the events that end earliest
        this ensures days are freed up for future events

        use a minHeap to track end days of ongoing events.
        for each day, add events that start that day to minHeap and
        remove expired events from minHeap

        time: O(nlogn)
        space: O(n)
        """
        n = len(events)

        # process events in chronological order
        events.sort() 

        # track ongoing events in minHeap so
        # event with earliest end is prioritized
        minHeap = []

        res = 0 # count events
        i = 0 # index to track events
        day = 1 # track current day

        # while there are ongoing events or events left to process
        while minHeap or i < n:
            if not minHeap:
                # this allows us to skip ahead days
                day = events[i][0]

            while i < n and events[i][0] == day:
                # add all events starting on current day to heap
                heapq.heappush(minHeap, events[i][1]) # track ends
                i += 1
            
            # remove any expired events from PQ
            while minHeap and minHeap[0] < day:
                # event ended before cur day
                heapq.heappop(minHeap)
            
            if minHeap:
                # event is available to attend for current day
                res += 1 
                heapq.heappop(minHeap) # remove it from available events
                day += 1
        
        return res
