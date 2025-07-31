class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        """
        subarrays are contiguous so to find all the unique bitwise
        OR values that end at index i, we extend all unique OR values
        that end at the previous index i - 1 (and also include nums[i]
        itself). we can track OR values from the previous index in a set

        iterate over array and keep track of all the unique values found
        in a set, updating on each iteration
        then return the length of set

        time: O(n * k) where k is the the number of unique OR values
        space: O(k)

        how large is k? 32? for 32 bit int
        when doing bitwise ORs, once a bit is flipped, it cannot be
        switched "off"
        therefore number of distinct ORs is bounded
        ex: if you have bits 0101, you can never get to 0011
        """
        n = len(arr)
        res = set()
        prev = set()

        for i in range(n):
            cur_set = {arr[i]}
            for val in prev:
                cur_set.add(arr[i] | val)
            res.update(cur_set)
            prev = cur_set

        return len(res)
