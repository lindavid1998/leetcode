# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal, but return when the kth element is found
        # O(n) but better than traversing whole tree
        # O(log n) space if tree balanced, otherwise O(n) space 

        s = [] # stack
        cur = root

        while s or cur:
            # build stack by traversing to the left on branch
            while cur:
                s.append(cur)
                cur = cur.left
            cur = s.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right # explore right subtree of current node


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # O(n) time and space
        # get inorder traversal, which returns nodes in sorted order

        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        inorder_arr = inorder(root)
        return inorder_arr[k - 1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        DFS
        Time: O(n)
        Space: O(n)

        Traversing to the left will always give you the smallest value.
        Each time end of left subtree is reached, repeat search on right subtree
        '''
        self.res = -1
        self.count = k
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.count -= 1
            if self.count == 0:
                self.res = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return self.res

