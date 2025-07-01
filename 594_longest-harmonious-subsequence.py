class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        sort + sliding window
        time: O(nlogn)
        time: O(1)
        """
        nums.sort()
        l = r = 0
        n = len(nums)

        res = 0

        while r < n:
            while nums[r] - nums[l] > 1:
                l += 1
            
            if nums[r] - nums[l] == 1:
                res = max(res, r - l + 1)
                
            r += 1

        return res

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        use hash table to track frequencies
        for every num in frequency table, check if next num exists. 
        if it does, add their frequencies and overwrite max

        time: O(n)
        space: O(n) 
        """

        res = 0
        num_to_count = Counter(nums)
        for num, count in num_to_count.items():
            if num + 1 in num_to_count:
                res = max(res, count + num_to_count[num + 1])
        
        return res

