# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        if not head:
            return head
        
        node = head
        l = 1
        while node.next:
            l += 1
            node = node.next
        k %= l
        
        if k == 0:
            return head
        
        curr = head
        for i in range(l-k-1):
            curr = curr.next
        
        newHead = curr.next
        curr.next = None
        
        node.next = head
            
        return newHead