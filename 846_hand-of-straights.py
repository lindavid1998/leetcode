class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # O(n * log(m))
        # n is size of hand
        # m is unique values 
        
        # get mapping of value -> count
        count = collections.defaultdict(int)
        for card in hand:
            count[card] += 1
        
        # create a minHeap for unique card values
        values = list(count.keys())
        heapq.heapify(values)

        while count:
            target = values[0]
            for _ in range(groupSize):
                if target not in count:
                    return False
                count[target] -= 1
                
                if count[target] == 0:
                    del count[target]
                    heapq.heappop(values)
                target += 1

        return True