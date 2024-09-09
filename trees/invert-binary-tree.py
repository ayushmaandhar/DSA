class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
    def invertTree(self, root):
        
        # we know our code will reach the leaf node for every subtree
        if root is None:
            return None # hence the base condition for recursion
        
        # swapping the left node/subtree to the right one
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left) # going inside left subtree
        self.invertTree(root.right) # going inside right subtree
        
        return root