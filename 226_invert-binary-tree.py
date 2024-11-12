# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        DFS, recursive

        Time: O(n)
        Space: O(log n) if balanced, O(n) otherwise
        '''
        if not root:
            return None

        right = self.invertTree(root.left)
        left = self.invertTree(root.right)

        root.left = left
        root.right = right

        return root
