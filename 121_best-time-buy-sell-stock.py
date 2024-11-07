class Solution:
    def maxProfit(self, prices: List[int]) -> int:
	'''
	Two pointers, O(n)
	'''
        res = 0
        l = 0
        r = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)

            if prices[r] < prices[l]:
                l = r
            r += 1

        return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        DFS: O(2^n) time, O(n) space
	This gets TLE
        '''
        def dfs(i, profit, hasStock):
            if i == len(prices):
                return profit
            
            if hasStock:
                res = max(profit + prices[i], dfs(i + 1, profit, hasStock))
            else:
                res = max(
                    dfs(i + 1, profit - prices[i], True),
                    dfs(i + 1, profit, False)
                )

            return res
        
        return dfs(0, 0, False)

