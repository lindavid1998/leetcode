class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''
        The relations between the vowels can be represented as a graph
        The goal is then to find the number of paths with length n in the graph

        Let dp[n][char] represent the number of paths of length n that end with char
        To find dp[n][char], we need to find the number of paths to the letters that precede char

        In other words, dp[n][char] = sum of dp[n - 1][prev] such that there is an edge from prev to char

        We can represent the vowels as indices from 0 to 4
        '''
        preceding_chars = [
            [1, 2, 4],
            [0, 2],
            [1, 3],
            [2],
            [2, 3]
        ]

        dp = [[0] * 5 for _ in range(n + 1)]

        # base case
        for i in range(5):
            dp[1][i] = 1
        
        for i in range(2, n + 1):
            for c in range(5):
                for p in preceding_chars[c]:
                    dp[i][c] += dp[i - 1][p]
        
        res = 0
        for i in range(5):
            res += dp[n][i]
        
        return res % (10 ** 9 + 7)
    

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''
        DFS solution with memoization
        '''
        
        next_chars = {
            'a': 'e',
            'e': 'ai',
            'i': 'aeou',
            'o': 'iu',
            'u': 'a',
            'z': 'aeiou'
        }

        dp = {}
        def dfs(i, prev):
            if (i, prev) in dp:
                return dp[(i, prev)]
            if i == n:
                return 1
            
            res = 0
            chars = next_chars[prev]
            for c in chars:
                res += dfs(i + 1, c)
            
            dp[(i, prev)] = res
            
            return res
        
        res = dfs(0, 'z') 
        
        return res % (10 ** 9 + 7)