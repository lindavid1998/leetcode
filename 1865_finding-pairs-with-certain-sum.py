class FindSumPairs:
    """
    Intuition:
    nums1 is small relative to nums2
    so we can afford to iterate over nums1

    maintain a frequency map for nums2
    when counting pairs, iterate over nums1 and check if its complement
    is in the hash table (just like Two Sum)
    if it is, add the count to res

    when updating nums2, be sure to update the frequency map
    decrement the old value
    increment the new value

    Time:
    - add O(1)
    - count O(n) where n is len(nums1)
    
    Space:
    - frequency map for nums2 -> O(m) where m is len(nums2)
    """

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        cur = self.nums2[index]
        self.freq[cur] -= 1

        new_val = cur + val
        self.nums2[index] = new_val
        self.freq[new_val] += 1

    def count(self, tot: int) -> int:
        res = 0
        for n in self.nums1:
            target = tot - n
            if target in self.freq:
                res += self.freq[target]

        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
