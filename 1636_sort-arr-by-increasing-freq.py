class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # sort by incresing freq first, then by decreasing value
        numToCount = collections.Counter(nums)

        res = sorted(nums, key = lambda x: (numToCount[x], -x))

        return res