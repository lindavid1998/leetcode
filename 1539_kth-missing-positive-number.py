class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # number of missing numbers before index i is
        # missing = arr[i] - (i + 1)

        # use bin search to find smallest index l where
        # missing numbers before l is >= k

        # ans = l + k
        # why?
        # when you finish the bin search and get l
        # it tells you that there are l non missing numbers before the missing
        # number
        # and since everything is strictly increasing we can just add l + k
        # i.e. l non missing numbers and k missing numbers

        # another way to think about it, the kth missing positive number is at
        # least k

        n = len(arr)
        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2

            missing = arr[m] - (m + 1)
            
            if missing < k:
                l = m + 1
            else:
                r = m - 1
            
        return l + k
