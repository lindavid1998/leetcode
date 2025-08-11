class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        prefix sum and hash table

        convert nums to binary array (even -> 0, odd -> 1)
        then find count of subarrays where sum == k

        efficiently find sums using prefix sum
        [1, 1, 0, 1, 1] -> nums
        [1, 2, 2, 3, 4] -> pre
        subarr nums[i:j+1] is nice if pre[j] - pre[i - 1] == k
        so for every j in nums, calculate pre[i - 1] = pre[j] - k
        this gives a target value
        the number of nice subarrays ending at j is the number of occurrences 
        of this target value prior to j. count occurrences in arr or hash map

        track sum of occurrences and return

        time: O(n)
        space: O(n)
        """
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] % 2

        pre = [0] * n
        for i in range(n):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = nums[i] + pre[i - 1]

        prefix_counts = [0] * (n + 1)
        prefix_counts[0] = 1 # sum of 0 exists with empty subarray

        res = 0
        for j in range(n):
            target = pre[j] - k
            if target >= 0:
                count = prefix_counts[target]
                res += count
            prefix_counts[pre[j]] += 1

        return res

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        sliding window

        exactly k odd numbers = subarrrays with at most k - subarr with
        at most k - 1

        time: O(n)
        """
        n = len(nums)

        def atMost(k):
            # sliding window
            l = r = odds = 0
            res = 0
            while r < n:
                if nums[r] % 2 == 1:
                    odds += 1

                while odds > k:
                    # invalid window, shrink
                    if nums[l] % 2 == 1:
                        odds -= 1
                    l += 1

                res += r - l + 1 # every subarray ending at r is valid
                r += 1
            return res

        return atMost(k) - atMost(k - 1)
