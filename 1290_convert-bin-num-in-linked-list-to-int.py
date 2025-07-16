# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # time: O(n) where n is size of list
        # space: O(1)
        res = 0
        cur = head
        while cur:
            res *= 2
            res += cur.val
            cur = cur.next

        return res
