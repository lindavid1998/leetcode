class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # DFS backtracking solution O(2^n)

        if sum(nums) % 2:
            return False
        
        target = sum(nums) / 2

        def dfs(i, total):
            if total == target:
                return True
            if total > target or i >= len(nums):
                return False
            
            return dfs(i+1, total+nums[i]) or dfs(i+1, total)
        
        return dfs(0,0)
    
        # DFS solution O(n * sum(nums))
        # with caching

        if sum(nums) % 2:
            return False
        
        cache = {}
        target = sum(nums) / 2

        def dfs(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            
            if total > target or i >= len(nums):
                cache[(i, total)] = False
                return False
            if total == target:
                cache[(i, total)] = True
                return True
            
            cache[(i, total)] = dfs(i+1, total+nums[i]) or dfs(i+1, total)

            return cache[(i, total)]
        
        return dfs(0,0)
    
        # Iterative solution O(n * sum(nums))
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) / 2
        
        dp = set()
        dp.add(0)

        for num in nums:
            new_dp = set()
            for total in dp:
                new_dp.add(total)
                new_dp.add(total + num)
                if total + num == target:
                    return True
            dp = new_dp
        
        return False
            