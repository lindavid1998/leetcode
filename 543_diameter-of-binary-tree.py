# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        DFS
        Time: O(n)
        Space: O(n)
        '''
        self.diameter = 0
        
        def height(node):
            if not node:
                return -1

            diameter = height(node.left) + height(node.right) + 2
            self.diameter = max(self.diameter, diameter)
            
            return max(height(node.left), height(node.right)) + 1
        
        height(root)
        
        return self.diameter
