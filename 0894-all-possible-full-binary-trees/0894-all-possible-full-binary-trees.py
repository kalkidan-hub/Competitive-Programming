# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        res = []
        
        if n == 1:
            return [TreeNode()]
        
        if (n & 1):
            prev = self.allPossibleFBT(n - 2)
            for left_node in range(1,n,2):
                left_tree = self.allPossibleFBT(left_node)
                right_tree = self.allPossibleFBT(n-1-left_node)
                
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode()
                        root.left = left
                        root.right = right
                         
                        res.append(root)
           
        return res