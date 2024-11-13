# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        DFS
        Time: O(n)
        Space: O(n)
        '''
        self.count = 0
        def dfs(node, maxVal):
            if not node:
                return
            if node.val >= maxVal:
                self.count += 1
            
            dfs(node.left, max(maxVal, node.val))
            dfs(node.right, max(maxVal, node.val))
    
        dfs(root, -999)
        return self.count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        BFS
        Time: O(n)
        Space: O(n)
        '''
        count = 0
        q = deque()
        if root:
            q.append([root, -999])
        
        while q:
            [cur, maxVal] = q.popleft()
            if cur.val >= maxVal:
                count += 1
            if cur.left:
                q.append([cur.left, max(maxVal, cur.val)])
            if cur.right:
                q.append([cur.right, max(maxVal, cur.val)])
        
        return count
