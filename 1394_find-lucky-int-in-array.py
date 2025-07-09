class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        Two solutions

        Approach 1: Hash map, counting
        Time: O(n)
        Space: O(n)
        """
        res = -1

        num_to_count = Counter(arr)

        for num, count in num_to_count.items():
            if num == count:
                res = max(res, num)

        return res

        """
        Approach 2: Sorting, count consecutive numbers
        Time: O(nlogn) for sorting
        Space: O(1)

        """

        arr.sort(reverse=True)

        i = 0
        n = len(arr)

        while i < n:
            count = 1
            while i < n - 1 and arr[i + 1] == arr[i]:
                count += 1
                i += 1
            if count == arr[i]:
                return arr[i]
            i += 1

        return -1

