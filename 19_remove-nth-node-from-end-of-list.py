# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n) time, O(1) space
        # use two pointers, offset by n + 1 nodes
        # dummy node is needed for case where there's only 1 node

        dummy = ListNode()
        dummy.next = head

        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        slow = dummy
        
        # traverse until fast pointer reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # skip over node to remove
        slow.next = slow.next.next

        return dummy.next
