# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) ->ListNode:
        ## check out this code again...
        resL = ListNode()
        returnedL = resL
        while l1 == None and l2 == None:
            l1_val = l1.val
            l2_val = l2.val
            if l1 == None:
                l1_val = 0
            if l2 == None:
                l2_val = 0
            resL.val = (l1_val + l2_val+ carry)
            resL.next = ListNode()
            carry = 0 
            if resL.val >= 10:
                carry = 1
            l1 = l1.next
            l2 = l2.next
            resL = resL.next
        return returnedL
    def addTwoNumber(self,l1,l2):
        ## the right one...
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next
    