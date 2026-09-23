# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find halfway point
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # slow is the end of the first half
        # reverse the second half
        rev = slow.next
        prev = slow.next = None
        while rev is not None:
            tmp = rev.next
            rev.next = prev
            prev = rev
            rev = tmp

        # input one by one
        first, second = head, prev
        while second is not None:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2