class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        maxHeap

        pop twice
        if x != y, get abs(x-y) and add it back to heap
        repeat until size of heap is <= 1

        Time: O(nlogn)
        Space: O(n)
        '''
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -1 * heapq.heappop(maxHeap)
            y = -1 * heapq.heappop(maxHeap)

            if x != y:
                z = abs(x - y)
                heapq.heappush(maxHeap, -1 * z)
        
        return -1 * maxHeap[0] if maxHeap else 0

