class KthLargest:
    '''
    Maintain a min heap of size k
    the element at the top of the heap is the kth largest

    Init: O(nlog n) time
    Add: O(log k) time
    Space: O(k)
    '''

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # O(n)
        while len(self.heap) > k:
            heapq.heappop(self.heap) # O(log n)
        

    def add(self, val: int) -> int:
        # O(log k)
        heapq.heappush(self.heap, val) 
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap) 
        
        return self.heap[0]

