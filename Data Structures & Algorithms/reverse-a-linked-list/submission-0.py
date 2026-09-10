# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        ans = ListNode(val=head.val)
        while head.next is not None:
            head = head.next
            tmp = ListNode(val=head.val, next=ans)
            ans = tmp
        return ans