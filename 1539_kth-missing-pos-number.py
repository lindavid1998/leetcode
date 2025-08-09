class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # bin search
        # number of missing numbers is monotically increasing with i

        # num of missing numbers before arr[i] = arr[i] - (i + 1)
        # [1, 2, 4]
        # i = 2 -> expected to be 3 -> actual = 4 => 1 missing number (4-(3))

        # find smallest index where num of missing numbers >= k
        # answer = smallest index (num of nonmissing numbers) + k (number of missing numbers)

        n = len(arr)
        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2
            n_missing = arr[m] - (m + 1)

            if n_missing < k:
                l = m + 1
            else:
                r = m - 1
        
        return l + k
