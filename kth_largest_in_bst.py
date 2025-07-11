class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val 
    self.left = left
    self.right = right

root = TreeNode(4)
root.left = TreeNode(3, TreeNode(2))
root.right = TreeNode(5)

def kth_largest_element(root, k):
	def inorder(node):
		if not node:
			return []

		return inorder(node.left) + [node.val] + inorder(node.right)

	inorder_arr = inorder(root)
	print(inorder_arr)
	return inorder_arr[-k]

print(kth_largest_element(root, 1)) # 5
print(kth_largest_element(root, 2)) # 4
print(kth_largest_element(root, 3)) # 3