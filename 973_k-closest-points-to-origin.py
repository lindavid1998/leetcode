class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        minHeap of [dist, x, y]

        dist = x^2 + y^2 

        Time: O(nlogn + klogn)
        Space: O(n)
        '''
        heap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, [dist, x, y])
        
        res = []
        for _ in range(k):
            [dist, x, y] = heapq.heappop(heap)
            res.append([x, y])
        
        return res

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        maxHeap, optimization over minHeap
        
        restrict maxHeap to size k

        Time: O(nlogk + klogk)
        Space: O(k)
        '''
        heap = []
        for x, y in points:
            d = x ** 2 + y ** 2
            heapq.heappush(heap, [-1 * d, x, y])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            [d, x, y] = heapq.heappop(heap)
            res.append([x, y])
        
        return res
