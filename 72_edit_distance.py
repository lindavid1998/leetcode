class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        Top down
        Time: O(len(word1) x len(word2))
        Space: O(len(word1) x len(word2))
        '''
        dp = {} # (i, j) -> min ops

        def dfs(i, j):
            # returns min ops to convert first i chars of word1 to first j chars
            # of word2
            if (i, j) in dp:
                return dp[(i, j)]

            # base case
            if i == 0:
                return j
            if j == 0:
                return i

            # recursive
            if word1[i - 1] == word2[j - 1]:
                return dfs(i - 1, j - 1)
            
            dp[(i, j)] = 1 + min(
                dfs(i - 1, j),
                dfs(i, j - 1),
                dfs(i - 1, j - 1)
            )

            return dp[(i, j)]
        
        n1 = len(word1)
        n2 = len(word2)

        return dfs(n1, n2)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] -> min # operations to convert first i chars of word1
        # to first j chars of word2

        n1 = len(word1)
        n2 = len(word2)

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        

        # fill base cases
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j

        print(dp)
        
        # iterate over table 
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],
                        dp[i - 1][j],
                        dp[i - 1][j - 1]
                    )
        
        return dp[n1][n2]
