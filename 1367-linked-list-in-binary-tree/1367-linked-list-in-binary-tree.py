# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        head_str = ""
        while head:
            head_str += str(head.val)
            head = head.next
        
        
        def dfs(root,path):
            if head_str in path:
                return True
            if not root:
                return False
            
            return dfs(root.right,path+str(root.val)) or dfs(root.left,path+str(root.val))
        
        return dfs(root,"")