# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lp = dummy
        rp = head
        for _ in range(n - 1):
            rp = rp.next
        
        while rp.next is not None:
            lp = lp.next
            rp = rp.next

        lp.next = lp.next.next
        return dummy.next
        