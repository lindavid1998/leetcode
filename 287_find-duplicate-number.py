class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's cycle detection
        # O(n)

        s = 0
        f = 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        
        s2 = 0
        while nums[s] != nums[s2]:
            s = nums[s]
            s2 = nums[s2]
        return nums[s]