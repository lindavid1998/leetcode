class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # let i track nums1
        # let j track nums2
        # let k track the final nums1 array

        # iterate from the back of each array
        # use the larger element to build the final array
        # repeat until there are no more elements in nums2 
        # even if there are still elements in nums1, they are already in the correct spot

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

