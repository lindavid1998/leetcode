class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        brute force: find all subsequences of length k, return subsequence with largest sum
        O(n * 2^n)

        intuition: to get sum, pick the k largest elements
        k largest elements can be determined using a minHeap of size k
        iterate over nums, push to heap, pop if larger than k elements

        but need to return subsequence (maintain original order)
        so include index in minHeap
        and then sort by index in increasing order to recover the subsequence

        time: O(nlogk) bc each heap operation is log k and there are n elements that can be pushed
        space: O(k)
        """

        minHeap = []
        for i, n in enumerate(nums):
            heapq.heappush(minHeap, [n, i])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # recreate the subsequence
        minHeap.sort(key=lambda x: x[1])

        res = [n for n, i in minHeap]

        return res

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        O(nlogk + n)
        """
        # use heap to track top k elements
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        
        # get the count of each top k elements
        count = Counter(heap)
        res = []
        for n in nums: 
            if count[n] > 0:
                res.append(n)
                count[n] -= 1
            if len(res) == k:
                break
        return res

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        greedy
        time: O(n * k)
        space: O(1)
        """
        res = []
        minimum = float("-inf")
        minIdx = -1

        for num in nums:
            if len(res) < k:
                res.append(num)
                minimum = min(res)
                minIdx = res.index(minimum)
            elif len(res) == k:
                # replace the minimum number in res if num > minimum
                if num > minimum:
                    # remove minimum from res
                    res.pop(minIdx)

                    # append num to res
                    res.append(num)

                    # get the new minimum
                    minimum = min(res)
                    minIdx = res.index(minimum)
        
        return res
