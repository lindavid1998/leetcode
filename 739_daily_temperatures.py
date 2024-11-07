class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        O(n) time and space

        use monotonic decreasing stack
        the [idx, temperature] pairs in the stack represent all the days that are
        pending a hotter day
        '''
        stack = [] # (i, temperature)
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                j, temp = stack.pop()
                res[j] = i - j
            stack.append([i, t])
        return res
