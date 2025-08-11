class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        """
        Return the count of subarrays in nums that match the pattern.

        array problem
        range queries, sliding window
        use range queries to find whether adjacent numbers
        are same, incremented, or decremented

        match range query with pattern

        for example, 
        nums = [1,4,4,1,3,5,5,3]
        range_query = [1, 1, 0, -1, 1, 1, 0, -1]
        now look for pattern 1, 0, -1 in range query
        exclude index = 0 because that is just the start of nums

        time: O(n * m)
        space: O(n)

        note that the pattern search can be optimized with kmp
        """

        prev = 0
        range_query = []
        for num in nums:
            diff = num - prev
            if diff < 0:
                diff = -1
            elif diff > 0:
                diff = 1
            range_query.append(diff)
            prev = num
        
        count = 0
        for l in range(1, len(nums)):
            r = l + len(pattern) - 1
            if range_query[l:r + 1] == pattern:
                count += 1
        return count

