class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # top down dp with memoization
        # O(len(coins) * amount) time and space

        dp = {} # (i, amount) -> ways
        def dfs(i, amount):
            if amount == 0:
                return 1
            if amount < 0 or i == len(coins):
                return 0
            if (i, amount) in dp:
                return dp[(i, amount)]
        
            dp[(i, amount)] = dfs(i, amount - coins[i]) + dfs(i + 1, amount)
            return dp[(i, amount)]

        return dfs(0, amount)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # another top down dp with memoization
        # except decision tree iterates over coins instead of include vs exclude i'th coin
        # O(len(coins) * amount) time and space
        dp = {}
        def dfs(amt, i):
            if amt < 0:
                return 0
            if amt == 0:
                return 1
            if (amt, i) in dp:
                return dp[(amt, i)]
            
            dp[(amt, i)] = 0
            for j in range(i, len(coins)):
                dp[(amt, i)] += dfs(amt - coins[j], j)
            
            return dp[(amt, i)]
        
        return dfs(amount, 0)
    
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # bottom up dp
        # O(len(coins) * amount) time
        # O(amount) space
        
        dp = [0] * (amount + 1)
        N = len(coins)

        for i in range(N - 1, -1, -1):
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1 # base case

            for a in range(1, amount + 1):
                nextDp[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDp[a] += nextDp[a - coins[i]]
            
            dp = nextDp
        
        return dp[amount]