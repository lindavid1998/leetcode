# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Recursive solution

        Example: [0, 1, 2, 3, 4, 5, 6]
        The recursive case is [0, 6] + reorder([1, 2, 3, 4, 5])

        Time: O(n^2) since list is traversed on each recursive call
        Space: O(n)
        '''
        if not head or not head.next or not head.next.next:
            return
        
        # traverse over list to get tail
        prev = head
        tail = head.next
        while tail.next:
            tail = tail.next
            prev = prev.next
        tmp = head.next
        head.next = tail
        prev.next = None

        # reorder middle of list
        tail.next = tmp
        self.reorderList(tmp)

