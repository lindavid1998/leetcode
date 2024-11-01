class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) time and space
        # top down dp with memoization

        N = len(prices)
        dp = {} # (i, hasStock) -> max profit
        def dfs(i, hasStock):
            # returns max profit from day i
            if i >= N:
                return 0
            if (i, hasStock) in dp:
                return dp[(i, hasStock)]
            
            profit = dfs(i + 1, hasStock) # profit from doing nothing
            if hasStock:
                # pick between max of doing nothing vs selling
                dp[(i, hasStock)] = max(profit, prices[i] + dfs(i + 2, False))
            else:
                # pick between max of doing nothing vs buying
                dp[(i, hasStock)] = max(profit, dfs(i + 1, True) - prices[i])
            
            return dp[(i, hasStock)]
        
        return dfs(0, False)
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(2^n) time, O(n) space DFS solution
        # TLE

        N = len(prices)
        def dfs(i, hasStock):
            if i >= N:
                return 0
            
            profit = dfs(i + 1, hasStock) 
            if hasStock:
                profit = max(profit, prices[i] + dfs(i + 2, False))
            else:
                profit = max(profit, dfs(i + 1, True) - prices[i])
            
            return profit
        
        return dfs(0, False)