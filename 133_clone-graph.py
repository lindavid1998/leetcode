"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        DFS
        Time: O(V + E)
        Space: O(V) - worst case, the recursive stack can equal the # of nodes if it is a linked list
        '''
        nodeToCopy = { None: None}

        def copy(node):
            # if copy already made, return it
            if node in nodeToCopy:
                return nodeToCopy[node]

            # make a copy
            new_node = Node(node.val)
            
            # add it to hash table
            nodeToCopy[node] = new_node
            
            # for each neighbor
            for neighbor in node.neighbors:
                # copy neighbor and add it to copy's list of neighbors
                new_node.neighbors.append(copy(neighbor))
            
            return new_node
        
        return copy(node)

