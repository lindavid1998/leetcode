class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # Binary search, prefix sum, difference array
        # Time: O((m + n)log m) where n is len(nums) and m is len(queries)
        # Space: O(n) for difference array

        # The minimum k can be found using binary search. To efficiently check whether 
        # the first k queries can create a zero array, use a difference array (each element represents diff
        # relative to previous element). The difference array captures range updates without
        # having to traverse over the entire nums array.
        # Otherwise processing each query would take O(n) time, resulting in an overall O(n x m) time.

        low = 0
        high = len(queries)

        if sum(nums) == 0:
            return 0

        while low < high:
            k = (low + high) // 2

            def check(k):
                # O(k + n)
                # k operations to create diff array, then n operations to check nums

                # init difference array
                diff = [0] * (len(nums) + 1)  # an extra element is needed due to how diff array is updated below
                
                for i in range(k):
                    # update difference array
                    # note that doing it this way removes time complexity dependency on len(nums)
                    l, r, val = queries[i]
                    diff[l] += val
                    diff[r + 1] -= val
                
                # init prefix sum
                pre = 0
                for i, n in enumerate(nums):
                    pre += diff[i]
                    if pre < n:
                        return False
                
                return True

            if check(k):
                # k is valid
                high = k
            else:
                low = k + 1
        
        return low if check(low) else -1
