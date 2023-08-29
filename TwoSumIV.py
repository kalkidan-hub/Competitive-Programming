from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # extracting all values from the binary search tree, BST
        
        values = []
        def node_value(root):
            if not root:
                return 
            values.append(root.val)
            node_value(root.left)
            node_value(root.right)
        node_value(root)
        
        values.sort()
        
        # perform two sum
        i, j = 0, len(values) - 1
        while i != j:
            if values[i] + values[j] == k:
                return True
            else:
                if values[i] + values[j] < k:
                    i += 1
                else:
                    j -= 1
            
        
        return False