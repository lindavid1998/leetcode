class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(log n) time, O(1) space
        
        # rotated array has a left and right portion
        # which pointers to move in binary search depends on which half
        # the middle index is in 

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # if idx M is in left half
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1

        return -1

