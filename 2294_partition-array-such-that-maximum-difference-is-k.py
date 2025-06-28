class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        Sort + greedy

        we don't care about order of numbers in subsequence, only the number of subsequences
        so what we can do is sort
        add numbers to subsequence until the min-max constraint is violated
        when it is violated, start a new subsequence (increment count)

        time: O(nlogn) due to sorting
        space: O(1)
        """
        n = len(nums)

        nums.sort()

        minimum = nums[0]
        res = 1

        for i in range(1, n):
            if nums[i] - minimum > k:
                res += 1
                minimum = nums[i]
        
        return res

