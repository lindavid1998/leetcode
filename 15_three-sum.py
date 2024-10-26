class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2)
        res = []
        nums.sort()
        N = len(nums)

        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = 0 - nums[i]
            l = i + 1
            r = N - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
        
        return res
