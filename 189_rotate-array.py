class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time: O(n), space: O(n)
        # k = k % len(nums)
        # rotated = nums[-k:] + nums[:-k]
        # for i in range(len(nums)):
        #     nums[i] = rotated[i]

        # time: O(n), )space: O(1)
        # reverse whole list
        # reverse list[k:]
        # reverse list[:k]

        k = k % len(nums)

        l = 0
        r = len(nums) - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1
        
        l = k
        r = len(nums) - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1
        
        l = 0
        r = k - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1

