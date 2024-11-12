# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Two pointers
        Sum values at two pointers and create node
        Iterate down both lists until there are no more nodes

        Time: O(max(m,n)))
        Space: O(1)
        '''
        carry = 0
        dummy = ListNode()
        cur = dummy

        while l1 or l2:
            total = carry
            if l1:
                total += l1.val
            if l2:
                total += l2.val

            carry = total // 10  
            total = total % 10
            
            newNode = ListNode(total)
            cur.next = newNode
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            newNode = ListNode(carry)
            cur.next = newNode

        return dummy.next
