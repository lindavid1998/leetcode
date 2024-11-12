"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Recursively copy nodes, using hash table to store previously copied nodes

        Time: O(n)
        Space: O(n)
        '''
        nodeToCopy = { None:None }
        def dfs(node):
            if node in nodeToCopy:
                return nodeToCopy[node]
            
            copy = Node(node.val)
            nodeToCopy[node] = copy
            copy.next = dfs(node.next)
            copy.random = dfs(node.random)

            return copy
        
        return dfs(head)

