class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up dynamic programming

        # if a solution exists, the largest num of coins will be amount
        # therefore you are guaranteed to overwrite dp[i] if there's a solution
        dp = [(amount + 1)] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])

        return dp[amount] if dp[amount] != amount + 1 else -1 

        # recursive top down DP with memoization
        # O(amount * len(coins))
        # def dfs(n):
        #     if dp[n]: # it's already calculated, simply return it
        #         return dp[n]
        #     if n == 0:
        #         return 0
        #     dp[n] = float("inf")
        #     for coin in coins:
        #         if n - coin >= 0:
        #             dp[n] = min(dp[n], 1 + dfs(n - coin))
        #     return dp[n]
        
        # dp = collections.defaultdict(int)
        # res = dfs(amount)
        # return res if res != float("inf") else -1

        # without memoization, time complexity is O(len(coins)^amount)
        # def dfs(n):
        #     if n == 0:
        #         return 0
        #     res = float("inf")
        #     for coin in coins:
        #         if n - coin >= 0:
        #             res = min(res, 1 + dfs(n - coin))
        #     return res
        
        # dp = collections.defaultdict(int)
        # res = dfs(amount)
        # return res if res != float("inf") else -1