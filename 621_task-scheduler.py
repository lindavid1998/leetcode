class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Time: O(tlogt) where t is len(tasks)
        Space: O(t)

        Use priority queue to schedule highest freq tasks
        Use queue to hold tasks until cooldown expires, then add them
        back to priority queue
        '''
        count = defaultdict(int) # letter to count
        for t in tasks:
            count[t] -= 1 # maintain negative count for maxHeap
        
        maxHeap = list(count.values())
        heapq.heapify(maxHeap) 
        q = deque() # [cycle, qty]
        cycles = 0
        while maxHeap or q:
            if q and q[0][0] == cycles:
                cur = q.popleft()
                heapq.heappush(maxHeap, cur[1])
            
            if maxHeap:
                qty = heapq.heappop(maxHeap)
                if qty < -1:
                    q.append([cycles + n + 1, qty + 1])
            cycles += 1
        
        return cycles
