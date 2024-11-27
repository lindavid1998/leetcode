'''
Given a list of instruments with their weights, values, and the maximum weight the module can carry, 
write a function to find the maximum total value that can be achieved.

'''

class Solution:
  def lunarPayload(self, n: int, weight: List[int], value: List[int], capacity: int) -> int:
    dp = {}
    
    def dfs(i, total_weight):
        if (i, total_weight) in dp:
            return dp[(i, total_weight)]
        if i == n:
            return 0
        
        res = dfs(i + 1, total_weight)
        if total_weight + weight[i] <= capacity:
            res = max(
                res,
                value[i] + dfs(i + 1, total_weight + weight[i])
            )
        
        dp[(i, total_weight)] = res
    
        return res
    
    return dfs(0, 0)
  

class Solution:
  def lunarPayload(self, n: int, weight: List[int], value: List[int], capacity: int) -> int:
    # dp[i][j] -> max value of payload from weight[i:] and current weight j 
    
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for j in range(capacity + 1):
            dp[i][j] = dp[i + 1][j]
            
            if j + weight[i] <= capacity:
                dp[i][j] = max(
                    dp[i][j], 
                    value[i] + dp[i + 1][j + weight[i]]
                )
    
    return dp[0][0]
