# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # print([str(2)  + i for i in []]) --> [] that's why we have the second base case.
        if not root:
            return []
        if not root.right and not root.left:
            return [str(root.val)]
        return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)] + [str(root.val) + '->' + j for j in self.binaryTreePaths(root.left)]
            