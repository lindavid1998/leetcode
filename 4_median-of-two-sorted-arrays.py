class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        find the left portion of the merged array (without merge + sorting)
        the median is the number that comes after the end of the left portion

        the left portion of the merged array is constructed from the left portions of num1 and num2
        the objective is to find which numbers in num1 and num2 belong in the left portion 

        this can be achieved with binary search on the smaller array
        '''
        A = nums1
        B = nums2

        if len(nums2) < len(nums1):
            A = nums2
            B = nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2
        l = 0
        r = len(A) - 1
        
        while True:
            # i and j are the idxes that represent the end (inclusive) of the left portions in each array
            i = (l + r) // 2
            j = half - i - 2 

            # Aleft and Bleft are the last numbers in the left portions
            # Aright and Bright are the first numbers in the right portions
            Aleft = float('-inf') if i < 0 else A[i] 
            Aright = float('inf') if i >= len(A) - 1 else A[i + 1]
            Bleft = float('-inf') if j < 0 else B[j]
            Bright = float('inf') if j >= len(B) - 1 else B[j + 1]

            if Aleft <= Bright and Bleft <= Aright:
                # median found
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Bleft > Aright:
                # left portion of B has numbers that are too large
                # reduce size of B by increasing size of A
                l = i + 1
            else:
                # reduce size of A
                r = i - 1

