# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal, but return when the kth element is found
        # instead of traversing the whole tree
        # O(k) so slightly better than O(n) time
        # O(log n) space if tree balanced, otherwise O(n) space 

        s = [] # stack
        cur = root

        while s or cur:
            # build stack using nodes on the left
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
