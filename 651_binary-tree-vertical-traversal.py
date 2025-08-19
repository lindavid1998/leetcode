from typing import (
    List,
)
from collections import defaultdict

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def vertical_order(self, test_root_1: TreeNode) -> List[List[int]]:
        """
        each node has a row, column determined by the r, c of its parent
        except the root which starts at 0, 0

        use DFS to map column index to list of nodes in column
        sort by column index, then add each column's node values to res

        since binary tree, no need to worry about cycles and tracking visited nodes

        time: O(n)
        space: O(n) recursive stack for dfs, O(n) for hash map tracking nodes in column
        """
        col_idx_to_nodes = defaultdict(list)

        def dfs(r, c, node):
            if not node:
                return
            col_idx_to_nodes[c].append(node)
            dfs(r + 1, c - 1, node.left)
            dfs(r + 1, c + 1, node.right)
        
        dfs(0, 0, test_root_1)

        col_idx_to_nodes_list = list(col_idx_to_nodes.items())

        col_idx_to_nodes_list.sort()

        res = []
        for idx, nodes_list in col_idx_to_nodes_list:
            column = []
            for node in nodes_list:
                column.append(node.val)
            res.append(column)
        
        print(res)
        return res


solution = Solution()

test_root_1 = TreeNode(3)
test_root_1.left = TreeNode(9)
test_root_1.right = TreeNode(20)
test_root_1.right.left = TreeNode(15)
test_root_1.right.right = TreeNode(7)


solution.vertical_order(test_root_1)

test_root_2 = TreeNode(1)
test_root_2.left = TreeNode(2)
test_root_2.right = TreeNode(3)
test_root_2.right.right = TreeNode(4)

solution.vertical_order(test_root_2)

test_root_3 = TreeNode(1)
test_root_3.left = TreeNode(2)
test_root_3.left.left = TreeNode(4)
test_root_3.right = TreeNode(3)
test_root_3.right.right = TreeNode(5)

solution.vertical_order(test_root_3)