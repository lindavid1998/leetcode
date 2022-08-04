# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:11:21 2022

@author: David Lin
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Make a copy of 1st list
        result = list1[:]
        
        # Loop through 1st list
        for i in range(0, len(list1) - 1):
            
            current = list1[i]
            upcoming = list1[i + 1]
            
            # Find index of 1st element greater than or equal to current
            start = next(x for x, val in enumerate(list2) if val >= current)
            
            # Find index of 1st element greater than upcoming 
            end = next(x for x, val in enumerate(list2) if val > upcoming) 
            
            print(start)
            print(end)
            
            # Insert start and end list into result
            # temp = list2[start, end]
            
            # print(temp)

solution = Solution()
solution.mergeTwoLists([0, 1, 3, 5, 6], [1, 1, 1, 2, 3, 4])


