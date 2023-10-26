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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head:
            return 
        
        origin = head
        dummy = ListNode()
        dummy.next = head
        left = dummy
        
        _len = 0
        while head:
            _len += 1
            head = head.next
        
        head = origin
        orinin = head
        mid = _len//2
        
        for i in range(mid):
            head = head.next
            dummy = dummy.next 
            
        dummy.next = None
        mid_val = head.val
        right = head.next
        left = left.next
        
        
        
        return TreeNode(mid_val,self.sortedListToBST(left),self.sortedListToBST(right))