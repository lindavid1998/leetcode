class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        O(n) time and space
        Maintain a set. Find the beginning of a sequence.
        Keep looking for the next number until end of sequence.
        '''
        res = 0
        numSet = set(nums)

        for n in nums:
            if n - 1 not in numSet:
                count = 1
                while n + count in numSet:
                    count += 1
                res = max(res, count)

        return res
