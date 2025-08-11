class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        track count of number of adjacent pairs
        adjust count on each update, checking neighbors of cell that is updated
        
        time: O(q)
        space: O(n) for colors, O(q) for res
        """
        def in_bounds(i):
            return i >= 0 and i < n

        colors = [0] * n
        num_pairs = 0
        res = [] 
        for idx, color in queries:
            l, r = idx - 1, idx + 1

            if colors[idx] != 0:
                # cell colored, check if recoloring it loses pairs
                if in_bounds(l) and colors[l] == colors[idx]:
                    num_pairs -= 1
                if in_bounds(r) and colors[r] == colors[idx]:
                    num_pairs -= 1

            # update colors array
            colors[idx] = color

            # update count of adjacent pairs
            if in_bounds(l) and colors[l] == colors[idx]:
                num_pairs += 1
            if in_bounds(r) and colors[r] == colors[idx]:
                num_pairs += 1
            
            res.append(num_pairs)
        
        return res

