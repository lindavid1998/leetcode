class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # the key intuition is that if there's a valid split,
        # the majority element in the left and right subarrays will be the same
        # majority element of the original array

        # proof:
        # let x be the majority element in arr1 and arr2, which have lengths A and B
        # respectively. that means the total count of x is > (A/2 + B/2) 
        # let n = the size of the original arr = A + B
        # then count of x > N/2, making x the majority element 

        # get the majority element and its count
        # use Boyer-Moore algo
        # see https://leetcode.com/problems/majority-element/description/
        majority = nums[0]
        count = 0
        for i, n in enumerate(nums):
            if count == 0:
                majority = n
                count = 1
            elif n == majority:
                count += 1
            else:
                count -= 1
        
        n = len(nums)

        # map index i to count of majority element in nums[:i + 1]
        total = 0
        for num in nums:
            if num == majority:
                total += 1

        left_count = 0
        for i in range(n - 1):
            if nums[i] == majority:
                left_count += 1
            right_count = total - left_count
            # if freq * 2 are larger than the arr sizes, return i
            if left_count * 2 > (i + 1) and right_count * 2 > (n - i - 1):
                return i
        
        return -1
