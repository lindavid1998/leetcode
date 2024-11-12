# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Two pointers
        Time: O(n)
        Space: O(1)
        '''
        dummy = ListNode()
        cur = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Recursive

        Pick smaller of the two heads -> newHead

        newHead.next = mergeTwoLists(list1.next, list2)
        OR
        mergeTwoLists(list1, list2.next)

        depending on which list was chosen

        Base case?
        if both are null, return null
        if one is null, return the other

        Time: O(n)
        Space: O(n) recursive depth
        '''
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            newHead = list1
            newHead.next = self.mergeTwoLists(list1.next, list2)
        else:
            newHead = list2
            newHead.next = self.mergeTwoLists(list1, list2.next)

        return newHead
