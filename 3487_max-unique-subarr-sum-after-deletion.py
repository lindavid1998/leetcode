class Solution:
    def maxSum(self, nums: List[int]) -> int:
        """
        Filter out duplicates
        Then add up all the positive numbers
        If no positive numbers, then return max of nums (subarray cannot
        be empty)

        Time: O(n)
        Space: O(n)
        """
        unique = set(nums)
        res = 0
        all_neg = True
        for n in unique:
            if n > 0:
                all_neg = False
                res += n
        
        return max(nums) if all_neg else res
