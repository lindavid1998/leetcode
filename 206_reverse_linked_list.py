# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Two pointers
        O(n) time, O(1) space
        '''
        prev = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Recursive
        Time: O(n)
        Space: O(n)
        '''
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        # reverse root.next
        newHead = self.reverseList(head.next)

        # append original head to end of reversed list
        head.next.next = head
        head.next = None
        
        return newHead
