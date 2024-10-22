class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dynamic programming solution
        N = len(nums)
        LIS = [1] * N
        # LIS[i] = longest increasing subsequence starting at idx i

        # build the LIS array from the back
        for i in range(N-1,-1,-1):
            for j in range(i+1,N):
                # if current num can extend an existing subsequence
                if nums[i] < nums[j]:
                    # overwrite LIS[i] if a new longest length found
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)