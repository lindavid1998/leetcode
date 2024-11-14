# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Time: O(n^2)
        Space: O(n^2)

        To understand complexity, imagine you have a degenerate tree (linked list)
        On each iteration, to get the index of the root, it will need to traverse across
        the entire array

        It does this n times until the end of the list is reached

        Similarly, this means space will be quadratic because on each recursive call,
        a new array of size n needs to be created
        '''
        # base cases
        if not preorder or not inorder:
            return None

        # build root
        root = TreeNode(preorder[0])

        # split arrays
        rootIdx = inorder.index(root.val)  # O(n) 

        leftPre = preorder[1:rootIdx + 1]
        rightPre = preorder[rootIdx + 1:]

        leftIn = inorder[0:rootIdx]
        rightIn = inorder[rootIdx + 1:]

        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)
        
        return root

class Solution:
    def __init__(self):
        self.cache = {} # value -> index

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Optimize previous solution by adding a hash map to track indices

        Time: O(n^2)
        Space: O(n^2)

        Time complexity still quadratic since array slicing is O(n) operation
        and it is called n times (one for each node)
        '''
        # base cases
        if not preorder or not inorder:
            return None

        # build root
        root = TreeNode(preorder[0])

        # split arrays
        if root.val in self.cache:
            rootIdx = self.cache[root.val]
        else:
            rootIdx = inorder.index(root.val)  # O(n) 
            self.cache[root.val] = rootIdx

        leftPre = preorder[1:rootIdx + 1]
        rightPre = preorder[rootIdx + 1:]

        leftIn = inorder[0:rootIdx]
        rightIn = inorder[rootIdx + 1:]

        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)
        
        return root
    

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Optimal solution, DFS with hash map

        Time: O(n), DFS is called on each node once
        Space: O(n) needed for hash map to track indices
        '''
        # O(n)
        self.indices = {}
        for i, n in enumerate(inorder):
            self.indices[n] = i
        
        self.preIdx = 0  # variable to track index of root in preorder arr

        def dfs(l, r):
            # returns root of tree defined by l, r pointers in the inorder arr
            if l > r:
                return None
            
            # get root val
            rootVal = preorder[self.preIdx]
            self.preIdx += 1

            # get root idx
            rootIdx = self.indices[rootVal]

            # construct tree
            root = TreeNode(rootVal)
            root.left = dfs(l, rootIdx - 1)
            root.right = dfs(rootIdx + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)