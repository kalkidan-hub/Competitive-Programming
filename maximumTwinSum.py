# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        twins = [slow.val]

        i = 0
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            twins.append(slow.val)
            i += 1

        slow = slow.next

        while slow:
            twins[i] += slow.val
            i -= 1
            slow = slow.next

        return max(twins)
