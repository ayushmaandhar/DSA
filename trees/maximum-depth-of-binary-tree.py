from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # iterative BFS
    def maxDepth1(self, root: Node) -> int:
        if not root:
            return 0

        q = deque([root])
        depth = 0

        while q:
            level_length = len(q)  # Number of elements (nodes) at the current level (snapshsot)
            for _ in range(level_length):
                node = q.popleft()  # Process nodes at the current level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1  # Increment depth after processing all nodes at the current level

        return depth
    
    # iterative DFS (Pre-order root,left,right)
    def maxDepth2(self, root) -> int:
        if not root:
            return 0
        
        res = 1
        stack = [[root, res]] # initializing stack with [node, depth] in it.
        
        while stack: # while stack is non empty
            node, depth = stack.pop()
            
            if node: # if node is not null/None
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
                
        return res
    
    # Recursive DFS
    def maxDepth3(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))