# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # returns [height, balanced]
            if not node:
                return [0, True]
            
            left = dfs(node.left)
            right = dfs(node.right)

            height = max(left[0], right[0]) + 1
            balanced = left[1] and right[1] and abs(left[0] - right[0]) < 2

            return [height, balanced]
        
        return dfs(root)[1]
