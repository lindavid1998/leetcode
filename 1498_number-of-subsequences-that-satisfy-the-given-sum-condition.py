class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        two pointers

        sorting makes it easier to sum min and max in any subarray
        if min and max in a sorted subarray satisfy condition, then all subsequences with that same min in the
        subarray are valid
        
        it is like two sum, except now we are counting subsequences each time the sum to target is satisfied

        time: O(nlogn)
        space: O(1)
        """
        nums.sort()
        n = len(nums)
        res = 0
        mod = 10 ** 9 + 7

        l = 0
        r = n - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        
        return res % mod
