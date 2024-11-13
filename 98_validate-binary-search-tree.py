# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        DFS
        Time: O(n)
        Space: O(n)
        
        Each node has to be between a min and a max based on its parent node

        Tree is valid if 1) root is between min, max 2) left tree is valid and 3) right tree is valid
        '''
        def dfs(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float('-inf'), float('inf'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        BFS
        Time: O(n)
        Space: O(n)
        '''
        q = deque()
        if root:
            q.append([root, -2000, 2000])

        while q:
            [cur, low, high] = q.popleft()
            if not low < cur.val < high:
                return False
            if cur.left:
                q.append([cur.left, low, cur.val])
            if cur.right:
                q.append([cur.right, cur.val, high])
        
        return True

