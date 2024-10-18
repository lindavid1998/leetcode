class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(n) time, O(1) space
        N = len(nums)
        if N < 3:
            return max(nums)
        
        nums[1] = max(nums[0], nums[1])
        for i in range(2, N):
            nums[i] = max(nums[i-1], nums[i] + nums[i-2])
        
        return nums[-1]