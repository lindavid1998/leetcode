class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        O(n + k) solution
        create array mapping count to values
        iterate from highest count and build res array until k elements found
        '''
        numToCount = defaultdict(int)
        for n in nums:
            numToCount[n] += 1
        
        countToValues = [[] for _ in range(len(nums) + 1)]
        for n in numToCount:
            count = numToCount[n]
            countToValues[count].append(n)

        res = []
        for i in range(len(nums), 0, -1):
            for num in countToValues[i]:
                res.append(num)
                if len(res) == k:
                    return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Use heap, O(nlogk) time, O(n) space
        Optimized by restricting heap size <= k
        '''
        numCount = defaultdict(int)
        for i, n in enumerate(nums):
            numCount[n] += 1
        
        heap = []
        for num in numCount:
            count = numCount[num]
            heapq.heappush(heap, [count, num])

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _ in range(k):
            tmp = heapq.heappop(heap)
            res.append(tmp[1])

        return res
