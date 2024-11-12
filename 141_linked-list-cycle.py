# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Two pointers, fast and slow
        Time: O(n)
        Space: O(1) 
        '''
        s = head
        f = head.next

        while f and f.next:
            if s == f:
                return True
            s = s.next
            f = f.next.next
        
        return False
