class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Greedy, stack

        Prioritize removing the higher value pair first
        If "ab", track count of a's that are waiting to be paired (i.e. add to stack)
        When "b" found and there are open a's, then make the pairing and increment res
        Otherwise increment count of b's
        
        If at the end (or at an irrelevant char), count the number of pairs that can make
        the lower value pair and add to res
        (irrelevant chars acts as a reset, as you cannot make pairs that are 
        on different sides of it)

        why does greedy work? i.e. why prioritize higher value pairs? it gives more points
        per character. also removing lower pair means removing a char that can be used in a
        higher pair

        time complexity: O(n)
        space: O(1)
        """

        res = 0
        count_1 = count_2 = 0 # count_1 tracks the first char in the higher-value pair
        c1 = 'a'
        c2 = 'b'
        low = min(x, y) # value of low pair
        high = max(x, y) # value of high pair

        if y > x:
            # ba is the higher priority pair
            c1 = 'b'
            c2 = 'a'
        
        for c in s:
            if c == c1:
                count_1 += 1
            elif c == c2:
                if count_1 > 0:
                    # available to pair
                    count_1 -= 1
                    res += high
                else:
                    count_2 += 1
            else:
                # irrelevant char, which resets
                res += min(count_1, count_2) * low
                count_1 = count_2 = 0
        
        if count_1 > 0:
            res += min(count_1, count_2) * low

        return res
