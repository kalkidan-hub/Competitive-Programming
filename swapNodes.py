class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
       [1,] [2,],[3,], [4,]


        """
        swapped = head
        if head != None and head.next != None:

            while  head != None and head.next != None:
                print(head.val)
                value = head.val
                head.val = head.next.val
                head.next.val = value
                head = head.next.next
        return swapped
