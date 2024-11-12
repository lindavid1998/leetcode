# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        DFS, O(n) time and space

        use depth to index into res array

        on each recursion, search left before right
        '''
        res = []
        def dfs(node, depth):
            if not node:
                return
            
            if len(res) == depth:
                res.append([])
            
            res[depth] = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        BFS
        Time: O(n)
        Space: O(n)
        '''
        q = deque()
        res = []

        if root:
            q.append(root)
        
        while q:
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                if i == n - 1:
                    res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        
        return res

