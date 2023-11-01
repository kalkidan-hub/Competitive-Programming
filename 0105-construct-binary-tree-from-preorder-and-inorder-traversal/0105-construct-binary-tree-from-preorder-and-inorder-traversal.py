# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        root = preorder[0]
        i = 0
        while inorder[i] != root:
            i += 1
        left_pre = preorder[1:i + 1]
        right_pre = preorder[i + 1:]
        
        left_in = inorder[:i]
        right_in = inorder[i + 1:]
        
        root_tree = TreeNode(preorder[0], self.buildTree(left_pre,left_in),self.buildTree(right_pre,right_in))
        
        return root_tree