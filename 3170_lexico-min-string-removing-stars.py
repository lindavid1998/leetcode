class Solution:
    def clearStars(self, s: str) -> str:
        """
        iterate over s
        use a priority queue to track the smallest chars seen so far and their last index
        when a * is found, pop from the queue to get the char (and its index) to remove

        removed chars are flagged with boolean, and then the res string is reconstructed by iterating
        over the boolean flags

        time: O(nlogn)
        space: O(n) heap + O(n) boolean
        """
        n = len(s)
        remove = [False] * n
        pq = []

        for i, c in enumerate(s):
            if c == '*':
                char_to_remove, j = heapq.heappop(pq)
                remove[-j] = True
                remove[i] = True
            else:
                heapq.heappush(pq, (c, -i))
        
        res = ""
        for i, c in enumerate(s):
            if not remove[i]:
                res += c
        return res

