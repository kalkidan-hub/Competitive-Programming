# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        # general case
        # find mid-point
        ps, pf = head, head
        while pf and pf.next:
            ps = ps.next
            pf = pf.next.next
        
        right_head = ps.next
        reversed_right_head = self.reverseL(right_head)
        ps.next = None

        # insert reversed_right_head into head (reorder)
        pl, pr = head, reversed_right_head
        while pl and pr:
            pl_next = pl.next
            pr_next = pr.next
            pl.next = pr
            pr.next = pl_next
            pl = pl_next
            pr = pr_next
        
        return head

    def reverseL(self, l):
        prev, curr = None, l

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
