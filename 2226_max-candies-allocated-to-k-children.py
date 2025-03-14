class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Time: O(nlogm) where m = sum(candies) / k and n = len(candies)
        # Space: O(1)

        def get_num_piles(candies, amount):
            piles = 0
            for pile in candies:
                piles += pile // amount
            return piles

        total = sum(candies)
        if total < k:
            return 0
        
        low = 1
        high = total // k
        res = 0

        while low <= high:
            mid = (low + high) // 2

            if get_num_piles(candies, mid) < k:
                high = mid - 1
            else:
                res = mid
                low = mid + 1
        
        return res
