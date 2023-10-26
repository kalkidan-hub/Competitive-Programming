# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def travel(root,store):
            # print(root)
            if not root:
                return
            if not root.right and not root.left:
                store.append(root.val)
                res.append("->".join([str(i) for i in store]))
                return
           
            store.append(root.val)
            store_right = store.copy()
            travel(root.left,store)
            travel(root.right,store_right)
            
        
        travel(root,[])
        return res
            