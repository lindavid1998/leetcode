class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Time: O(nqlogq)
        # Space: O(q)
        # Intuition: the value of each nums[i] tells you the min number of queries that need to be picked to
        # get nums[i] to 0. for each i, pick the queries with the farthest end for more coverage

        queries.sort(key = lambda x: x[0]) # sort queries by start time
        count = 0
        avail = [] # maxHeap of range ends
        active = [] # minHeap of range ends
        n = len(nums)
        k = 0 # index to track queries that have been added to available

        for i in range(n):
            # get rid of any queries that are no longer active
            while active and i > active[0]:
                heapq.heappop(active)
            
            # calculate how many queries are needed for nums[i]
            need = nums[i] - len(active)

            # add available queries 
            while k < len(queries) and queries[k][0] <= i:
                heapq.heappush(avail, -queries[k][1])
                k += 1
            
            # keep picking queries with farthest end until need is satisfied, or queries run out
            while need > 0:
                if len(avail) == 0:
                    return -1
                
                # only use ranges that include i
                end = -1 * heapq.heappop(avail)
                if end < i:
                    # no more ranges that can be used
                    return -1

                heapq.heappush(active, end)
                need -= 1
                count += 1

        return len(queries) - count

