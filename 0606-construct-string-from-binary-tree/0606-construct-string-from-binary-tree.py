# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        left_part = f"({self.tree2str(root.left)})"
        right_part = f"({self.tree2str(root.right)})"
        
        if right_part == '()':
            if left_part != '()':
                return str(root.val) + left_part
            else:
                return str(root.val)
        
        return str(root.val) + left_part + right_part