class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # O(1) space
        N = len(cost)
        
        # overwrite cost[i] to be min cost to reach goal, starting from goal
        # last two indices are unchanged
        # min cost to reach goal is cost to reach goal + lowest cost between the two reachable cells
        for i in range(N-3,-1,-1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1]) # can start from either idx 0 or 1

class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # O(1) space
        N = len(cost)
        dp1 = 0
        dp2 = 0

        for i in range(2, N + 1):
            res = min(
                dp2 + cost[i - 2],
                dp1 + cost[i - 1]
            )
            dp2 = dp1
            dp1 = res
        
        return res
    
class Solution3:
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        # O(n) space
        N = len(cost)
        dp = [0] * (N + 1)

        for i in range(2, N + 1):
            dp[i] = min(
                dp[i - 2] + cost[i - 2],
                dp[i - 1] + cost[i - 1]
            )
        
        return dp[N]